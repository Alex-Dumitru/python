'''
This is a drive-wide, FTP-like tool.
The server receives multiple connections, each on their own thread and takes several commands:

DRIVESEARCH <filename>
    DRIVESEARCH looks for the given filename across the entire drive. If it finds the file, it sends back the drive
    location.

DIRSEARCH <directory> <filename>
    DIRSEARCH looks for th file in the given directory or its subdirectories.
    If it fnds the file, it sends back the location.

DOWNLOAD <filename>
    DOWNLOAD requires the full file path, or at least the relative path of the file. It send the contents of the file
    across the network.

UPLOAD <filename>
    UPLOAD requires the full file path, or at least the relative path where the user wants to locate the file. It reads
    the file contents from across the network connection

CLOSE
    CLOSE ends the connection

This project requires the use of multithreading, ctypes, regex and some other libraries
'''

import os
import re
import socket
import threading
import struct
import ctypes
import sys


def read_file(filename):  # ctypes
    file_handle = ctypes.windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 3, 0x80, 0)
    if file_handle == -1:
        return -1

    data = ctypes.create_string_buffer(4096)
    data_read = ctypes.c_int(0)
    bool_success = ctypes.windll.Kernel32.ReadFile(file_handle, ctypes.byref(data), 4096, ctypes.byref(data_read), 0)
    ctypes.windll.Kernel32.CloseHandle(file_handle)
    if bool_success == 0:
        return -1
    return data.value


def create_file(filename, data):  # ctypes
    file_handle = ctypes.windll.Kernel32.CreateFileA(filename, 0x10000000, 0, 0, 2, 0x80, 0)
    if file_handle == -1:
        return -1

    data_written = ctypes.c_int(0)
    bool_success = ctypes.windll.Kernel32.WriteFile(file_handle, data, len(data), ctypes.byref(data_written), 0)
    ctypes.windll.Kernel32.CloseHandle(file_handle)
    if bool_success == 0:
        return -1
    return


def recv_data(sock):  # networking protocol
    data_len, = struct.unpack("!I", sock.recv(4))
    return sock.recv(data_len).decode("utf-8")


def send_data(sock, data):  # networking protocol
    data_len = len(data)
    sock.send(struct.pack("!I", data_len))
    sock.send(data.encode('utf-8'))
    return


def search_drive(filename):  # DRIVESEARCH
    re_obj = re.compile(filename)
    for root, dirs, files in os.walk("C:\\"):
        for f in files:
            print(f)
            if re.search(re_obj, f):
                return os.path.join(root, f)
        return -1


def search_directory(filename):  # DIRSEARCH
    re_obj = re.compile(filename)
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if re.search(re_obj, f):
                return os.path.join(root, f)
        return -1


def send_file_content(filename, usersock, userinfo):  # DOWNLOAD
    send_data(usersock, read_file(filename))
    return


def recv_file_content(filename, usersock):  # UPLOAD
    if create_file(filename, recv_data(usersock)) == -1:
        send_data(usersock, 'File creation failed!')
    return


def main():
    command_list = ['DRIVESEARCH',
                    'DIRSEARCH',
                    'DOWNLOAD',
                    'UPLOAD',
                    'CLOSE']

    cont = True

    if len(sys.argv) < 2:
        print("Usage: %s [IP ADDRESS]" % sys.argv[0])
        exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((sys.argv[1],55555))
    except:
        print("Cannot connect to %s" % sys.argv[1])


    while cont != False:
        command = input(recv_data(sock)).upper()
        send_data(sock, command)
        if command not in command_list:
            print(recv_data(sock))
            print(command_list)

        elif command == 'DRIVESEARCH':
            file_name = input(recv_data(sock))
            send_data(sock, file_name)
            print(recv_data(sock))

        elif command == 'DIRSEARCH':
            file_name = input(recv_data(sock))
            send_data(sock, file_name)
            print(recv_data(sock))

        elif command == 'DOWNLOAD':
            file_name = input(recv_data(sock))
            send_data(sock, file_name)
            recv_file_content(input("Local filename: "), sock)

        elif command == 'UPLOAD':
            file_name = input(recv_data(sock))
            new_file_name = input("File to create: ")
            send_data(sock, new_file_name)
            send_file_content(file_name, sock)

        elif command == 'CLOSE':
            cont = False

    return


main()