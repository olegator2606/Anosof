import tkinter
master = tkinter.Tk()
master.title('Веселый кирпич')
canvas = tkinter.Canvas(master, width=600, height=600, bg='black')
x = canvas.create_rectangle((270,0),(330,30), fill = "red")
def move_brick():
    canvas.move(x, 0, 3)
    y = canvas.coords(x)
    master.title(y)
    if y[3] < 600:
        master.after(30,move_brick )

#move_brick()

def key_down(event):
    z = event.keysym
    master.title(z)
    if z == 'Down':
        canvas.move(x,0,30)
    elif z == 'Up':
        canvas.move(x, 0, -30)
    elif z == 'Left':
        canvas.move(x, -30,0)
    elif z == 'Right':
        canvas.move(x, 30,0)
    if z == 'd':
        canvas.move(x,15,15)
    elif z == 'a':
        canvas.move(x, -15, -15)
    elif z == 't':
        canvas.move(x, -15,15)
    elif z == 'p':
        canvas.move(x, 15,-15)


master.bind("<Key>",key_down )
canvas.pack()
master.mainloop()