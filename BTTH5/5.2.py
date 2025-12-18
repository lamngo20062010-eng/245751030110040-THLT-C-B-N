print('Ngo Xuan Lam')
print('245751030110040')
import turtle
def draw_circle():
    screen = turtle.Screen()
    screen.setup(width=400, height=400)
    pen = turtle.Turtle()
    pen.color("red")
    pen.speed(3)
    pen.circle(50)
    screen.mainloop()
if __name__ == "__main__":
    draw_circle()
