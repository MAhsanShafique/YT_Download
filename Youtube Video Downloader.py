from future.moves import tkinter
from pytube import YouTube

root = tk()
root.geometry('500*300')
root.resizeable(0,0)
root.title("Ahsan's YouTube Video Downloader")
Label(root,text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link That You Copied: ', font = 'arial 15 bold').place(x = 160 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Download', font = 'arail 15 bold' , bg = 'pale violet red', padx = 2, command = Downloader().place(x=180, y = 150))

root.mainloop()