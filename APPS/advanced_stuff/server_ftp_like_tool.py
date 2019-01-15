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
    data = read_file(filename)
    if data == -1:
        send_data(usersock, 'FILE NOT FOUND!')
    else:
        send_data(usersock, data)
    return


def recv_file_content(filename, usersock):  # UPLOAD
    if create_file(filename, recv_data(usersock)) == -1:
        send_data(usersock, 'File creation failed!')
    return


def handle_connection(usersock, userinfo):
    command_list = ['DRIVESEARCH',
                    'DIRSEARCH',
                    'DOWNLOAD',
                    'UPLOAD',
                    'CLOSE']

    continue_bool = True

    while continue_bool:
        send_data(usersock, "COMMAND: ")
        command = recv_data(usersock).upper()

        if command == 'DRIVESEARCH':
            send_data(usersock, 'Filename: ')
            search_results = search_drive(recv_data(usersock))
            if search_results == -1:
                send_data(usersock, "FILE NOT FOUND!")
            else:
                send_data(usersock, search_results)

        elif command == 'DIRSEARCH':
            send_data(usersock, 'Filename: ')
            search_results = search_directory(recv_data(usersock))
            if search_results == -1:
                send_data(usersock, "FILE NOT FOUND!")
            else:
                send_data(usersock, search_results)

        elif command == 'DOWNLOAD':
            send_data(usersock, 'Filename: ')
            send_file_content(recv_data(usersock), usersock, userinfo)

        elif command == 'UPLOAD':
            send_data(usersock, 'Filename: ')
            recv_file_content(recv_data(usersock), usersock)

        elif command == 'CLOSE':
            continue_bool = False

        else:
            send_data(usersock, 'INVALID COMMAND')
    return


def main():

    while True:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind(('', 55555))
        server_sock.listen(8)
        usersock, userinfo = server_sock.accept()
        handle_connection(usersock,userinfo)
        # conn_thread = threading.Thread(None, handle_connection, None, (usersock, userinfo))
        # conn_thread.start()

    return


main()