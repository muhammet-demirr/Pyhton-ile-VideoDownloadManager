from tkinter import *
import pytube
from PIL import Image, ImageTk
from tkinter import filedialog


def get_location():
    download_path = filedialog.askdirectory()
    if download_path:
        my_location_entry.delete(0, END)
        my_location_entry.insert(0, download_path)

def download_video():
    my_link = my_link_entry.get()
    download_path = my_location_entry.get()
    if len(my_link) == 0 or len(download_path) == 0:
        status_label.config(text="Please enter all info!")
    else:
        try:
            pytube.YouTube(my_link).streams.get_highest_resolution().download(download_path)
            status_label.config(text="Download complete!")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")



my_window = Tk()
my_window.title("Youtube Downloader")
my_window.minsize(width=300,height=200)
my_window.configure(background="black")


my_icon = PhotoImage(file='yticon.png')
my_window.iconphoto(False, my_icon)


my_img = Image.open("ytphoto.png")
new_width = 200
new_height = 100
my_img = my_img.resize((new_width, new_height))
tk_img = ImageTk.PhotoImage(my_img)
label = Label(my_window, image=tk_img)
label.grid(row=0, column=0, columnspan=2)
label.config(border=0)

my_link_label = Label(text="Enter Your Url:")
my_link_label.grid(row=1, column=0, sticky="w")
my_link_label.config(background="black",foreground="red")

my_link_entry = Entry(width=30)
my_link_entry.grid(row=1, column=1)
my_link_entry.config(background="black",foreground="white",borderwidth=5,insertbackground="white")

my_location_label = Label(text="Select Download Location:")
my_location_label.grid(row=2, column=0, sticky="w")
my_location_label.config(background="black",foreground="red")

my_location_entry = Entry(width=30)
my_location_entry.grid(row=2, column=1)
my_location_entry.config(background="black",foreground="white",borderwidth=5,insertbackground="white")

my_button_icon = Image.open("buttonicon.jpg")
second_width = 20
second_height = 20
my_button_icon = my_button_icon.resize((second_width,second_height))
tk_icon = ImageTk.PhotoImage(my_button_icon)

my_location_button = Button(image=tk_icon, command=get_location)
my_location_button.grid(row=2, column=2)
my_location_button.config(border=0)

download_button = Button(text="Download",command=download_video)
download_button.grid(row=3, column=0, columnspan=2)
download_button.config(background="red",foreground="black")

status_label = Label(text="")
status_label.grid(row=4, column=0, columnspan=2)
status_label.config(background="black",foreground="red")

my_window.mainloop()
