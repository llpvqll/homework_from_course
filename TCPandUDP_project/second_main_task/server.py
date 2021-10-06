import socket

local_ip = '127.0.0.1'
local_port = 20001
buffer_size = 1024

msg_from_server = "Hello UDP Client"
bytes_to_send = str.encode(msg_from_server)

# create a datagram socket
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
udp_server_socket.bind((local_ip, local_port))
print('UDP server up and listening!')

# Listening for incoming datagrams
while True:
    bytes_address_pair = udp_server_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]

    client_msg = 'Message from Client: {}'.format(message)
    client_ip = "Client IP Address: {}".format(address)

    print(client_msg)
    print(client_ip)

#     Sending a reply to client
    udp_server_socket.sendto(bytes_to_send, address)
