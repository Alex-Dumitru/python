import socket # all socket operations and defines the means of accessing BSD sockets for network communication

'''
https://docs.python.org/3/library/socket.html#module-socket
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
    sock - var name for the socket object which will be returned
    socket.socket() - constructor function for socket objects
    socket.AF_INET - IPv4
        socket.AF_INET6 - IPv6
    socket.SOCK_STREAM - TCP
        socket.SOCK_DGRAM - UDP
'''

HOST = ''    # this will bind on any network interface (if you want, you can write a specific IP address)
PORT = 50000

sock.bind((HOST, PORT))
'''
bind takes only 1 argument, to make sure you pass in a tuple with your HOST, PORT pair
associates a socket object with a specific interface and port
'''

sock.listen(1)
'''
    sock.listen() - sets the socket object in blocking mode waiting for a client to attempt a connection
    1 - listen_queue - determines the number of connections to permit while waiting for acceptance. Older systems need a lower number
    but modern computers can pretty much listen for as many as necessary
'''

conn, addr = sock.accept()
'''
    conn - a new socket object, this one is for a specific client connection, whereas the 'sock' object was for our server to listen
    addr - address information about the client (IP, port, etc)
    sock.accept() - returns a tuple - this is where a connection is fully negotiated, and data can begin travelling back and forward
'''

'''
After you issue the accept() method, your program waits for a connection. To do this, create a new socket and connect to the port used
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',50000))
'''
>>> print(s)
<socket.socket fd=124, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 59199)
, raddr=('127.0.0.1', 50000)>
>>>


>>> print(conn)
<socket.socket fd=116, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 50000)
, raddr=('127.0.0.1', 59199)>
>>> print(addr)
('127.0.0.1', 59199)
>>> print(sock)
<socket.socket fd=456, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 50000)
>>>


! From now on, all communication is done on CONN object, not SOCK, just because that is the one between client and server. SOCK is just for SERVER
'''

conn.recv(1024)

'''
    conn.recv() - received data from a connection
    1024 - buffer size is the amount of data to accept (good to use power of 2s, easier for the computer to work with it)
'''

s.send(b'Hello, world!')

'''
    s.send() - sends a buffer to the specified target and returns the number of bytes sent. This return value is a useful error check, make sure you send as much
    as you think you do
    string_argument - can be a hard-coded string or a variable you define and populate elsewhere
                    - has to be transmited in bytes !!!!

https://stackoverflow.com/questions/42612002/python-sockets-error-typeerror-a-bytes-like-object-is-required-not-str-with?noredirect=1&lq=1
    you can also send interactive text by using input('prompt_here: ').encode('utf-8')
'''

conn.close()
s.close()
sock.close()
'''
The last socket function to use, this terminates the connection, and frees up the memory. The interpreter will do this automatically, but again; good habits
are good habits

>>> print(conn, sock)
<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
>>>

>>> print(s)
<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
'''
