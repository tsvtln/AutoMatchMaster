import os
import sys
import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import *

from workPlace.base_vars import Locations


class HelperFunctions:

    @staticmethod
    def take_screenshot(screenshot_path):
        take_screenshot = pyautogui.screenshot()
        take_screenshot.save(screenshot_path)


class TakeScreenshot(Locations):
    def __init__(self):
        super().__init__()

    def take_screenshot(self):
        # Takes screenshot of the current state of the game.
        screenshot_path = os.path.join(self.screenshot_state_path)
        HelperFunctions.take_screenshot(screenshot_path)


class TkinterWorker(Locations):
    def __init__(self):
        super().__init__()

    # Check of the button selection status
    def getCheckboxValue(self):
        checkedOrNot = self.cbRocket.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbDuck.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbPaint.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbJelly.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbRocketTwo.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbHat.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbOwl.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbBroom.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbLazer.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbWand.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbDragon.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbBaloons.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbLightning.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbLeprichaun.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbBug.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbGeneral.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbTrain.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbRobot.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbUFO.get()
        return checkedOrNot

    def getCheckboxValue(self):
        checkedOrNot = self.cbCobra.get()
        return checkedOrNot

    # Function to update the state of checkboxes
    def updateCheckboxes(self):
        # List of all checkboxes and their corresponding IntVar
        checkboxes = [
            (self.powerRocket, self.cbRocket),
            (self.powerDuck, self.cbDuck),
            (self.powerPaint, self.cbPaint),
            (self.powerJelly, self.cbJelly),
            (self.powerRocketTwo, self.cbRocketTwo),
            (self.powerHat, self.cbHat),
            (self.powerOwl, self.cbOwl),
            (self.powerBroom, self.cbBroom),
            (self.powerLazer, self.cbLazer),
            (self.powerWand, self.cbWand),
            (self.powerDragon, self.cbDragon),
            (self.powerBaloons, self.cbBaloons),
            (self.powerLightning, self.cbLightning),
            (self.powerLeprichaun, self.cbLeprichaun),
            (self.powerBug, self.cbBug),
            (self.powerGeneral, self.cbGeneral),
            (self.powerTrain, self.cbTrain),
            (self.powerRobot, self.cbRobot),
            (self.powerUFO, self.cbUFO),
            (self.powerCobra, self.cbCobra)
        ]

        any_selected = any(var.get() for _, var in checkboxes)

        for checkbox, var in checkboxes:
            if var.get():
                # If this checkbox is selected, leave it enabled
                checkbox.config(state=NORMAL)
            else:
                # Otherwise, disable it if any checkbox is selected
                checkbox.config(state=DISABLED if any_selected else NORMAL)

    # functionality of NEXT BUTTON
    def btnClickFunction(self):
        print('clicked')

    root = Tk()
    # Declarations of the variable associated with the checkboxes for power-up
    cbRocket = tk.IntVar()
    cbDuck = tk.IntVar()
    cbPaint = tk.IntVar()
    cbJelly = tk.IntVar()
    cbRocketTwo = tk.IntVar()
    cbHat = tk.IntVar()
    cbOwl = tk.IntVar()
    cbBroom = tk.IntVar()
    cbLazer = tk.IntVar()
    cbWand = tk.IntVar()
    cbDragon = tk.IntVar()
    cbBaloons = tk.IntVar()
    cbLightning = tk.IntVar()
    cbLeprichaun = tk.IntVar()
    cbBug = tk.IntVar()
    cbGeneral = tk.IntVar()
    cbTrain = tk.IntVar()
    cbRobot = tk.IntVar()
    cbUFO = tk.IntVar()
    cbCobra = tk.IntVar()

    # Main Window
    root.geometry('880x570')
    root.configure(background='#458B00')
    root.title('Auto Match Master')

    # Label
    Label(root, text='POWER UP SELECT', bg='#458B00', font=('arial', 17, 'bold')).place(x=340, y=13)

    # Checkboxes
    powerRocket = Checkbutton(root, text=' ', variable=cbRocket, bg='#F0F8FF', font=('arial', 12, 'bold'),
                              command=updateCheckboxes)
    powerRocket.place(x=20, y=53)

    powerDuck = Checkbutton(root, text=' ', variable=cbDuck, bg='#F0F8FF', font=('arial', 12, 'bold'),
                            command=updateCheckboxes)
    powerDuck.place(x=130, y=53)

    # Image Rocket
    rocket = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    rocket.create_image(37, 0, anchor=NE, image=picture_file)
    rocket.place(x=60, y=53)

    # This is the section of code which creates a checkbox

    # First, we create a canvas to put the picture on
    duck = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    duck.create_image(37, 0, anchor=NE, image=picture_file)
    duck.place(x=170, y=53)

    # This is the section of code which creates a checkbox
    powerPaint = Checkbutton(root, text=' ', variable=cbPaint, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerPaint.place(x=240, y=53)

    # First, we create a canvas to put the picture on
    paint = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    paint.create_image(37, 0, anchor=NE, image=picture_file)
    paint.place(x=280, y=53)

    # This is the section of code which creates a checkbox
    powerJelly = Checkbutton(root, text=' ', variable=cbJelly, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerJelly.place(x=350, y=53)

    # First, we create a canvas to put the picture on
    jelly = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    jelly.create_image(37, 0, anchor=NE, image=picture_file)
    jelly.place(x=390, y=53)

    # This is the section of code which creates a checkbox
    powerRocketTwo = Checkbutton(root, text=' ', variable=cbRocketTwo, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerRocketTwo.place(x=460, y=53)

    # First, we create a canvas to put the picture on
    rocketTwo = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    rocketTwo.create_image(37, 0, anchor=NE, image=picture_file)
    rocketTwo.place(x=500, y=53)

    # This is the section of code which creates a checkbox
    powerHat = Checkbutton(root, text=' ', variable=cbHat, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerHat.place(x=570, y=53)

    # First, we create a canvas to put the picture on
    hat = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    hat.create_image(37, 0, anchor=NE, image=picture_file)
    hat.place(x=610, y=53)

    # This is the section of code which creates a checkbox
    powerOwl = Checkbutton(root, text=' ', variable=cbOwl, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerOwl.place(x=680, y=53)

    # First, we create a canvas to put the picture on
    owl = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    owl.create_image(37, 0, anchor=NE, image=picture_file)
    owl.place(x=720, y=53)

    # This is the section of code which creates a checkbox
    powerBroom = Checkbutton(root, text=' ', variable=cbBroom, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerBroom.place(x=790, y=53)

    # First, we create a canvas to put the picture on
    broom = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    broom.create_image(37, 0, anchor=NE, image=picture_file)
    broom.place(x=830, y=53)

    # This is the section of code which creates a checkbox
    powerLazer = Checkbutton(root, text=' ', variable=cbLazer, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerLazer.place(x=20, y=123)

    # First, we create a canvas to put the picture on
    lazer = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    lazer.create_image(37, 0, anchor=NE, image=picture_file)
    lazer.place(x=60, y=123)

    # This is the section of code which creates a checkbox
    powerWand = Checkbutton(root, text=' ', variable=cbWand, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerWand.place(x=130, y=123)

    # First, we create a canvas to put the picture on
    wand = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    wand.create_image(37, 0, anchor=NE, image=picture_file)
    wand.place(x=170, y=123)

    # This is the section of code which creates a checkbox
    powerDragon = Checkbutton(root, text=' ', variable=cbDragon, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerDragon.place(x=240, y=123)

    # First, we create a canvas to put the picture on
    dragon = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    dragon.create_image(37, 0, anchor=NE, image=picture_file)
    dragon.place(x=280, y=123)

    # This is the section of code which creates a checkbox
    powerBaloons = Checkbutton(root, text=' ', variable=cbBaloons, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerBaloons.place(x=350, y=123)

    # First, we create a canvas to put the picture on
    baloons = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    baloons.create_image(37, 0, anchor=NE, image=picture_file)
    baloons.place(x=390, y=123)

    # This is the section of code which creates a checkbox
    powerLightning = Checkbutton(root, text=' ', variable=cbLightning, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerLightning.place(x=460, y=123)

    # First, we create a canvas to put the picture on
    lightning = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    lightning.create_image(37, 0, anchor=NE, image=picture_file)
    lightning.place(x=500, y=123)

    # This is the section of code which creates a checkbox
    powerLeprichaun = Checkbutton(root, text=' ', variable=cbLeprichaun, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerLeprichaun.place(x=570, y=123)

    # First, we create a canvas to put the picture on
    leprichaun = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    leprichaun.create_image(37, 0, anchor=NE, image=picture_file)
    leprichaun.place(x=610, y=123)

    # This is the section of code which creates a checkbox
    powerBug = Checkbutton(root, text=' ', variable=cbBug, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerBug.place(x=680, y=123)

    # First, we create a canvas to put the picture on
    bug = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    bug.create_image(37, 0, anchor=NE, image=picture_file)
    bug.place(x=720, y=123)

    # This is the section of code which creates a checkbox
    powerGeneral = Checkbutton(root, text=' ', variable=cbGeneral, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerGeneral.place(x=790, y=123)

    # First, we create a canvas to put the picture on
    general = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    general.create_image(37, 0, anchor=NE, image=picture_file)
    general.place(x=830, y=123)

    # This is the section of code which creates a checkbox
    powerTrain = Checkbutton(root, text=' ', variable=cbTrain, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerTrain.place(x=20, y=193)

    # First, we create a canvas to put the picture on
    train = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    train.create_image(37, 0, anchor=NE, image=picture_file)
    train.place(x=60, y=193)

    # This is the section of code which creates a checkbox
    powerRobot = Checkbutton(root, text=' ', variable=cbRobot, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerRobot.place(x=130, y=193)

    # First, we create a canvas to put the picture on
    robot = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    robot.create_image(37, 0, anchor=NE, image=picture_file)
    robot.place(x=170, y=193)

    # This is the section of code which creates a checkbox
    powerUFO = Checkbutton(root, text=' ', variable=cbUFO, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerUFO.place(x=240, y=193)

    # First, we create a canvas to put the picture on
    UFO = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    UFO.create_image(37, 0, anchor=NE, image=picture_file)
    UFO.place(x=280, y=193)

    # This is the section of code which creates a checkbox
    powerCobra = Checkbutton(root, text=' ', variable=cbCobra, bg='#F0F8FF', font=('arial', 12, 'bold'))
    powerCobra.place(x=350, y=193)

    # First, we create a canvas to put the picture on
    cobra = Canvas(root, height=37, width=37)
    # Then, we actually create the image file to use (it has to be a *.gif)
    picture_file = PhotoImage(
        file='')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
    # Finally, we create the image on the canvas and then place it onto the main window
    cobra.create_image(37, 0, anchor=NE, image=picture_file)
    cobra.place(x=390, y=193)

    # This is the section of code which creates a button
    Button(root, text='Next', bg='#F0F8FF', font=('arial', 17, 'bold'), command=btnClickFunction).place(x=400, y=503)

    root.mainloop()
