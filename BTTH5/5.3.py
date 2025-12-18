print('Ngo Xuan Lam')
print('245751030110040')
import turtle

def draw_combined_shape():
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    pen = turtle.Turtle()
    pen.speed(5)

    pen.color("blue")
    for _ in range(4):
        pen.forward(150)
        pen.right(90)
    pen.penup()     
    pen.goto(75, -50)
    pen.pendown()    
    pen.color("red")
    pen.circle(50) 
    pen.hideturtle() 
    screen.mainloop()

if __name__ == "__main__":
    draw_combined_shape()
