from tkinter import *
from pytube import YouTube

#gui display
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Simple YouTube Downloader")


#link space
link = StringVar()
Label(root, text = 'Paste the Link Below',font = 'arial 12 bold').place(x= 165 , y = 50)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 45, y = 90)

#download function
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download('/Users/Nishen/Videos')
    Label(root, text = 'DOWNLOAD COMPLETED').place(x= 200 , y = 220)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()

