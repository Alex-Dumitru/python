import socket
import time

'''
Python server which will:
receive a connection from a client (see Client.py),
store received data in a file then add the file to a list,
return the data from a sotred file if requested to do so
deal with errors and missing files
'''
def save_data(connection):
    fname = connection.recv(5).decode()
    fobj = open(fname, 'a+')
    data = connection.recv(1024).decode()
    print(fname, data)
    fobj.write(data)
    fobj.close()
    connection.close()
    return fname


def load_data(connection, fname):
    fobj = open(fname, 'r+')
    data = fobj.read()
    print(fname, data)
    connection.send(data.encode('utf-8'))
    connection.close()
    fobj.close()
    return

def main():
    HOST = ''
    PORT = 50000
    sentinel = False
    opts_list = ['SAVE', 'LOAD']
    file_list = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    while sentinel != True:
        s.listen(1)
        connection, address = s.accept()
        mode = connection.recv(4).decode()
        if mode == opts_list[0]: #SAVE
            print(mode)
            file_list.append(save_data(connection))

        elif mode == opts_list[1]: #LOAD
            print(mode)
            fname = connection.recv(5).decode()
            if fname not in file_list:
                connection.send('File Not Found'.encode('utf-8'))
                connection.close()
            else:
                load_data(connection, fname)

        else:
            print('Mode: ',mode)
            sentinel = True

    s.close()
main()
