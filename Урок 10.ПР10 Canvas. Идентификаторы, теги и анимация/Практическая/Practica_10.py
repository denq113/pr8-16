from tkinter import *
x_target = 0
y_target = 0
ball_speed = 3
def clic(event):
    global x_target, y_target
    x_target = event.x
    y_target = event.y
    move_ball()
def move_ball():
    current_coords = c.coords(ball)
    ball_center_x = (current_coords[0] + current_coords[2]) / 2
    ball_center_y = (current_coords[1] + current_coords[3]) / 2

    if abs(ball_center_x - x_target) > ball_speed or abs(ball_center_y - y_target) > ball_speed:
        move_x = ball_speed if ball_center_x < x_target else -ball_speed
        move_y = ball_speed if ball_center_y < y_target else -ball_speed

        c.move(ball, move_x, move_y)
        root.after(10, move_ball)
root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='green')
c.bind('<Button-1>', clic)

root.mainloop()
