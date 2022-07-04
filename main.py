from setuptools import Command
import pytube
import tkinter as tk
from cProfile import label
app = tk.Tk()
app.title("Youtube Video Downloader")
app.geometry("600x600")

def downloadyt():
    url= box1.get()
    path="D:"
    pytube.YouTube(url).streams.get_highest_resolution().download(path)

app.iconbitmap("jonty_dp_G1h_icon.ico")
label1 =tk.Label(app, text = "Enter URL:",font = ("Arial", 15))
label1.place(x=40, y=60)
box1 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box1.place(x=180, y=50)
button1 = tk.Button(app , font=("Arial",15),bg ="Orange",text = "Download",command=downloadyt)  
button1.place(x=300 , y= 120 , width = 100)

app.mainloop()
