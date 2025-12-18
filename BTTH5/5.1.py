print('Ngo Xuan Lam')
print('245751030110040')

import turtle
def draw_square():
    screen = turtle.Screen()
    screen.setup(width=400, height=400)
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("blue")
    pen.speed(1)
    for _ in range(4):
        pen.forward(100) 
        pen.right(90)  
    screen.mainloop()
if __name__ == "__main__":
    draw_square()
