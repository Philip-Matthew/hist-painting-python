import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(220)
tim.forward(290)
tim.setheading(0)

colors_list = [(182, 65, 34), (14, 24, 42), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4)]
for dot_count in range(1,101):
    tim.dot(15, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle.Screen()
screen.exitonclick()



"""import colorgram

rgb_colors = []
colors = colorgram.extract('Hist_dot_painting.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)"""