import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

screen = turtle.Screen()
image = "spain_bg.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()