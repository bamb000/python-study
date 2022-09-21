import socket
from time import sleep
target_host = "127.0.0.1"
target_port = 9998
data=input().encode()
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The AF_INET parameter indicates we’ll use a standard IPv4 address
# or hostname, and SOCK_STREAM indicates that this will be a TCP client. We
# then connect the client to the server

# connect the client
client.connect((target_host,target_port))
# send some data
# client.send(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
# while True:
client.send(data)
# receive some data
response = client.recv(4096)
print(response.decode())
sleep(3)
    # a=input()
    # if a=="y":
    #     continue
    # else:
    #     break
# f = open(r"C:\Users\57328\Desktop\python\1.html", "w", encoding="utf-8")
# f.write(response.decode())
# f.close()
client.close()