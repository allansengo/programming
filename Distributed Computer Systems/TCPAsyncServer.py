from socket import socket, AF_INET, SOCK_STREAM
#from threading import Thread
from asyncio import get_event_loop, run, ensure_future


async def handle_connection(client_sock, addr):
    print(f"Accepted connection from {addr}.")
    ev_loop = get_event_loop()

    while True:
        bin_data = await ev_loop.sock_recv(client_sock, buf_size)
        data = bin_data.decode()
        if (data == "\quit"):
            print(f"Quiting the connection with {addr}!")
            break
        else:
            print(f"\nReceived message '{data}' from {addr}")

    client_sock.close()


async def wait_for_connections(TCPSock):
    ev_loop = get_event_loop()
    while True:
        TCPSock.listen(10)
        client_sock, addr = await ev_loop.sock_accept(TCPSock)
        #await serve_connection(client_sock, addr)
        ensure_future(handle_connection(client_sock, addr))



host = "localhost"
#host = "127.0.0.1"
port = 2223
buf_size = 1024

addr = (host, port)
TCPSock = socket(AF_INET, SOCK_STREAM)
TCPSock.setblocking(False)
TCPSock.bind(addr)

ev_loop = get_event_loop()
ev_loop.run_until_complete(wait_for_connections(TCPSock))

TCPSock.close()

