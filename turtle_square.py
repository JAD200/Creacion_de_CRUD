import turtle


window = turtle.Screen()
tortuga = turtle.Turtle()

def make_a_square():
    for side in range(4):
        tortuga.fd(100)
        tortuga.right(90)

make_a_square()
window.mainloop()
