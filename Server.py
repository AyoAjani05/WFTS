import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 12345

s.bind(("", PORT))

s.listen()
print("Listening...", s.getsockname())


object, address = s.accept()
print(address)
transfer_rate = 1024 * 1024
if address:
    File_Name = r"C:\Users\USPF\Downloads\Blue Exorcist - S00E13 - OVA Kyoto Impure King.mkv"
    Size = os.path.getsize(File_Name)
    Transfer_Protocol = "File#" + File_Name + "#" + str(Size)
    print(Transfer_Protocol)
    object.send(Transfer_Protocol.encode())
    msg = object.recv(transfer_rate).decode()
    print(msg)
    with open(File_Name, 'rb') as file:
        while Size:
            if Size >= transfer_rate:
                object.send(file.read(transfer_rate))
                Size -= transfer_rate
            else:
                print(True)
                object.send(file.read(Size))
                Size -= Size
            msg = object.recv(transfer_rate).decode()
            print(Size, msg)
    object.send("Hello".encode())

s.close()
