from tkinter import Frame, Label, BOTH, Button, Tk, Entry
from tkinter.filedialog import askopenfilenames, askdirectory
import pathlib
import os
import re

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


    def ip_config(self):
        try:
            self.ip_full = os.popen("ipconfig").read()
            self.ip = "Your IP address is " + re.search(string=self.ip_full, pattern=r"IPv4 Address.*").group().split(":")[-1].strip()
        except AttributeError:
            self.ip = "Looks like you're not connected a LAN network, Please connect to one and then try again."


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

        self.opener_text = self.ip
        self.Send_Label = Label(self.Send_frame, text=self.opener_text, font=(self.font, self.size), wraplength=250)
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
        self.Send_Filename_entry.insert(0, " ,".join([os.path.basename(i) for i in self.File_names]))

        self.select_filename_button = Button(self.Send_frame_3, text="Select Another File", command=self.Filename_Inquiry_System)
        self.select_filename_button.grid(row=1, column=0)

        self.send_confirm_btn = Button(self.Send_frame_3, text="Confirm", width=15)
        self.send_confirm_btn.grid(row=1, column=1, padx=78, pady=20)


    def Filename_Inquiry_System(self):
        self.File_names = askopenfilenames(filetypes=[("All Types", '*.*')])
        while not self.File_names:
            self.File_names = askopenfilenames(filetypes=[("All Types", '*.*')])
        self.Send_Window_create_widgets_cont()


    def Receive_Window_create_widgets(self):
        """
        Create various widgets inside the tkinter interface.
        """
        self.Receive_frame = Frame(self.master)
        self.Receive_frame.pack(fill=BOTH, pady=0)

        self.opener_text = self.ip
        self.Receive_Label = Label(self.Receive_frame, text=self.opener_text, font=(self.font, self.size), wraplength=250)
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

        self.Receive_confirm_btn = Button(self.Receive_frame_3, text="Confirm", width=15)
        self.Receive_confirm_btn.grid(row=1, column=1, padx=60, pady=20)


    def Folder_Inquiry_System(self):
        self.Folder = askdirectory(initialdir=pathlib.Path.home())
        while not self.Folder:
            self.Folder = askdirectory(initialdir=pathlib.Path.home())
        self.Receive_Window_create_widgets_cont()

    def send_confirm(self):
        self.send_connection_status = "Waiting for Receiver"


    def back(self):
        if self.current_window == "Send 1":
            self.clear_window()
            self.welcome_window()
        elif self.current_window == "Receive 1":
            self.clear_window()
            self.welcome_window()


    def receive_window(self):
        self.ip_config()
        self.clear_window()
        self.current_window = "Receive 1"
        self.Receive_Window_create_widgets()


    def send_window(self):
        self.ip_config()
        self.clear_window()
        self.current_window = "Send 1"
        self.Send_Window_create_widgets()


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
