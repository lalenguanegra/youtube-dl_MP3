import requests
import subprocess 
from subprocess import call
from tkinter import *
import webbrowser
from tkinter import messagebox
window = Tk()
root = Tk()
frame = Frame(root)
frame.pack()
def OpenGithub():
    url = 'https://github.com/lalenguanegra/youtube-dl_MP3'
    webbrowser.open_new(url)
window.title("Sadie Socio's")
lbl = Button(window, text="youtube-dl", command=OpenGithub, width=30, height=10, font=("Arial Bold", 30))
window.wm_iconbitmap('drip.ico')
def command():
    Toplevel(root)
root.title("")
canvas1 = Canvas(root, width = 150, height = 35)
canvas1.pack()
entry1 = Entry (root, justify='center') 
def Entry():
        messagebox.showwarning("Please Wait...","Downloading...")
        a = entry1.get()
        with open(('URL.txt'), 'w') as f: 
            f.write(a)
        call(['./python/python.exe', './youtube-dl/youtube_dl/__main__.py', '--ffmpeg-location', './ffmpeg/bin/ffmpeg.exe', '-f', 'mp4', '-a', './URL.txt'], shell=False)
canvas1.create_window(75, 25, width=337, window=entry1)



b1 = Button(root, text="MP4", command=Entry, height=1, width=8, font=("Arial Bold", 50))
root.wm_iconbitmap('drip.ico')
window.geometry("500x100+300+300")
b1.pack()
lbl.pack()
b1.config(bg="#6600cc")
lbl.config(bg="#b3003b")


root.resizable(width=False, height=False)
window.resizable(width=False, height=False)
window.mainloop()


