import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():

    options = ["Visoka rezoluciq", "Niska rezuluciq"]

    head_label = Label(root,
                       text = "Youtube Downloader",
                       padx = 15,
                       pady = 15,
                       font = "Arial 14",
                       bg = "green",
                       fg = "blue")

    head_label.grid (row = 1,
                     column = 1,
                     padx = 5,
                     pady = 10)

    link_label = Label(root,
                       text = "Link na videoto:",
                       bg = "salmon",
                       padx = 5,
                       pady = 5)

    link_label.grid (row = 2,
                     column = 0,
                     padx = 5,
                     pady = 5)

    root.linkText = Entry(root,
                          width = 35,
                          textvariable = video_link,
                          font = "Arial 14")
   
    root.linkText.grid (row = 2,
                        column = 1,
                        padx = 5,
                        pady = 5)

    destination_label = Label(root,
                              text = "Kude da se zapazi:",
                              bg = "salmon",
                              padx = 5,
                              pady = 5)

    destination_label.grid (row = 3,
                            column = 0,
                            padx = 5,
                            pady = 5)
   
    root.destinationText = Entry(root,
                                 width = 35,
                                 textvariable = download_Path,
                                 font = "Arial 14")

    root.destinationText.grid (row = 3,
                               column = 1,
                               padx = 5,
                               pady = 5)

    name_label = Label(root,
                       text = "Imeto na fila:",
                       bg = "salmon",
                       padx = 5,
                       pady= 5)

    name_label.grid (row = 4,
                     column = 0,
                     padx = 5,
                     pady = 5)

    root.nameLabel = Entry(root,
                           width = 35,
                           textvariable = download_name,
                           font = "Arial 14")

    root.nameLabel.grid (row = 4,
                         column = 1,
                         padx = 5,
                         pady= 5)
   
    quality_label = Label(root,
                          text = "Kachestvo na videoto:",
                          bg = "salmon",
                          padx = 5,
                          pady= 5)

    quality_label.grid (row = 5,
                        column = 0,
                        padx = 5,
                        pady = 5)
   
    root.qualityLabel = OptionMenu(root,
                                   quality,
                                   *options)
   
    root.qualityLabel.grid (row = 5,
                            column = 1,
                            padx = 5,
                            pady = 5)

    browse_button = Button(root,
                           text = "Papka",
                           command = Browse,
                           width = 10,
                           bg = "red",
                           relief = GROOVE)

    browse_button.grid (row = 3,
                        column = 2,
                        padx = 1,
                        pady = 1)

    download_button = Button(root,
                             text = "Iztegli",
                             command = Download,
                             bg = "red",
                             relief = GROOVE)

    download_button.grid (row = 6,
                          column = 1,
                          padx = 20,
                          pady = 20)

def Browse():
    download_Directory = filedialog.askdirectory(initialdir = "Path", title = "Save Video")
    download_Path.set(download_Directory)

def Download():
    Youtube_link = video_link.get()
    filename = download_name.get()
    video_quality = quality.get()
    download_folder = download_Path.get()
    get_Video = YouTube(Youtube_link)
    if video_quality == "High resolution":
        video_stream = get_Video.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download(download_folder, filename)
        messagebox.showinfo("Successfully downloaded and saved in " + download_folder)
    elif video_quality == "Low resolution":
        video_stream = get_Video.streams.filter(progressive = True, file_extension = 'mp4').first().download(download_folder, filename)
        messagebox.showinfo("Successfully downloaded and saved in " + download_folder)
    else:
        video_stream = get_Video.streams.filter(progressive = True, file_extension = 'mp4').first().download(download_folder, filename)
        messagebox.showinfo("Successfully downloaded and saved in " + download_folder)

root = tk.Tk()
root.geometry = ("600x300")
root.resizable(False, False)
root.title("Video Downloader")
root.config(bg = "green")
video_link = StringVar()
download_Path = StringVar()
download_name = StringVar()
quality = StringVar()
Widgets()
root.mainloop()