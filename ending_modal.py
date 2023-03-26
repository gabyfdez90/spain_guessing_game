import tkinter as tk
import turtle

class Modal:
    def show_message_box( message):
        root = tk.Tk()
        root.title("Message Box")
        
        width = 300
        height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
        label = tk.Label(root, text=message)
        label.pack(pady=20)
        
        button = tk.Button(root, text="OK", command=root.destroy)
        button.pack()
        
        root.mainloop()

    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

    def on_click(self,x, y):
        self.show_message_box("¡Enhorabuena! Conoces todas las Comunidades Autónomas de España")
        