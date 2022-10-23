"""
Dated: 15/11/2021
Aumthor: Bhargav Pratim Sharma
"""

from pickletools import optimize
from tkinter import *
import PIL
from PIL import Image
from tkinter.filedialog import *

master = Tk()
master.geometry("370x700")
master.resizable(False, False)
master.title("Thad Image Compressor")

Label(text="Hemlo").pack()

file_path = askopenfilename()

Image = PIL.Image.open(file_path)
height, width = Image.size
Img = Image.resize((height,width), PIL.Image.Resampling.LANCZOS)
save_path = asksaveasfilename()

qual = int(input("Define the quality in size. High value hlow compression, low value high compression: "))
Img.save(f"{save_path}" + ".jpg", optimize=True, quality=qual)

