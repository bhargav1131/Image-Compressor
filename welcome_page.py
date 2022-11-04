from tkinter import *
master = Tk()
master.geometry("365x800")
master.resizable(False, False)
master.title("WELCOME")

img = PhotoImage(file="/home/bhargav/My_projects/Image_compressor/images/background.png")
label = Label(image=img)
label.image = img
label.pack()

def nextPage():
    master.destroy()
    import main

# continue button
continue_img = PhotoImage(file="/home/bhargav/My_projects/Image_compressor/images/Rectangle 1.png")
continue1 = Button(master, image=continue_img,bd=0, command=nextPage, bg="white")
continue1.place(x=150, y=720)

master.mainloop()