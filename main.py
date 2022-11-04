"""
Dated: 15/11/2021
Aumthor: Bhargav Pratim Sharma
"""

"""
Dated: 15/11/2021
Aumthor: Bhargav Pratim Sharma
"""


from pickletools import optimize
from tkinter import *
import PIL
from PIL import Image
from tkinter.filedialog import  *
master = Tk()
master.geometry("640x370")
master.resizable(False, False)
master.title("Thad Image Compressor")
master.config(bg="black")
qual = IntVar()
qual.set(0)

Label(text="\n\n\nDefine the quality in number.\nHigh value low compression, low value high compression: ",
      font=("arial", 12, "bold"), bg="black", fg="white").pack()
Entry(master, textvariable=qual, bd=0, width=25, border=1).place(x=195, y=200)


def compress():

    file_path = askopenfilename()
    Image = PIL.Image.open(file_path)
    height, width = Image.size
    Img = Image.resize((height, width), PIL.Image.Resampling.LANCZOS)
    save_path = asksaveasfilename()

    # qual = int(input("Define the quality in size. High value hlow compression, low value high compression: "))
    Img.save(f"{save_path}" + ".jpg", optimize=True, quality=qual.get())


Button(master, text="COMPRESS", command=compress,
       bd=0, bg="#EFF2F0"). place(x=260, y=250)

master.mainloop()
