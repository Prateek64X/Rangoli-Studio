# Rangoli Studio, version = Alpha 28
# By Section-F, CSE-MA
# Credits: Prateek Panwar, Shashank Shinde, Dhairya Jain, Pratham Rathore, Rishab Dosi, Harsh Mishra, Saad Quereshi, Samarth Dubey
# For new starters: Check ==Variables== and ==Shape Functions==
#                   Check Circle() in ==Shape Functions== 
#                   and read comments.

from tkinter import *
from tkinter import simpledialog
from tktooltip import ToolTip
import turtle

#Window and Canvas
window = Tk()
window.geometry("1280x720")
window.title("Rangoli Studio")
window.configure(bg="#222222")
canvas = Canvas(
    window,
    bg="#222222",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"./images/background.png")
background = canvas.create_image(
    640.0, 359.0,
    image=background_img)

# Turtle config
canvasT = Canvas(
    window,
    bg="#222222",
    height=630,
    width=1130,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvasT.place(relx=0.544, rely=0.540, anchor=CENTER)
screen = turtle.TurtleScreen(canvasT)
trtl = turtle.RawTurtle(canvasT)
# trtl.listen()
trtl.speed(-1)
trtl.screen.bgcolor("#171717")
trtl.color("white")

# == Variables ==
click_num, x2, y2 = 0, 0, 0  # Line: Mouseclick
toggleSymmetry = False  # Symmetry On/OFF
symmetryVal = 2  # Symmetry value 2 to 20
fill_color, line_color = 'blue', 'white'  # Default Color
radius, num_of, distance, size = float, float, float, float  #SizeDialog() & Functions

# == Drawing Functions ==
# Useful variables: radius, num_of, distance, size
# Useful functions: SizeDialog('enter_shape_name'), SetColor(), CenterTurtle() 
# Use trtl.x instead of turtle.x
def Circle():
    # SizeDialog takes input from user. ex: SizeDialog('enter_your_shape')
    SizeDialog('circle')
    SetColor()  # Sets chosen color
    CenterTurtle()  # Centers turtle before drawing circle
    trtl.circle(radius)  # Draw circle for given radius
    trtl.end_fill()  # Fill color

def DotPattern():
    global distance
    SizeDialog('dotpattern')
    SetColor()
    CenterTurtle()
    if (distance <= 0.0):
        distance = 5.0
    trtl.penup()
    circumference = 2 * 3.14 * radius
    dot_extent = 360 * size*distance / circumference  # diameter to angle
    extent = 0
    while extent < 360:
        trtl.dot(size)
        trtl.circle(radius, extent=dot_extent)

        extent += dot_extent

def CurveLine():
    print('CurveLine')
    SetColor()
    # Code


def Polygon():
    SizeDialog('polygon')
    print('Polygon')
    SetColor()

def Arc():
    print('Arc')
    SetColor()
    # Code


def Petal():
    SizeDialog('petal')
    print('Petal')
    SetColor()
    # Code


def text():
    print('Text')
    # Code


def Symmetry():
    global toggleSymmetry

    if (toggleSymmetry != True):
        toggleSymmetry = True
    else:
        toggleSymmetry = False
    # Code


def ColorSelection(color):
    global fill_color
    global line_color
    fill_color = color
    line_color = color

def ColorPallete():
    print('ColorPallete')
    # Code


def FileSystem(fs: int):
    print('FileSystem', fs)
    # Code


def grid():
    print('Grid')
    # Code

def About():
    print('About')
    # Code

# == Helper Functions ==
def SetColor():
    trtl.fillcolor(fill_color)
    trtl.color(line_color)
    trtl.begin_fill()

def CenterTurtle():
    trtl.setheading(0)  # Rotation to 0
    GOTO(0, -radius)  # To goto given position relatively

## Turtle functions
def clickRight():
    trtl.clear()

## To move turtle with mouse drag
def Drag_Turtle(x, y):
    trtl.ondrag(None)
    trtl.setheading(trtl.towards(x, y))
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()
    trtl.ondrag(Drag_Turtle)

def GOTO(x, y):
    trtl.penup()
    trtl.goto(trtl.pos() + (x, y))
    trtl.pendown()

trtl.ondrag(Drag_Turtle)

#Dialogs & Helpers
# Dialog to ask for size, curvature, etc
radius_sv, num_of_sv, size_sv, distance_sv = DoubleVar(
), DoubleVar(), DoubleVar(), DoubleVar()


def SizeDialog(shape):
    global radius, num_of, size, distance
    shape = shape.lower()
    if shape == "circle":
        radius_sv.set(simpledialog.askstring(
            "Add "+shape, "Enter radius", parent=window))
    if shape == "polygon":
        size_sv.set(simpledialog.askstring(
            "Add "+shape, "Enter size of side", parent=window))
        num_of_sv.set(simpledialog.askstring(
            "Add "+shape, "Number of sides", parent=window))
    if shape == "petal":
        radius_sv.set(simpledialog.askstring(
            "Add "+shape, "Enter radius", parent=window))
        num_of_sv.set(simpledialog.askstring(
            "Add "+shape, "Number of petals", parent=window))
    if shape == "dotpattern":
        radius_sv.set(simpledialog.askstring(
            "Add "+shape, "Enter radius", parent=window))
        size_sv.set(simpledialog.askstring(
            "Add "+shape, "Size of dots", parent=window))
        distance_sv.set(simpledialog.askstring(
            "Add "+shape, "Distance of dots", parent=window))
    # Converting to int
    radius = float(radius_sv.get())
    num_of = float(num_of_sv.get())
    size = float(size_sv.get())
    distance = float(distance_sv.get())


def btn_clicked():
    print("Button Clicked")


# Function initialization
# canvas.bind('<Button-1>', DotPattern)   #Removed

# Buttons
# Button's icon
img0 = PhotoImage(file=f"./images/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection(),  # This will call function for given button
    relief="flat",
    activebackground="#000000",
    bg="#171717")

b0.place(
    # Button's location on screen
    x=21, y=625,
    width=82,
    height=38)
ToolTip(b0, msg="Color Pallete")

img1 = PhotoImage(file=f"./images/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#FFB950'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b1.place(
    x=65, y=571,
    width=38,
    height=38)

img2 = PhotoImage(file=f"./images/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#ab5539'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b2.place(
    x=21, y=571,
    width=38,
    height=38)

img3 = PhotoImage(file=f"./images/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#0d0c0d'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b3.place(
    x=65, y=527,
    width=38,
    height=38)

img4 = PhotoImage(file=f"./images/img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#fefffe'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b4.place(
    x=21, y=527,
    width=38,
    height=38)

img5 = PhotoImage(file=f"./images/img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#7929fb'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b5.place(
    x=65, y=483,
    width=38,
    height=38)

img6 = PhotoImage(file=f"./images/img6.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#27a2ff'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b6.place(
    x=21, y=483,
    width=38,
    height=38)

img7 = PhotoImage(file=f"./images/img7.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#71f897'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b7.place(
    x=65, y=439,
    width=38,
    height=37)
ToolTip(b7, msg="Pattern")

img8 = PhotoImage(file=f"./images/img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#ec8e01'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b8.place(
    x=21, y=439,
    width=38,
    height=37)
ToolTip(b8, msg="Pattern")

img9 = PhotoImage(file=f"./images/img9.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#da0539'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b9.place(
    x=65, y=394,
    width=38,
    height=38)

img10 = PhotoImage(file=f"./images/img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorSelection('#f55f9d'),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b10.place(
    x=21, y=394,
    width=38,
    height=38)

img11 = PhotoImage(file=f"./images/img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Symmetry(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b11.place(
    x=22, y=285,
    width=82,
    height=37)
ToolTip(b11, msg="Symmetry ON/OFF")

symmetry_slider = Scale(
    window,
    from_=2,
    to=20,
    orient='horizontal',
    fg="#ffffff",
    bg="#171717",
    troughcolor="#000000",
    highlightthickness=0,
    variable=symmetryVal)
symmetry_slider.place(
    x=22, y=325,
    width=82,
    height=46)
ToolTip(symmetry_slider, msg="Symmetrical divisions")

img12 = PhotoImage(file=f"./images/img12.png")
b12 = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: text(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b12.place(
    x=66, y=241,
    width=37,
    height=37)
ToolTip(b12, msg="Text")

img13 = PhotoImage(file=f"./images/img13.png")
b13 = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Petal(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b13.place(
    x=22, y=241,
    width=37,
    height=37)
ToolTip(b13, msg="Petal")

img14 = PhotoImage(file=f"./images/img14.png")
b14 = Button(
    image=img14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorPallete(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b14.place(
    x=66, y=197,
    width=37,
    height=37)
ToolTip(b14, msg="Color")

img15 = PhotoImage(file=f"./images/img15.png")
b15 = Button(
    image=img15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Arc(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b15.place(
    x=22, y=197,
    width=37,
    height=37)
ToolTip(b15, msg="Arc")

img16 = PhotoImage(file=f"./images/img16.png")
b16 = Button(
    image=img16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Circle(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b16.place(
    x=66, y=153,
    width=37,
    height=37)
ToolTip(b16, msg="Circle")

img17 = PhotoImage(file=f"./images/img17.png")
b17 = Button(
    image=img17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Polygon(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b17.place(
    x=22, y=153,
    width=37,
    height=37)
ToolTip(b17, msg="Polygon")

img18 = PhotoImage(file=f"./images/img18.png")
b18 = Button(
    image=img18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: CurveLine(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b18.place(
    x=66, y=109,
    width=37,
    height=37)
ToolTip(b18, msg="Curve Line")

img19 = PhotoImage(file=f"./images/img19.png")
b19 = Button(
    image=img19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: DotPattern(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b19.place(
    x=22, y=109,
    width=37,
    height=37)
ToolTip(b19, msg="Pattern")

img20 = PhotoImage(file=f"./images/img20.png")
b20 = Button(
    image=img20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: About(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b20.place(
    x=1219, y=14,
    width=38,
    height=38)
ToolTip(b20, msg="About")

img21 = PhotoImage(file=f"./images/img21.png")
b21 = Button(
    image=img21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: grid(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b21.place(
    x=1175, y=14,
    width=38,
    height=38)
ToolTip(b21, msg="Grid Show/Hide")

img22 = PhotoImage(file=f"./images/img22.png")
b22 = Button(
    image=img22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: FileSystem(2),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b22.place(
    x=163, y=17,
    width=62,
    height=32)
ToolTip(b22, msg="Save")

img23 = PhotoImage(file=f"./images/img23.png")
b23 = Button(
    image=img23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: FileSystem(1),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b23.place(
    x=93, y=17,
    width=62,
    height=32)
ToolTip(b23, msg="Open")

img24 = PhotoImage(file=f"./images/img24.png")
b24 = Button(
    image=img24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: FileSystem(0),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b24.place(
    x=24, y=17,
    width=62,
    height=32)
ToolTip(b24, msg="New")

# Mainloop
window.mainloop()
