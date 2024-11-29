from tkinter import Frame, Label, BOTH, Button, Tk, Entry, IntVar, ttk
from tkinter.filedialog import askopenfilenames, askdirectory
import pathlib
import os
import re
import threading
import socket
import signal

class PROMPT:
    """
    A class representing a custom prompt interface using tkinter for file organization.

    Attributes:
        master (Tk): The tkinter root window.
    """

    def __init__(self, master, x=300, y = 200):
        """
        Initializes the prompt window and displays the selected directory.

        Args:
            master (Tk): The tkinter root window.
        """

        self.master = master
        self.master.title('WFTS')
        self.x, self.y = x, y
        self.master.geometry(f"{self.x}x{self.y}")
        self.opener_text = None
        self.font, self.size = 'Arial', 12
        self.Welcome_frame, self.send_btn = None, None
        self.receive_btn = None
        self.Welcome_Label = None
        self.current_window = None
        self.Back_btn = None
        self.File_names = ''
        self.ip = "Loading...".rjust(30, ' ')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 12345
        self.thread_id = None


    def kill(self, pid):
        # os.kill(pid, signal.SIGTERM)
        self.socket.close()
        self.T1.join()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def ip_thread(self, event=None):
        t1 = threading.Thread(target=self.ip_config, args=(event,))
        t1.start()
        # t1.join()


    def ip_config(self, event=None):
        try:
            self.ip_full = os.popen("ipconfig").read()
            self.ip = "Your IP address is " + re.search(string=self.ip_full, pattern=r"IPv4 Address.*").group().split(":")[-1].strip()
        except AttributeError:
            self.ip = "Looks like you're not connected a LAN network, Please connect to one and then try again."

        event.configure(text=self.ip)
        self.master.update_idletasks()


    def Welcome_Window_create_widgets(self):
        """
        Create various widgets inside the tkinter interface.
        """
        self.opener_text = "Welcome to the WFTS"
        self.Welcome_Label = Label(self.master, text=self.opener_text, font=(self.font, self.size))
        self.Welcome_Label.pack(anchor='n')

        self.Welcome_frame = Frame(self.master)
        self.Welcome_frame.pack(fill=BOTH, expand=True)

        self.send_btn = Button(self.Welcome_frame, text='Send', height=2, width=10, command=self.send_window)
        self.send_btn.grid(row=0, column=0, padx=30, pady=40)

        self.receive_btn = Button(self.Welcome_frame, text='Receive', height=2, width=10, command=self.receive_window)
        self.receive_btn.grid(row=0, column=1, padx=30, pady=40)


    def Send_Window_create_widgets(self):
        """
        Create various widgets inside the tkinter interface.
        """
        self.Send_frame = Frame(self.master)
        self.Send_frame.pack(fill=BOTH, pady=0)

        self.Send_Label = Label(self.Send_frame, text=self.ip, font=(self.font, self.size), wraplength=250)
        self.Send_Label.grid(row=0, column=1, columnspan=3)
        self.Back_btn = Button(self.Send_frame, text='<=', height=3, bd=0, command = self.back)
        self.Back_btn.grid(row=0, column=0,rowspan=1)

        self.Send_frame_2 = Frame(self.master)
        self.Send_frame_2.pack(fill=BOTH, pady=0)

        self.filename_label = Label(self.Send_frame_2, text="Filename: ", font=(self.font, self.size), wraplength=-1)
        self.filename_label.grid(row=0, column=0)

        self.select_filename_button = Button(self.Send_frame_2, text="Select File", command=self.Filename_Inquiry_System)
        self.select_filename_button.grid(row=0, column=1, padx=20)

        self.Send_frame_3 = Frame(self.master)
        self.Send_frame_3.pack(fill=BOTH, expand=True, pady=0)


    def Send_Window_create_widgets_cont(self):
        self.select_filename_button.destroy()
        self.Send_Filename_entry = Entry(self.Send_frame_2, width=35, bd=0)
        self.Send_Filename_entry.grid(row=0, column=1)
        self.Send_Filename_entry.insert(0, os.path.basename(self.File_names))

        self.select_filename_button = Button(self.Send_frame_3, text="Select Another File", command=self.Filename_Inquiry_System)
        self.select_filename_button.grid(row=1, column=0)

        self.send_confirm_btn = Button(self.Send_frame_3, text="Confirm", width=15, command=self.confirm)
        self.send_confirm_btn.grid(row=1, column=1, padx=78, pady=20)


    def Filename_Inquiry_System(self):
        self.File_names = askopenfilenames(filetypes=[("All Types", '*.*')])[0]
        while not self.File_names:
            self.File_names = askopenfilenames(filetypes=[("All Types", '*.*')])[0]
        print(self.File_names)
        self.Send_Window_create_widgets_cont()


    def Receive_Window_create_widgets(self):
        """
        Create various widgets inside the tkinter interface.
        """
        self.Receive_frame = Frame(self.master)
        self.Receive_frame.pack(fill=BOTH, pady=0)

        self.Receive_Label = Label(self.Receive_frame, text=self.ip, font=(self.font, self.size), wraplength=250)
        self.Receive_Label.grid(row=0, column=1, columnspan=3)
        self.Back_btn = Button(self.Receive_frame, text='<=', height=3, bd=0, command = self.back)
        self.Back_btn.grid(row=0, column=0,rowspan=1)

        self.Receive_frame_2 = Frame(self.master)
        self.Receive_frame_2.pack(fill=BOTH, pady=0)

        self.Receive_Label_2 = Label(self.Receive_frame_2, text="Folder: ", font=(self.font, self.size), wraplength=-1)
        self.Receive_Label_2.grid(row=0, column=0)

        self.select_folder_button = Button(self.Receive_frame_2, text="Select Folder", command=self.Folder_Inquiry_System)
        self.select_folder_button.grid(row=0, column=1, padx=20)

        self.Receive_frame_3 = Frame(self.master)
        self.Receive_frame_3.pack(fill=BOTH, expand=True, pady=0)


    def Receive_Window_create_widgets_cont(self):
        self.select_folder_button.destroy()
        self.Receive_Folder_entry = Entry(self.Receive_frame_2, width=35, bd=0)
        self.Receive_Folder_entry.grid(row=0, column=1)
        self.Receive_Folder_entry.insert(0, self.Folder)

        self.select_folder_button = Button(self.Receive_frame_3, text="Select Another Folder", command=self.Folder_Inquiry_System)
        self.select_folder_button.grid(row=1, column=0)

        self.Receive_confirm_btn = Button(self.Receive_frame_3, text="Confirm", width=15, command=self.confirm)
        self.Receive_confirm_btn.grid(row=1, column=1, padx=60, pady=20)


    def Folder_Inquiry_System(self):
        self.Folder = askdirectory(initialdir=pathlib.Path.home())
        while not self.Folder:
            self.Folder = askdirectory(initialdir=pathlib.Path.home())
        self.Receive_Window_create_widgets_cont()


    def send_transfer_confirm(self):
        self.Ctrl_frame = Frame(self.master)
        self.Ctrl_frame.pack(fill=BOTH, pady=0)

        self.Ctrl_Label = Label(self.Ctrl_frame, text=f"IP: {self.ip}\nWaiting for Receiver...", font=(self.font, self.size), wraplength=250)
        self.Ctrl_Label.grid(row=0, column=1, columnspan=3)
        self.Back_btn = Button(self.Ctrl_frame, text='<=', height=3, bd=0, command = self.back)
        self.Back_btn.grid(row=0, column=0,rowspan=1)

        self.Ctrl_frame_2 = Frame(self.master)
        self.Ctrl_frame_2.pack(fill=BOTH, pady=0)


    def send_transfer_confirm_cont(self):
        self.progress = IntVar()
        self.progressbar = ttk.Progressbar(self.Ctrl_frame_2, maximum=100, variable=self.progress)
        self.progressbar.pack()


    def send(self, transfer_rate=1024):
        self.thread_id = threading.get_ident()
        print(self.thread_id)
        self.socket.bind(("", self.port))

        self.socket.listen(1)
        print("Listening...")

        object, address = self.socket.accept()
        self.Ctrl_Label.configure(text=('Connected to IP: ' + address[0]).rjust(30, " "))
        self.send_transfer_confirm_cont()
        self.master.update_idletasks()
        if address:
            Ori_Size = os.path.getsize(self.File_names)
            Size = Ori_Size
            Transfer_Protocol = "File#" + self.File_names + "#" + str(Size)
            print(Transfer_Protocol)
            object.send(Transfer_Protocol.encode())
            with open(self.File_names, 'rb') as file:
                while Size:
                    if Size > transfer_rate:
                        object.send(file.read(transfer_rate))
                        Size -= transfer_rate
                        # print('sending')
                    else:
                        object.send(file.read(Size))
                        Size -= Size
                    msg = object.recv(transfer_rate).decode()
                    # print(Size, msg)
                    percent_complete = ((Ori_Size-Size)/ Ori_Size) * 100
                    print(percent_complete)
                    # Update progress bar and potentially add visual delay for effect
                    self.progress.set(percent_complete)
                    self.progressbar.update_idletasks()
            self.Ctrl_Label.configure(text=('Done').rjust(30, " "))
            self.master.update_idletasks()
            self.master.after(5000, self.master.destroy)
        self.socket.close()


    def Receive_transfer_confirm(self):
        self.Ctrl_frame = Frame(self.master)
        self.Ctrl_frame.pack(fill=BOTH, pady=0)

        self.Ctrl_Label = Label(self.Ctrl_frame, text=f"Enter IP Address Of Sender".rjust(30, " "), font=(self.font, self.size), wraplength=250)
        self.Ctrl_Label.grid(row=0, column=1, columnspan=3)
        self.Back_btn = Button(self.Ctrl_frame, text='<=', height=3, bd=0, command = self.back)
        self.Back_btn.grid(row=0, column=0,rowspan=1)

        self.Ctrl_frame_2 = Frame(self.master)
        self.Ctrl_frame_2.pack(fill=BOTH, pady=0)
        self.Ctrl_Entry = Entry(self.Ctrl_frame_2, font=(self.font, self.size))
        self.Ctrl_Entry.grid(row=0, column=1, columnspan=3, padx=50)

        self.Ctrl_frame_3 = Frame(self.master)
        self.Ctrl_frame_3.pack(fill=BOTH, pady=0)
        self.Ctrl_btn = Button(self.Ctrl_frame_3, text="Confirm", width=15, bd=0, command=self.receive_transfer_confirm_cont)
        self.Ctrl_btn.pack(pady=20)


    def receive_transfer_confirm_cont(self):
        self.text = self.Ctrl_Entry.get().strip()
        self.Ctrl_Entry.destroy()
        self.Ctrl_frame_3.destroy()
        self.progress = IntVar()
        self.progressbar = ttk.Progressbar(self.Ctrl_frame_2, maximum=100, variable=self.progress)
        self.progressbar.pack()
        # self.T1 = threading.Thread(target=self.Receive)
        # self.T1.start()


    def receive(self, transfer_rate=1024):
        self.socket.connect((self.text, self.port))

        self.Ctrl_Label.configure(text=('Connected to IP: ' + self.text).rjust(30, " "))
        self.receive_transfer_confirm_cont()
        self.master.update_idletasks()
        msg_recv = self.socket.recv(transfer_rate).decode().split("#")
        print(msg_recv)

        if msg_recv[0] == 'File':
            File_Name = os.path.basename(msg_recv[1])
            print(File_Name)
            Ori_Size = int(msg_recv[-1])
            Size = Ori_Size

            path = pathlib.path(self.Folder, File_Name)
            with open(path, "wb") as file:
                while Size:
                    if Size > transfer_rate:
                        mg = self.socket.recv(transfer_rate)
                        file.write(mg)
                        Size -= transfer_rate
                        print('Packet Received')
                    else:
                        mg = self.socket.recv(Size)
                        file.write(mg)
                        Size -= Size
                        print('Packet Received')
                    self.socket.send("Packet Received".encode())
                    percent_complete = ((Ori_Size-Size)/ Ori_Size) * 100
                    print(percent_complete)
                    # Update progress bar and potentially add visual delay for effect
                    self.progress.set(percent_complete)
                    self.progressbar.update_idletasks()
            self.Ctrl_Label.configure(text=('Done').rjust(30, " "))
            self.master.update_idletasks()
            self.master.after(5000, self.master.destroy)
        self.socket.close()
        print(msg_recv)

        self.socket.close()


    def confirm(self):
        if self.current_window == "Send 1" and self.ip.startswith("Your "):
            self.clear_window()
            self.current_window = "Send 2"
            self.send_transfer_confirm()
            self.T1 = threading.Thread(target=self.send)
            self.T1.start()

        elif self.current_window == "Receive 1" and self.ip.startswith("Your "):
            self.clear_window()
            self.current_window = "Receive 2"
            self.Receive_transfer_confirm()
        else:
            pass


    def back(self):
        if self.current_window == "Send 1":
            self.clear_window()
            self.welcome_window()
            self.ip = "Loading...".rjust(30, ' ')
        elif self.current_window == "Receive 1":
            self.clear_window()
            self.welcome_window()
            self.ip = "Loading...".rjust(30, ' ')
        elif self.current_window == "Send 2":
            self.ip = "Loading...".rjust(30, ' ')
            self.clear_window()
            self.send_window()
            if self.thread_id:
                self.kill(self.thread_id)
                print("Killed")
        elif self.current_window == "Receive 2":
            self.ip = "Loading...".rjust(30, ' ')
            self.clear_window()
            self.receive_window()


    def receive_window(self):
        self.clear_window()
        self.current_window = "Receive 1"
        self.Receive_Window_create_widgets()
        self.ip_thread((self.Receive_Label))


    def send_window(self):
        self.clear_window()
        self.current_window = "Send 1"
        self.Send_Window_create_widgets()
        self.ip_thread((self.Send_Label))


    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()


    def welcome_window(self):
        self.current_window = "Welcome 1"
        self.Welcome_Window_create_widgets()


    def main(self):
        """
        Starts the application by running the organization logic and entering the main event loop.
        """
        self.welcome_window()
        self.master.mainloop()

b = Tk()
P = PROMPT(b)
P.main()
