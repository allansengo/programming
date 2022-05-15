from asyncio import start_server, get_event_loop

host = "localhost"
port = 2223
buf_size = 1024

async def handle_client(reader, writer):
    data = None
    addr = writer.transport.get_extra_info("peername")
    print(f"Accepted connection from {addr}.")
    while True:
        bin_data = (await reader.read(buf_size))
        data = bin_data.decode()
        if (data == "\quit"):
            print(f"Quiting connection with {addr}!")
            break
        print(f"\nReceived message '{data}' from {addr}")
    writer.close()

loop = get_event_loop()
loop.create_task(start_server(handle_client, host, port))
loop.run_forever()

