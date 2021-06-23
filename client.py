import socket
import sys
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

while True:
    sockets_list = [sys.stdin, client]

    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
