import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    result_list = []
    for item in message.split(','):
        item = int(item)
        result_list.append(item)

    print(f"Received {message!r} from {addr!r}")

    print(f"{result_list[0]} + {result_list[1]} = {sum(result_list)!r}")
    writer.write(f"{result_list[0]} + {result_list[1]} = {sum(result_list)!r}".encode())
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
