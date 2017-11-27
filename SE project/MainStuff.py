from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from pic_processing import *
from vid_processing import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Face detection")
        self.pack(fill=BOTH, expand=1)
        self.showImg()
        self.showTxt()
        selectPictureButton = Button(self, text = "Select Picture", command = self.pT)
        selectPictureButton.place(x=152, y=45)
        selectVideoCaptureButton = Button(self, text = "Capture Video", command = self.capVid)
        selectVideoCaptureButton.place(x=150, y=80)
        aboutButton = Button(self, text = "About", command = self.client_detail)
        aboutButton.place(x=170, y=115)
        quitButton = Button(self, text = "Quit", command=self.client_exit)
        quitButton.place(x=175, y=150)
        #quitButton.pack(side=right)
    def capVid(self):
        vidtransformation()
    def pT(self):
        pictransformation()
    def client_detail(self):
        def leavemini():
            popup.destroy()
        msg = """   This Program is the sole property of:
Muhammad Omer Affan
Sohail Asghar
Muhammad Sohail
Muhammad Abdullah
FGA(Face detection - Gender recognitoin - Age predictiion)
is an application designed and developed as a Software
Engineering project by the students of
Air University Multan Campus
with the intention of learning to use
Software Enginreeing principles and coding in
Python."""
        popup = Tk()
        popup.wm_title("About FGA!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill = 'x', pady=10)
        b1 = Button(popup, text="Okay", command = leavemini)
        b1.pack()
        popup.mainloop()
    def client_exit(self):
        exit()
    def showImg(self):
        load = Image.open('pic.gif')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image = render)
        img.image = render
        img.place(x=0, y=0)
    def showTxt(self):
        text = Label(self, text = "Welcome to FGA!")
        text.pack()
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
