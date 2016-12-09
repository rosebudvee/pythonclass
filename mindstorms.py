import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    susie = turtle.Turtle()
    susie.shape("turtle")
    susie.color("blue")
    susie.speed(4)
    
    susie.forward(100)
    susie.right(90)
    susie.forward(100)
    susie.right(90)
    susie.forward(100)
    susie.right(90)
    susie.forward(100)
    susie.right(90)

