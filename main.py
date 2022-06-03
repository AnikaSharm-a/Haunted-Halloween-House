# Imports
from tkinter import *
from random import randint

# Screen setup
tk = Tk()
s = Canvas(tk, width = 450, height = 500, background = "white")
s.pack()


# Background colours
bg_colours = ["#7a57c2","#835fd1","#9773e3","#9671e7","#b392f8","#be98ff","#bd99fe"]

# Background coordinates
xc1 = -105
yc1 = -105
xc2 = 600
yc2 = 600

# Background
for i in range(7):
  s.create_oval(xc1,yc1, xc2,yc2, fill = bg_colours[i], outline = '')

  xc1 += 25
  yc1 += 25
  xc2 -= 35
  yc2 -= 35


# Moon
s.create_oval(100,75, 375,350, fill = "gold", outline = "orange", width = 2)


# Ground
s.create_polygon(-25,525, 0,450, 50,425, 75,400, 100,375, 150,350, 225,350, 325,350, 450,375, 375,400, 350,425,350, 450, 375,475, 400,525,smooth = True, fill = "grey8")


# Hanging roots
xl = 375
yl1 = 375

for line in range(25):
  size = randint(25,100)
  
  s.create_line(xl,yl1,xl,yl1+size, fill = "grey8")
  xl += 2



# Cross 1 (bottom left)
s.create_line(25,400, 45,430, fill = "grey8", width = 7)
s.create_line(15,420, 50,400, fill = "grey8", width = 7)


# Cross 2 (above previous)
s.create_line(65,350, 100,385, fill = "grey8", width = 8)
s.create_line(65,370, 90,345, fill = "grey8", width = 8)


# Steps leading up to house (bottom to top)
s.create_rectangle(100,475,200,490, fill = "#9773e3")

s.create_line(125,465, 200,455, fill = "#9773e3", width = 10)

s.create_line(150,425, 225,450, fill = "#9773e3", width = 10)

s.create_rectangle(175,410, 250,425, fill = "#9773e3")

s.create_line(200,400, 275,390, fill = "#9773e3", width = 10)

s.create_line(185,385, 250,375, fill = "#9773e3", width = 10)

s.create_rectangle(200,360, 275,370, fill = "#9773e3")

s.create_rectangle(215,350, 260,355, fill = "#9773e3")



# PUMPKIN

# Body
s.create_oval(275,450, 325,500, fill = "chocolate3", outline = "")

# Stem
s.create_line(300,440, 300,450, fill = "chocolate4", width = 5)

# Mouth
s.create_line(285,475, 290,485, 300,480, 310,485,315,475, fill = "yellow", width = 3)

# Left eye
s.create_polygon(290,460, 280,465, 295,470, fill = "yellow")

# Right eye
s.create_polygon(305,470, 320,465, 315,460, fill = "yellow")



# TREE

# Trunk
s.create_polygon(350,375, 375,325, 385,300, 415,250, 380,225, 425,225, 435,250, 425,275, 415,300, 415,325, 425,350, 425,387, fill = "grey8", smooth = True)

# BRANCHES

# Bottom left area
s.create_line(400,230, 375,225, 360,200, 347,200, fill = "grey8", width = 10)

s.create_line(350,200, 325,175, 320,200, 313,205, fill = "grey8", width = 10)

s.create_line(350,200, 335,150, 325,125, fill = "grey8", width = 5)

s.create_line(350,200, 350,175,355,150, 370,125, 375,100, fill = "grey8", width = 7)


# Middle area

# Top left
s.create_line(400,225, 405,175, 425,125, 455,50, fill = "grey8", width = 10)

s.create_line(425,125, 375,75, 325,70, 315,80, 300,75, fill = "grey8", width = 8)

s.create_line(325,75, 325,50, 315,45, fill = "grey8", width = 5)

s.create_line(375,75, 365,50, 350,45, 330,25, fill = "grey8", width = 6)

s.create_line(400,100, 405,75, 400,50, 395,50, 400,25, fill = "grey8", width = 7)

# Top
s.create_line(440,85, 435,40, 415,35, fill = "grey8", width = 6)

# Bottom 
s.create_line(402,175, 390,160, 375,175, fill = "grey8", width = 6)

# Right
s.create_line(400,170, 425,168, 430,150, 450,125, fill = "grey8", width = 5)


# Bottom right area
s.create_line(415,230, 425,200, 450,175, fill = "grey8", width = 7)

s.create_line(425,200, 425,175, fill = "grey8", width = 6)




# HOUSE

# Side pillar left
s.create_line(175,355, 150,270, fill = "grey8", width = 8)

# Side pillar right
s.create_line(300,355, 325,270, fill = "grey8", width = 8)

# Main base of house
s.create_polygon(190,350, 165,275, 125,275, 150,225, 160,225, 160,150, 175,125,275,125, 310,150, 300,150, 300,225, 310,225, 340,275, 310,275, 285,350, fill = "grey8")

# Door
s.create_rectangle(225,300, 250,345, fill = '', outline = "#aeaad1", width = 4)

s.create_oval(240,320,245,325, fill = "#aeaad1")


# First floor windows

# Left
s.create_polygon(195,340, 190,325, 200,300, 210,325, 205,340, fill = "yellow")

# Lines
s.create_line(200,300, 200,350, width = 2, fill = "grey8")

s.create_line(190,320, 210,320, width = 2, fill = "grey8")

s.create_line(190,330, 210,330, width = 2, fill = "grey8")


# Above door
# Window
s.create_oval(225,260, 250,285, fill = "yellow")

# Lines
start = -5
for line in range(4):
  s.create_arc(225,260, 250,285, start = start, extent = 10, fill = "black")
  start += 90


# Right
s.create_polygon(270,340, 265,325, 275,300, 285,325, 280,340, fill = "yellow")

# Lines
s.create_line(275,300, 275,350, width = 2, fill = "grey8")

s.create_line(265,320, 285,320, width = 2, fill = "grey8")

s.create_line(265,330, 285,330, width = 2, fill = "grey8")


# Roofs for first floor

# Left
s.create_polygon(200,275, 125,275, 150,225, 200,225,  fill = "", outline = "#7b78a3", width = 5)

# Right
s.create_polygon(340,275, 310,225, 275,225, 275,275, fill = "", outline = "#7b78a3", width = 5)

# Middle
s.create_polygon(180,250, 205,200, 265,200, 290,250, fill = "grey8", outline = "#7b78a3", width = 5)


# Top floor roofs

# Left
s.create_polygon(160,150, 175,125, 200,125, 200,150, fill = "", outline = "#7b78a3", width = 5)

# Right
s.create_polygon(275,125, 310,150, 260,150, 260,125, fill = "", outline = "#7b78a3", width = 5)

# Middle
s.create_polygon(190,135, 210,100, 250,100, 270,135, fill = "grey8", outline = "#7b78a3", width = 5)


# Top floor windows

# Middle
s.create_polygon(220,185, 240,185, 245,170, 230,150, 215,170, fill = "yellow")

# Lines
s.create_line(230,150, 230,185, width = 2)

s.create_line(245,160, 215,165, fill = "grey8", width = 2)

s.create_line(215,170, 247,175, fill = "grey8", width = 2)

s.create_line(215,180, 247,180, fill = "grey8", width = 2)


# Left
s.create_oval(175,165, 200,190, fill = "yellow")

# Lines
start = -5
for line in range(4):
  s.create_arc(175,165, 200,190, start = start, extent = 10, fill = "black")
  start += 90


# Right  
s.create_oval(265,165, 290,190, fill = "yellow")

# Lines
start = -5
for line in range(4):
  s.create_arc(265,165, 290,190, start = start, extent = 10, fill = "black")
  start += 90


# GHOST

# body
s.create_polygon(175,125, 175,100, 165,115, 150,100,150,115, 125,125, 150,130, 165,140, fill = "white", smooth = True)

# left eye
s.create_oval(150,120,154,124, fill = "black")

# right eye
s.create_oval(160,115,164,119, fill = "black")



# Fences

# On top of house
xf = 220
yf = 90

for fence in range(5):
  s.create_line(xf,yf, xf,yf+10, width = 2)
  xf += 5

s.create_line(215,94, 245,94, width = 2)


# Right side of house
xf = 325
yf = 325

for fence in range(5):
  s.create_line(xf,yf, xf-7,yf+28, width = 2, fill = "grey8")
  xf += 5
  yf += 2

s.create_line(320,335, 350,345, width = 2)


# Left side of house
xf = 140
yf = 328

for fence in range(5):
  s.create_line(xf,yf, xf+7,yf+28, width = 2, fill = "grey8")
  xf -= 5
  yf += 5

s.create_line(147,333, 117,360, width = 2)


# TITLE
s.create_text(80,35, text = "Spooky night", font = "Times 10 italic", fill = "white")