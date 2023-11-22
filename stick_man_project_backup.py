'''
Author name: Jeremiah E. Ochepo
last Edited: 2/15/2020 (7PM)
Description: Using GUI to create a program in Python that displays a stickman.

Credit:
1. John Zelle (imported Button class)
2. Import random
3. Import graphics
'''

import random
from graphics import *
from button import Button

# Initialize the graphics window
win = GraphWin("Stick Man", 600, 600)


# Display instructions for color buttons
def user_instruction():
    msg = "(1) Select size to view stick man\n"
    msg += "(2) Select color to color stick man\n"
    msg += "(3) Press erase to delete stick man\n"
    msg += "(4) Press quit to end program"

    message = Text(Point(460, 40), msg)
    message.setFace("times roman")
    message.setSize(10)
    message.setTextColor("black")
    message.draw(win)


user_instruction()


# Define the StickMan class
class StickMan(object):

    def __init__(self, name, color_list):
        # Attributes
        self.name = name
        self.color_list = color_list

    def large_stickman(self):
        # Draw large stickman components
        self.head = Circle(Point(160, 65), 50)
        self.right_eye = Circle(Point(140, 55), 5)
        self.right_eye_color = Circle(Point(140, 55), 3)
        self.left_eye = Circle(Point(180, 55), 5)
        self.left_eye_color = Circle(Point(180, 55), 3)
        self.nose = Oval(Point(155, 75), Point(165, 75))
        self.mouth = Oval(Point(140, 105), Point(180, 95))
        self.neck = Oval(Point(155, 135), Point(165, 195))
        self.neck.setWidth(40)
        self.sholder = Line(Point(245, 190), Point(75, 190))
        self.sholder.setWidth(40)
        self.T_shirt = Line(Point(160, 375), Point(160, 160))
        self.T_shirt.setWidth(140)
        self.right_arm = Line(Point(240, 190), Point(300, 190))
        self.right_arm.setWidth(20)
        self.left_arm = Line(Point(80, 190), Point(20, 190))
        self.left_arm.setWidth(20)
        self.right_pants = Rectangle(Point(110, 450), Point(150, 375))
        self.right_pants.setWidth(2)
        self.right_leg = Rectangle(Point(125, 530), Point(135, 460))
        self.right_leg.setWidth(20)
        self.left_pants = Rectangle(Point(170, 450), Point(210, 375))
        self.left_pants.setWidth(2)
        self.left_leg = Rectangle(Point(185, 460), Point(195, 530))
        self.left_leg.setWidth(20)

    def medium_stickman(self):
        # Draw medium stickman components
        self.head = Circle(Point(160, 80), 50)
        self.right_eye = Circle(Point(140, 65), 4)
        self.right_eye_color = Circle(Point(140, 65), 2)
        self.left_eye = Circle(Point(180, 65), 4)
        self.left_eye_color = Circle(Point(180, 65), 2)
        self.nose = Oval(Point(155, 90), Point(165, 90))
        self.mouth = Oval(Point(140, 120), Point(180, 110))
        self.neck = Oval(Point(155, 145), Point(165, 175))
        self.neck.setWidth(30)
        self.sholder = Line(Point(245, 185), Point(75, 185))
        self.sholder.setWidth(30)
        self.T_shirt = Line(Point(160, 375), Point(160, 160))
        self.T_shirt.setWidth(130)
        self.right_arm = Line(Point(240, 185), Point(300, 185))
        self.right_arm.setWidth(15)
        self.left_arm = Line(Point(80, 185), Point(20, 185))
        self.left_arm.setWidth(15)
        self.right_pants = Rectangle(Point(110, 440), Point(150, 375))
        self.right_pants.setWidth(2)
        self.right_leg = Rectangle(Point(125, 510), Point(135, 445))
        self.right_leg.setWidth(15)
        self.left_pants = Rectangle(Point(170, 440), Point(210, 375))
        self.left_pants.setWidth(2)
        self.left_leg = Rectangle(Point(185, 510), Point(195, 445))
        self.left_leg.setWidth(15)

    def small_stickman(self):
        # Draw small stickman components
        self.head = Circle(Point(160, 100), 30)
        self.right_eye = Circle(Point(145, 87), 3)
        self.right_eye_color = Circle(Point(145, 87), 1)
        self.left_eye = Circle(Point(175, 87), 3)
        self.left_eye_color = Circle(Point(175, 87), 1)
        self.nose = Oval(Point(155, 102), Point(165, 102))
        self.mouth = Oval(Point(155, 120), Point(165, 115))
        self.neck = Oval(Point(155, 138), Point(165, 175))
        self.neck.setWidth(20)
        self.sholder = Line(Point(245, 165), Point(75, 165))
        self.sholder.setWidth(20)
        self.T_shirt = Line(Point(160, 300), Point(160, 150))
        self.T_shirt.setWidth(110)
        self.right_arm = Line(Point(240, 165), Point(300, 165))
        self.right_arm.setWidth(8)
        self.left_arm = Line(Point(80, 165), Point(20, 165))
        self.left_arm.setWidth(8)
        self.right_pants = Rectangle(Point(110, 300), Point(150, 355))
        self.right_pants.setWidth(1)
        self.right_leg = Rectangle(Point(125, 360), Point(135, 400))
        self.right_leg.setWidth(10)
        self.left_pants = Rectangle(Point(170, 300), Point(210, 355))
        self.left_pants.setWidth(1)
        self.left_leg = Rectangle(Point(185, 360), Point(195, 400))
        self.left_leg.setWidth(10)

    def draw_stickman(self):
        # Draw all stickman components
        self.head.draw(win)
        self.right_eye.draw(win)
        self.right_eye_color.draw(win)
        self.left_eye.draw(win)
        self.left_eye_color.draw(win)
        self.nose.draw(win)
        self.mouth.draw(win)
        self.neck.draw(win)
        self.sholder.draw(win)
        self.T_shirt.draw(win)
        self.right_arm.draw(win)
        self.left_arm.draw(win)
        self.right_pants.draw(win)
        self.right_leg.draw(win)
        self.left_pants.draw(win)
        self.left_leg.draw(win)

    def color_stickman_method(self):
        # Color the stickman components
        self.head.setFill(random.choice([self.color_list[2], self.color_list[3], self.color_list[4]]))
        self.right_eye.setFill(self.color_list[0])
        self.right_eye_color.setFill(self.color_list[7])
        self.left_eye.setFill(self.color_list[0])
        self.left_eye_color.setFill(self.color_list[7])
        self.nose.setFill(self.color_list[0])
        self.mouth.setFill(self.color_list[0])
        self.neck.setFill(self.color_list[0])
        self.sholder.setFill(self.color_list[6])
        self.T_shirt.setFill(self.color_list[5])
        self.right_arm.setFill(self.color_list[0])
        self.left_arm.setFill(self.color_list[0])
        self.right_pants.setFill(self.color_list[6])
        self.right_leg.setFill(self.color_list[0])
        self.left_pants.setFill(self.color_list[6])
        self.left_leg.setFill(self.color_list[0])

    def undraw_method(self):
        # Undraw all stickman components
        self.head.undraw()
        self.right_eye.undraw()
        self.right_eye_color.undraw()
        self.left_eye.undraw()
        self.left_eye_color.undraw()
        self.nose.undraw()
        self.mouth.undraw()
        self.neck.undraw()
        self.sholder.undraw()
        self.T_shirt.undraw()
        self.right_arm.undraw()
        self.left_arm.undraw()
        self.right_pants.undraw()
        self.right_leg.undraw()
        self.left_pants.undraw()
        self.left_leg.undraw()


# Initialize StickMan object
name = 'Mr. Stick Man'
color_list = ['black', 'yellow', 'red1', 'blue', 'green', 'brown', 'gray', 'white']
stickman_instanciator = StickMan(name, color_list)


# Methods for drawing stickman of different sizes
def draw_large_black_and_white_version_of_stickman(stickman_instanciator):
    stickman_instanciator.large_stickman()
    stickman_instanciator.draw_stickman()


def draw_medium_black_and_white_version_of_stickman(stickman_instanciator):
    stickman_instanciator.medium_stickman()
    stickman_instanciator.draw_stickman()


def draw_small_black_and_white_version_of_stickman(stickman_instanciator):
    stickman_instanciator.small_stickman()
    stickman_instanciator.draw_stickman()


def draw_colored_version_of_stickman(stickman_instanciator):
    stickman_instanciator.color_stickman_method()


def undraw_stickman(stickman_instanciator):
    stickman_instanciator.undraw_method()


# Event Loop
def main(active_flag):
    # Button methods
    def my_large_button_method():
        large_button = Button(win, Point(460, 100), 100, 20, "Large")
        large_button.activate()
        return large_button

    my_large_button_method()

    def my_medium_button_method():
        medium_button = Button(win, Point(460, 125), 100, 20, "Medium")
        medium_button.activate()
        return medium_button

    my_medium_button_method()

    def my_small_button_method():
        small_button = Button(win, Point(460, 150), 100, 20, "Small")
        small_button.activate()
        return small_button

    my_small_button_method()

    def my_color_button_method():
        color_button = Button(win, Point(460, 175), 100, 20, "color")
        color_button.activate()
        return color_button

    my_color_button_method()

    def my_erase_button_method():
        erase_button = Button(win, Point(460, 200), 100, 20, "Erase")
        erase_button.activate()
        return erase_button

    my_erase_button_method()

    def my_quit_button_method():
        quit_button = Button(win, Point(460, 225), 100, 20, "Quit")
        quit_button.activate()
        return quit_button

    my_quit_button_method()

    # Call all button methods
    large_button = my_large_button_method()
    medium_button = my_medium_button_method()
    small_button = my_small_button_method()
    color_button = my_color_button_method()
    erase_button = my_erase_button_method()
    quit_button = my_quit_button_method()

    # Default stickman
    draw_large_black_and_white_version_of_stickman(stickman_instanciator)

    mouse_point = win.getMouse()  # Point Clicked
    while active_flag:

        if large_button.clicked(mouse_point):
            undraw_stickman(stickman_instanciator)
            draw_large_black_and_white_version_of_stickman(stickman_instanciator)

        elif medium_button.clicked(mouse_point):
            undraw_stickman(stickman_instanciator)
            draw_medium_black_and_white_version_of_stickman(stickman_instanciator)

        elif small_button.clicked(mouse_point):
            undraw_stickman(stickman_instanciator)
            draw_small_black_and_white_version_of_stickman(stickman_instanciator)

        elif color_button.clicked(mouse_point):
            draw_colored_version_of_stickman(stickman_instanciator)

        elif erase_button.clicked(mouse_point):
            undraw_stickman(stickman_instanciator)

        elif quit_button.clicked(mouse_point):
            win.close()
            active_flag = False

        mouse_point = win.getMouse()  # Point Clicked


try:
    main(active_flag=True)
except:
    pass
