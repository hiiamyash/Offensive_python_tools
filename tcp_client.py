import socket

host = "127.0.0.1"
port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.send(b"GET /HTTP/.1\r\nost:127.0.0.1\r\n\r\n")

revice = client.recv(4096)

print(revice.decode())





