import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 12345

s.bind(("", PORT))

s.listen()
print("Listening...")


object, address = s.accept()
print(address) 
if address:
    File_Name = r"C:\Users\HP\Videos\CSC202 pq\CSC QUESTION 2018.docx"
    Size = os.path.getsize(File_Name)
    Transfer_Protocol = "File#" + File_Name + "#" + str(Size)
    print(Transfer_Protocol)
    object.send(Transfer_Protocol.encode())
    with open(File_Name, 'rb') as file:
        while Size:        
            if Size > 1024:
                object.send(file.read(1024))
                Size -= 1024
                # print('sending')
            else:
                object.send(file.read(Size))
                Size -= Size
            msg = object.recv(1024).decode()
            print(Size, msg)
    # object.send("Hello".encode())

s.close()
