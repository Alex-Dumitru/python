import socket
import time

'''
Python server which will:
receive a connection from a client (see Client.py),
store received data in a file then add the file to a list,
return the data from a sotred file if requested to do so
deal with errors and missing files

implement objects instead of directly files
'''

class datasave:
    def __init__(self, name='', data=''):
        self.name = name
        self.data = data
        return

    def load(self, connection):
        connection.send(self.data.encode('utf-8'))
        connection.close()
        return

def main():
    HOST = ''
    PORT = 50000
    sentinel = False
    found_file = False
    opts_list = ['SAVE', 'LOAD']
    obj_list = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    while sentinel != True:
        s.listen(1)
        connection, address = s.accept()
        mode = connection.recv(4).decode()
        if mode == opts_list[0]: #SAVE
            print(mode)
            obj = datasave(connection.recv(5).decode(), connection.recv(1024).decode())
            connection.close()
            obj_list.append(obj)

        elif mode == opts_list[1]: #LOAD
            print(mode)
            name = connection.recv(5).decode()
            for obj in obj_list:
                if obj.name == name:
                    found_file = True
                    obj.load(connection)
            if found_file == False:
                connection.send('File not found'.encode('utf-8'))
            else:
                found_file = False #Always reset sentinels
        else:
            print('Mode: ',mode)
            sentinel = True

    s.close()
main()
