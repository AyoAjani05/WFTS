import socket
import os
import time

s = socket.socket()

# help(s.recvfrom)
s.connect(("127.0.0.1", 12345))

msg_recv = s.recv(1024).decode().split("#")

if msg_recv[0] == 'File':
    File_Name = os.path.basename(msg_recv[1])
    print(File_Name)
    Size = int(msg_recv[-1])
    
    with open(File_Name, "wb") as file:
        while Size:
            if Size > 1024:
                mg = s.recv(1024)
                file.write(mg)
                Size -= 1024
                print('Packet Received')
            else:
                mg = s.recv(Size)
                file.write(mg)
                Size -= Size
                print('Packet Received')
            time.sleep(1.5)
            s.send("Packet Received".encode())
# print(msg_recv)

s.close()

print(os.getcwd())