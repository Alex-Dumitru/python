'''

this will not work on windows, because we don't have the possibility to create raw sockets anymore

helper pages:
1) https://en.wikipedia.org/wiki/Ethernet_frame
2) https://docs.python.org/3/library/struct.html
3) https://docs.python.org/3/library/socket.html
4) https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
5) https://stackoverflow.com/questions/3792407/python-socket-pf-packet

not completed: for continuation see: https://www.cybrary.it/video/packet-analyzer-part-2/
'''

#!/usr/bin/python

import socket
import os
import struct
import binascii


def analyze_ether_header(data):
    ip_bool = False
    # the mapping !6s6sH starts at the MAC octets
    # see 1) and 2) for mapping
    eth_hdr  = struct.unpack('!6s6sH', data[:14])  # IPv4 = 0x0800
    dest_mac = binascii.hexlify(eth_hdr[0])   # destination address
    src_mac  = binascii.hexlify(eth_hdr[1])   # source address
    proto    = eth_hdr[2]                     # next protocol

    print(dest_mac)
    print(src_mac)
    print(hex(proto))

    if hex(proto) == 0x0800: # IPv4
        ip_bool = True
    data = data[14:]
    return data, ip_bool

def main():
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    # sniffer_socket.bind()
    # raw sockets don't need to be binded to any specific port
    # if we bind it, it will only listen to traffic on that specific port
    recv_data = sniffer_socket.recv(2048)
    # return from recv comes in a struct format, so it's not really possible to print it all the time
    os.system('clear')

    data, ip_bool = analyze_ether_header(recv_data)

while True:
    main()
