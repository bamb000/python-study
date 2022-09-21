import socket
target_host = "www.baidu.com"
target_port = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some data
client.sendto(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n",(target_host,target_port))
# receive some data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()