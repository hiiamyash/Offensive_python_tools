import socket
import threading
import argparse


def main():

    parser = argparse.ArgumentParser(description="Users Ip and port input")

    parser.add_argument('-t','--target',required=True,help="Give Target Ip")
    parser.add_argument('-p','--port',required=True,type=int,help="Give the target port to listen on")
    args = parser.parse_args()

    ip = args.target
    port = args.port

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)
    print(f"[-*-] Listning on {ip}:{port}\n")

    while True:
        client ,addres = server.accept()
        print(f"Bro you got an connection from IP {addres[0]} and Port {addres[1]}")
        client_handler= threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
def handle_client(client_socket):

    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recived: {request.decode("utf-8")}')

        sock.send(b"ACK")


if __name__ == "__main__":
    main()




