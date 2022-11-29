# Rangoli Studio, version = Alpha 42
# By Section-F, CSE-MA
# Credits: Prateek Panwar, Shashank Shinde, Dhairya Jain, Pratham Rathore, Rishab Dosi, Harsh Mishra, Saad Qureshi, Samarth Dubey
# For new starters: Check ==Variables== and ==Shape Functions==
#                   Check Circle() in ==Shape Functions== 
#                   and read comments.

from tkinter import *
from tkinter import simpledialog, filedialog, colorchooser
from tktooltip import ToolTip
from PIL import Image, ImageGrab
from turtle import Turtle, Screen
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
fill_color, line_color, canFill = 'blue', 'white', True  # Default Color
radius, distance, sharpness, num_of, size = float, float, float, int, int  #SizeDialog() & Functions
psize = int #Pen Size

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
    trtl.pencolor('white')

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

def Arc():
    #1. User point turtle and clicks button
    #2. User then drags turtle to another location
    #3. After leaving left click, SizeDialog is called
    #Call after finishing drag
    #By Saad
    SizeDialog('arc')
    SetColor()
    trtl.pensize(psize)
    trtl.circle(radius,num_of)
    trtl.pensize(1)

def Polygon():
    global radius, size
    SizeDialog('polygon')
    SetColor()
    trtl.pensize(psize)
    radius = -size
    CenterTurtle()
    for _ in range(num_of):
        trtl.forward(size)
        trtl.right(360 / num_of)
    trtl.pensize(1)
    trtl.end_fill()
    trtl.pencolor('white')

def Flower():
    SizeDialog('flower')
    SetColor()
    trtl.penup()
    GOTO(0,radius)
    trtl.setheading(0)
    for i in range(1,num_of+1):
        trtl.setheading(360/num_of*i + (180/num_of))
        trtl.circle(radius*3.5/num_of,180)
    trtl.pendown()
    trtl.setheading(0)
    trtl.end_fill()
    trtl.pencolor('white')


def Leaf():
    SizeDialog('leaf')
    SetColor()
    for _ in range(num_of):
        LeafBranch()
        trtl.left(360 / num_of)
def LeafBranch():
    SetColor()
    heading = trtl.heading()
    trtl.circle(radius, 60)
    trtl.left(120)
    trtl.circle(radius, 60)
    trtl.setheading(heading)
    trtl.end_fill()
    trtl.pencolor('white')

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

def PaintBucket():
    global canFill, img14, b14
    if (canFill == True):
        canFill = False
        b14.configure(image=img14)
    else:
        canFill = True
        b14.configure(image=img14_ON)

def ColorSelection(color):
    global fill_color, line_color
    fill_color = color
    line_color = color
    trtl.color(fill_color)
    trtl.pencolor(line_color)

def ColorPallete():
    global fill_color, line_color
    color_code = colorchooser.askcolor(title ="Choose color")
    print(color_code)
    fill_color = color_code[1]
    line_color = color_code[1]
    trtl.color(fill_color)
    trtl.pencolor(line_color)


def FileSystem(fs: int):
    print('FileSystem', fs)
    filename = 'image'
    #New File
    if (fs == 0):
        trtl.clear()
        trtl.setheading(0)
        trtl.penup()
        trtl.goto(0,0)
        trtl.pendown()
    #Open File
    elif (fs == 1):
        print("Open")
        file_path = filedialog.askopenfilename(initialfile = 'Drawing.png', title="Open File", filetypes=[('PNG File','*.png')])
    #Save File
    elif (fs == 2):
        #Save EPS File
        file_path = filedialog.asksaveasfilename(initialfile = 'Drawing', title="Save File", filetypes=[('Inksscape, Illustrator EPS', '*.eps'),('PNG File','*.png')])
        canvasT.postscript(file=file_path+'.eps', colormode='color')
        
        #Save PNG File
        trtl.hideturtle()
        x0 = canvasT.winfo_rootx()
        y0 = canvasT.winfo_rooty()
        x1 = x0 + canvasT.winfo_width()
        y1 = y0 + canvasT.winfo_height()
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(file_path+'.png')
        trtl.showturtle()

showGrid = False
def grid():
    #Canvas size = 1130x630
    global showGrid
    print('Grid')
    grid_value = 10
    w = canvasT.winfo_width() # Get current width of canvas
    h = canvasT.winfo_height() # Get current height of canvas
    
    if showGrid==True:
        canvasT.delete('grid_line') # Will only remove the grid_line
        showGrid = False
    else:

    # canvasT.create_line(-w,25,w,25, tag='grid_line')
    # Creates all vertical lines at intevals of 100
        for i in range(-w, w, grid_value):
            if i%100==0:
                canvasT.create_line(i, -h, i, h, tag='grid_line',fill='#8c8c8c')

    # Creates all horizontal lines at intevals of 100
        for i in range(-h, h, grid_value):
            if i%100==0:
                canvasT.create_line(-w, i, w, i, tag='grid_line',fill='#8c8c8c')
        showGrid=True


# window.mainloop()

def Preset():
    print("Show Preset")

def About():
    aboutWin = Toplevel(window)
    aboutWin.title("About Rangoli Studio")
    aboutWin.geometry("960x540")
    aboutWin.configure(bg="#171717")
    aboutWin.wm_transient(window)
    #Title
    Label(aboutWin,text ="Rangoli Studio",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 18").pack()
    #Desc
    Label(aboutWin,text ="Rangoli Studio gives you power to create beautiful rangoli designs in your desktop easily.",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 12").pack()
    #Controls
    Label(aboutWin,text ="Controls",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 16").pack()
    Label(aboutWin,text ="Mouse Left Click + Drag  -  Move turtle on screen \nMouse Right Click  -  Rotate turtle 90 degrees clockwise \nCtrl+C  -  Clear screen",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 12").pack()
    #Devs
    Label(aboutWin,text ="Designed By",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 12").pack()
    Label(aboutWin,text ="SVVV B.TECH CSE-MA, Section F",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 12").pack()
    Label(aboutWin,text ="Prateek Panwar, Pratham Rathore, Tanaygeet, DJ, Saad Ahmed Qureshi",
        fg="#ffffff",
        bg="#171717",
        font="Calibri, 12").pack()


# == Helper Functions ==
def SetColor():
    global canFill
    trtl.fillcolor(fill_color)
    trtl.color(line_color)
    if (canFill == True):
        trtl.begin_fill()

def CenterTurtle():
    trtl.setheading(0)  # Rotation to 0
    GOTO(0, -radius)  # To goto given position relatively

## Turtle functions
def clickRight(x,y):
    h = trtl.heading()
    if(h % 90 != 0):
        trtl.setheading(0)
    trtl.setheading(trtl.heading()-90)

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
trtl.onclick(clickRight,btn=2)
trtl.onclick(clickRight,btn=3)

#Dialogs & Helpers
# Dialog to ask for size, curvature, etc
radius_sv, num_of_sv, size_sv, distance_sv = DoubleVar(
), DoubleVar(), DoubleVar(), DoubleVar()
psize_sv = IntVar()

def SizeDialog(shape):
    global radius, num_of, size, distance
    shape = shape.lower()
    if shape == "circle":
        radius_sv.set(simpledialog.askfloat(
            "Add "+shape, "Enter radius", parent=window))
    if shape == "polygon":
        size_sv.set(simpledialog.askinteger(
            "Add "+shape, "Enter size of side", parent=window))
        num_of_sv.set(simpledialog.askinteger(
            "Add "+shape, "Number of sides", parent=window))
    if shape == "leaf":
        radius_sv.set(simpledialog.askfloat(
            "Add "+shape, "Enter radius", parent=window))
        num_of_sv.set(simpledialog.askinteger(
            "Add "+shape, "Number of leaves", parent=window))    
    if shape == "dotpattern":
        radius_sv.set(simpledialog.askfloat(
            "Add "+shape, "Enter radius", parent=window))
        size_sv.set(simpledialog.askinteger(
            "Add "+shape, "Size of dots", parent=window))
        distance_sv.set(simpledialog.askfloat(
            "Add "+shape, "Distance of dots", parent=window))
    if shape == "arc":
        radius_sv.set(simpledialog.askfloat(
            "Add "+shape, "Enter radius", parent=window))
        num_of_sv.set(simpledialog.askinteger(
            "Add "+shape, "Enter the Degree", parent=window))
    if shape == "flower":
        radius_sv.set(simpledialog.askfloat(
            "Add "+shape, "Enter radius", parent=window))
        num_of_sv.set(simpledialog.askinteger(
            "Add "+shape, "Number of petals", parent=window))
    # Converting to int
    radius = float(radius_sv.get())
    num_of = int(num_of_sv.get())
    size = int(size_sv.get())
    distance = float(distance_sv.get())

def ConvertSliderVal():
    global psize
    psize = int(psize_sv.get())
# Function initialization
# canvas.bind('<Button-1>', DotPattern)   #Removed

# Buttons
# Button's icon
img0 = PhotoImage(file=f"./images/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ColorPallete(),  # This will call function for given button
    relief="flat",
    activebackground="#000000",
    bg="#171717")

b0.place(
    # Button's location on screen
    x=21, y=660,
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
    x=65, y=610,
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
    x=21, y=610,
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
    x=65, y=565,
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
    x=21, y=565,
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
    x=65, y=520,
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
    x=21, y=520,
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
    x=65, y=475,
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
    x=21, y=475,
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
    x=65, y=430,
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
    x=21, y=430,
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
    x=22, y=320,
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
    x=22, y=275,
    width=82,
    height=38)
ToolTip(symmetry_slider, msg="Symmetrical divisions")

pensize_slider = Scale(
    window,
    from_=1,
    to=36,
    orient='horizontal',
    fg="#ffffff",
    bg="#171717",
    troughcolor="#000000",
    highlightthickness=0,
    variable = psize_sv,
    command=lambda x=None: ConvertSliderVal())
pensize_slider.place(
    x=22, y=365,
    width=82,
    height=38)
ToolTip(pensize_slider, msg="Line Weight")

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
    command=lambda: Leaf(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b13.place(
    x=22, y=241,
    width=37,
    height=37)
ToolTip(b13, msg="Leaf")

img14 = PhotoImage(file=f"./images/img14.png")
img14_ON = PhotoImage(file=f"./images/img14_ON.png")
b14 = Button(
    image=img14_ON,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: PaintBucket(),
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
    command=lambda: Flower(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b15.place(
    x=22, y=197,
    width=37,
    height=37)
ToolTip(b15, msg="Make Flower pattern")

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
    command=lambda: Arc(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b18.place(
    x=66, y=109,
    width=37,
    height=37)
ToolTip(b18, msg="Make an Arc")

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
    x=1220, y=14,
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

img25 = PhotoImage(file=f"./images/img25.png")
b25 = Button(
    image=img25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Preset(),
    relief="flat",
    activebackground="#000000",
    bg="#171717")
b25.place(
    x=1130, y=14,
    width=38,
    height=38)
ToolTip(b25, msg="Presets")

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
