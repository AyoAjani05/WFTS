import socket
import os
# import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.close()

# help(s.recvfrom)
s.connect(("127.0.0.1", 12345))

transfer_rate = 1024
print("Connected")
msg_recv = s.recv(transfer_rate).decode().split("#")
print(msg_recv)
s.send("Done".encode())


if msg_recv[0] == 'File':
    File_Name = os.path.basename(msg_recv[1])
    print(File_Name)
    Size = int(msg_recv[-1])

    with open(File_Name, "wb") as file:
        while Size:
            if Size > transfer_rate:
                mg = s.recv(transfer_rate)
                file.write(mg)
                Size -= transfer_rate
                print('Packet Received')
            else:
                mg = s.recv(Size)
                file.write(mg)
                Size -= Size
                print('Packet Received')
            # time.sleep(1.5)
            s.send("Packet Received".encode())
print(msg_recv)

s.close()

