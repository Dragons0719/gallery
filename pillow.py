from json import load
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
import random as r

def citypage():
    def choosepic():
        loadpic = Image.open(r.choice(images))
        render3 = ImageTk.PhotoImage(loadpic)
        resize3 = loadpic.resize((1000, 1000), Image.Resampling.LANCZOS)
        render3 = ImageTk.PhotoImage(resize3)
        img3 = Label(top1, image=render3)
        img3.photo = render3
        img3.place(x=15, y=30)
    top1 = Toplevel()
    top1.attributes("-fullscreen", True)
    top1.config(bg='#fd5e53')
    top1.title('Cities Slideshow')
    images = ['Photos\\Chicago.png', 'Photos\\nyc.png', 'Photos\\Miami.png', 'Photos\\LA.png']
    loadpic4 = Image.open('Photos\\LA.png')
    render6 = ImageTk.PhotoImage(loadpic4)
    resize6 = loadpic4.resize((1000, 1000), Image.Resampling.LANCZOS)
    render6 = ImageTk.PhotoImage(resize6)
    img6 = Label(top1, image=render6)
    img6.photo = render6
    img6.place(x=15, y=30)
    nextpic = Button(top1, text='Next Picture', font=('Times', 30), bg='grey', fg='white', command=choosepic).place(x=1350, y=200)
    closeprgm = Button(top1, text='Go Back To Home', font=('Times', 30), bg='grey', fg='white', command=top1.withdraw).place(x=1300, y=400)

def yepage():
    def chooseye():
        loadpic2 = Image.open(r.choice(images2))
        render4 = ImageTk.PhotoImage(loadpic2)
        resize4 = loadpic2.resize((1000, 1000), Image.Resampling.LANCZOS)
        render4 = ImageTk.PhotoImage(resize4)
        img4 = Label(top2, image=render4)
        img4.photo = render4
        img4.place(x=15, y=30)
    top2 = Toplevel()
    top2.attributes("-fullscreen", True)
    top2.config(bg='#fd5e53')
    top2.title('Cities Slideshow')
    images2 = ['Photos\\kanye1.png', 'Photos\\quote.png', 'Photos\\friends.png', 'Photos\\quote2.png']
    loadpic3 = Image.open(r.choice(images2))
    render5 = ImageTk.PhotoImage(loadpic3)
    resize5 = loadpic3.resize((1000, 1000), Image.Resampling.LANCZOS)
    render5 = ImageTk.PhotoImage(resize5)
    img5 = Label(top2, image=render5)
    img5.photo = render5
    img5.place(x=15, y=30)
    nextpic1 = Button(top2, text='Next Picture', font=('Times', 30), bg='grey', fg='white', command=chooseye).place(x=1350, y=200)
    closeprgm = Button(top2, text='Go Back To Home', font=('Times', 30), command=top2.withdraw, bg='grey', fg='white').place(x=1300, y=400)


root = Tk()
root.attributes("-fullscreen", True)
root.config(bg='#ADD8E6')
root.title('Tkinter Image')
menu = Menu(root)
file = Menu(menu, tearoff=1)
file.add_command(label='Go to Cities Page', command=citypage)
file.add_command(label='Go to Kanye Page', command=yepage)
file.add_command(label='Close Program', command=root.destroy)
menu.add_cascade(label='Open Different Pages', menu=file)
root.config(menu=menu)
welcome = Label(text= 'Welcome to your photo gallery!\nPress the drop down menu to choose your gallery!', font=('Times', 50, BOLD), bg='#ADD8E6'). place(x=230, y=15)
loadpic3 = Image.open('Photos\\photo-1578985824626-945a6f546304.png')
render5 = ImageTk.PhotoImage(loadpic3)
img5 = Label(root, image=render5).place(x=450, y=300)
root.mainloop()