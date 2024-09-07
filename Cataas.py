from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title('Cats!')
window.geometry('600x480')

label1 = Label()
label1.pack()

url = "https://cataas.com/cat"
img = img_load(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
