from tkinter import Frame, Label, BOTH, Button, Tk
from tkinter.filedialog import askopenfilenames
# import pathlib
# import os

class PROMPT:
    """
    A class representing a custom prompt interface using tkinter for file organization.

    Attributes:
        master (Tk): The tkinter root window.
    """

    def __init__(self, master):
        """
        Initializes the prompt window and displays the selected directory.

        Args:
            master (Tk): The tkinter root window.
        """

        self.master = master
        self.master.title('WFTS')
        x, y = 300, 200
        self.master.geometry(f"{x}x{y}")
        self.opener_text = "Welcome to the WFTS"
        self.font, self.size = 'Arial', 12
        
    def create_widgets(self, label=True):
        """
        Create various widgets inside the tkinter interface.
        """
        Label(self.master, text=self.opener_text, font=(self.font, self.size)).pack(anchor='n')
        self.Welcome_frame = Frame(self.master)
        self.Welcome_frame.pack(fill=BOTH, expand=True)
        
        self.send_btn = Button(self.Welcome_frame, text='Send', height=2, width=10, command=self.send_window)
        self.send_btn.grid(row=0, column=0, padx=30, pady=40)
        
        self.receive_btn = Button(self.Welcome_frame, text='Receive', height=2, width=10)
        self.receive_btn.grid(row=0, column=1, padx=30, pady=40)
        
    def send_window(self):
        self.master.destroy()

    def main(self):
        """
        Starts the application by running the organization logic and entering the main event loop.
        """

        self.create_widgets()
        self.master.mainloop()
  
b = Tk()      
P = PROMPT(b)
P.main()