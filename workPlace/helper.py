# Game Modes Identifiers:
#     self.MutationLab_solo = SOLO_MutationLab
#     self.MultiplierMadnes_solo = SOLO_MultiplierMadnes
#     self.BombAway_solo = SOLO_BombAway
#     self.MightyMushrooms_solo = SOLO_MightyMushrooms
#     self.ColorCrystals_solo = SOLO_ColorCrystals
#     self.ColorCrush_solo = SOLO_ColorCrush
#     self.Rainbow_solo = SOLO_Rainbow
#     self.CrazyColumns_solo = SOLO_CrazyColumns
#     self.SuperSized_solo = SOLO_SuperSized
#     self.BlowEmUp_solo = SOLO_BlowEmUp
#
#     self.ColorCrush_mr = MatchRumble_ColorCrush
#     self.DrillingDown_mr = MatchRumble_DrillingDown
#
#     self.ColorCrystals_tour = Tournament_ColorCrystals
#     self.ColorCrush_tour = Tournament_ColorCrush
#
#     self.MightyMushrooms_pvp = PVP_MightyMushrooms
#     self.MovesMulti_pvp = PVP_MovesMulti
#     self.DrillingDown_pvp = PVP_DrillingDown
#     self.ColorCrush_pvp = PVP_ColorCrush
#     self.Classic_pvp = PVP_Classic

import os
import pyautogui
import tkinter as tk
from tkinter import *

from workPlace.base_vars import Locations
from workPlace.manipulator import Manipulator


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
        self.selected_power = ''
        self.selected_mode = []

        # Main window init
        self.root = Tk()

        # Main Window
        self.root.geometry('880x570')
        self.root.configure(background='#458B00')
        self.root.title('Auto Match Master')

        # Declarations of the variable associated with the checkboxes for power-up
        self.cbRocket = tk.IntVar()
        self.cbDuck = tk.IntVar()
        self.cbPaint = tk.IntVar()
        self.cbJelly = tk.IntVar()
        self.cbRocketTwo = tk.IntVar()
        self.cbHat = tk.IntVar()
        self.cbOwl = tk.IntVar()
        self.cbBroom = tk.IntVar()
        self.cbLazer = tk.IntVar()
        self.cbWand = tk.IntVar()
        self.cbDragon = tk.IntVar()
        self.cbBaloons = tk.IntVar()
        self.cbLightning = tk.IntVar()
        self.cbLeprichaun = tk.IntVar()
        self.cbBug = tk.IntVar()
        self.cbGeneral = tk.IntVar()
        self.cbTrain = tk.IntVar()
        self.cbSpray = tk.IntVar()
        self.cbRobot = tk.IntVar()
        self.cbUFO = tk.IntVar()
        self.cbCobra = tk.IntVar()

        # Declaration of the variables associated with the checkboxes for game mode
        self.cbMutationLab_solo = tk.IntVar()
        self.cbMultiplierMadnes_solo = tk.IntVar()
        self.cbBombAway_solo = tk.IntVar()
        self.cbMightyMushrooms_solo = tk.IntVar()
        self.cbColorCrystals_solo = tk.IntVar()
        self.cbColorCrush_solo = tk.IntVar()
        self.cbRainbow_solo = tk.IntVar()

        self.cbColorCrush_mr = tk.IntVar()
        self.cbDrillingDown_mr = tk.IntVar()

        self.cbColorCrystals_tour = tk.IntVar()
        self.cbColorCrush_tour = tk.IntVar()

        self.cbMightyMushrooms_pvp = tk.IntVar()
        self.cbMovesMulti_pvp = tk.IntVar()
        self.cbDrillingDown_pvp = tk.IntVar()
        self.cbColorCrush_pvp = tk.IntVar()
        self.cbClassic_pvp = tk.IntVar()

        # new window vars
        self.MutationLab_solo = ''
        self.MultiplierMadnes_solo = ''
        self.BombAway_solo = ''
        self.MightyMushrooms_solo = ''
        self.ColorCrystals_solo = ''
        self.ColorCrush_solo = ''
        self.Rainbow_solo = ''

        self.ColorCrush_mr = ''
        self.DrillingDown_mr = ''

        self.ColorCrystals_tour = ''
        self.ColorCrush_tour = ''

        self.MightyMushrooms_pvp = ''
        self.MovesMulti_pvp = ''
        self.DrillingDown_pvp = ''
        self.ColorCrush_pvp = ''
        self.Classic_pvp = ''

        self.new_window = ''

        # Label
        Label(self.root, text='POWER UP SELECT', bg='#458B00', font=('arial', 17, 'bold')).place(x=340, y=13)

        # Checkboxes
        self.powerRocket = Checkbutton(self.root, text=' ', variable=self.cbRocket, bg='#F0F8FF',
                                       font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerRocket.place(x=20, y=53)

        self.powerDuck = Checkbutton(self.root, text=' ', variable=self.cbDuck, bg='#F0F8FF',
                                     font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerDuck.place(x=130, y=53)

        self.powerPaint = Checkbutton(self.root, text=' ', variable=self.cbPaint, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerPaint.place(x=240, y=53)

        self.powerJelly = Checkbutton(self.root, text=' ', variable=self.cbJelly, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerJelly.place(x=350, y=53)

        self.powerRocketTwo = Checkbutton(self.root, text=' ', variable=self.cbRocketTwo, bg='#F0F8FF',
                                          font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerRocketTwo.place(x=460, y=53)

        self.powerHat = Checkbutton(self.root, text=' ', variable=self.cbHat, bg='#F0F8FF', font=('arial', 12, 'bold'),
                                    command=self.updateCheckboxes)
        self.powerHat.place(x=570, y=53)

        self.powerOwl = Checkbutton(self.root, text=' ', variable=self.cbOwl, bg='#F0F8FF', font=('arial', 12, 'bold'),
                                    command=self.updateCheckboxes)
        self.powerOwl.place(x=680, y=53)

        self.powerBroom = Checkbutton(self.root, text=' ', variable=self.cbBroom, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerBroom.place(x=790, y=53)

        self.powerLazer = Checkbutton(self.root, text=' ', variable=self.cbLazer, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerLazer.place(x=20, y=123)

        self.powerWand = Checkbutton(self.root, text=' ', variable=self.cbWand, bg='#F0F8FF',
                                     font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerWand.place(x=130, y=123)

        self.powerDragon = Checkbutton(self.root, text=' ', variable=self.cbDragon, bg='#F0F8FF',
                                       font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerDragon.place(x=240, y=123)

        self.powerBaloons = Checkbutton(self.root, text=' ', variable=self.cbBaloons, bg='#F0F8FF',
                                        font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerBaloons.place(x=350, y=123)

        self.powerLightning = Checkbutton(self.root, text=' ', variable=self.cbLightning, bg='#F0F8FF',
                                          font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerLightning.place(x=460, y=123)

        self.powerLeprichaun = Checkbutton(self.root, text=' ', variable=self.cbLeprichaun, bg='#F0F8FF',
                                           font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerLeprichaun.place(x=570, y=123)

        self.powerBug = Checkbutton(self.root, text=' ', variable=self.cbBug, bg='#F0F8FF', font=('arial', 12, 'bold'),
                                    command=self.updateCheckboxes)
        self.powerBug.place(x=680, y=123)

        self.powerGeneral = Checkbutton(self.root, text=' ', variable=self.cbGeneral, bg='#F0F8FF',
                                        font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerGeneral.place(x=790, y=123)

        self.powerTrain = Checkbutton(self.root, text=' ', variable=self.cbTrain, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerTrain.place(x=20, y=193)

        self.powerSpray = Checkbutton(self.root, text=' ', variable=self.cbSpray, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerSpray.place(x=130, y=193)

        self.powerRobot = Checkbutton(self.root, text=' ', variable=self.cbRobot, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerRobot.place(x=240, y=193)

        self.powerUFO = Checkbutton(self.root, text=' ', variable=self.cbUFO, bg='#F0F8FF',
                                    font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerUFO.place(x=350, y=193)

        self.powerCobra = Checkbutton(self.root, text=' ', variable=self.cbCobra, bg='#F0F8FF',
                                      font=('arial', 12, 'bold'), command=self.updateCheckboxes)
        self.powerCobra.place(x=460, y=193)

        # Images for buttons

        # Rocket
        self.rocket = Canvas(self.root, height=34, width=34)
        picture_rocket = PhotoImage(file=self.power_rocket_pic)
        self.rocket.create_image(37, 0, anchor=NE, image=picture_rocket)
        self.rocket.place(x=60, y=53)

        # Duck
        self.duck = Canvas(self.root, height=34, width=34)
        picture_duck = PhotoImage(file=self.power_duck_pic)
        self.duck.create_image(37, 0, anchor=NE, image=picture_duck)
        self.duck.place(x=170, y=53)

        # Paint
        self.paint = Canvas(self.root, height=34, width=34)
        picture_paint = PhotoImage(file=self.power_paint_pic)
        self.paint.create_image(37, 0, anchor=NE, image=picture_paint)
        self.paint.place(x=280, y=53)

        # Jelly
        self.jelly = Canvas(self.root, height=34, width=34)
        picture_jelly = PhotoImage(file=self.power_jelly_pic)
        self.jelly.create_image(37, 0, anchor=NE, image=picture_jelly)
        self.jelly.place(x=390, y=53)

        # RocketTwo
        self.rocketTwo = Canvas(self.root, height=34, width=34)
        picture_rocketTwo = PhotoImage(file=self.power_rocket2_pic)
        self.rocketTwo.create_image(37, 0, anchor=NE, image=picture_rocketTwo)
        self.rocketTwo.place(x=500, y=53)

        # Hat
        self.hat = Canvas(self.root, height=34, width=34)
        picture_hat = PhotoImage(file=self.power_hat_pic)
        self.hat.create_image(37, 0, anchor=NE, image=picture_hat)
        self.hat.place(x=610, y=53)

        # Owl
        self.owl = Canvas(self.root, height=34, width=34)
        picture_owl = PhotoImage(file=self.power_owl_pic)
        self.owl.create_image(37, 0, anchor=NE, image=picture_owl)
        self.owl.place(x=720, y=53)

        # Broom
        self.broom = Canvas(self.root, height=34, width=34)
        picture_broom = PhotoImage(file=self.power_broom_pic)
        self.broom.create_image(37, 0, anchor=NE, image=picture_broom)
        self.broom.place(x=830, y=53)

        # Lazer
        self.lazer = Canvas(self.root, height=34, width=34)
        picture_lazer = PhotoImage(file=self.power_lazer_pic)
        self.lazer.create_image(37, 0, anchor=NE, image=picture_lazer)
        self.lazer.place(x=60, y=123)

        # Wand
        self.wand = Canvas(self.root, height=34, width=34)
        picture_wand = PhotoImage(file=self.power_wand_pic)
        self.wand.create_image(37, 0, anchor=NE, image=picture_wand)
        self.wand.place(x=170, y=123)

        # Dragon
        self.dragon = Canvas(self.root, height=34, width=34)
        picture_dragon = PhotoImage(file=self.power_dragon_pic)
        self.dragon.create_image(37, 0, anchor=NE, image=picture_dragon)
        self.dragon.place(x=280, y=123)

        # Balloons
        self.baloons = Canvas(self.root, height=34, width=34)
        picture_baloons = PhotoImage(file=self.power_baloons_pic)
        self.baloons.create_image(37, 0, anchor=NE, image=picture_baloons)
        self.baloons.place(x=390, y=123)

        # Lightning
        self.lightning = Canvas(self.root, height=34, width=34)
        picture_lightning = PhotoImage(file=self.power_lightning_pic)
        self.lightning.create_image(37, 0, anchor=NE, image=picture_lightning)
        self.lightning.place(x=500, y=123)

        # Leprichaun
        self.leprichaun = Canvas(self.root, height=34, width=34)
        picture_leprichaun = PhotoImage(file=self.power_leprichaun_pic)
        self.leprichaun.create_image(37, 0, anchor=NE, image=picture_leprichaun)
        self.leprichaun.place(x=610, y=123)

        # Bug
        self.bug = Canvas(self.root, height=34, width=34)
        picture_bug = PhotoImage(file=self.power_bug_pic)
        self.bug.create_image(37, 0, anchor=NE, image=picture_bug)
        self.bug.place(x=720, y=123)

        # General
        self.general = Canvas(self.root, height=34, width=34)
        picture_general = PhotoImage(file=self.power_general_pic)
        self.general.create_image(37, 0, anchor=NE, image=picture_general)
        self.general.place(x=830, y=123)

        # Train
        self.train = Canvas(self.root, height=34, width=34)
        picture_train = PhotoImage(file=self.power_train_pic)
        self.train.create_image(37, 0, anchor=NE, image=picture_train)
        self.train.place(x=60, y=193)

        # Spray
        self.spray = Canvas(self.root, height=34, width=34)
        picture_spray = PhotoImage(file=self.power_spray_pic)
        self.spray.create_image(37, 0, anchor=NE, image=picture_spray)
        self.spray.place(x=170, y=193)

        # Robot
        self.robot = Canvas(self.root, height=34, width=34)
        picture_robot = PhotoImage(file=self.power_robot_pic)
        self.robot.create_image(37, 0, anchor=NE, image=picture_robot)
        self.robot.place(x=280, y=193)

        # UFO
        self.UFO = Canvas(self.root, height=34, width=34)
        picture_UFO = PhotoImage(file=self.power_ufo_pic)
        self.UFO.create_image(37, 0, anchor=NE, image=picture_UFO)
        self.UFO.place(x=390, y=193)

        # Cobra
        self.cobra = Canvas(self.root, height=34, width=34)
        picture_cobra = PhotoImage(file=self.power_cobra_pic)
        self.cobra.create_image(37, 0, anchor=NE, image=picture_cobra)
        self.cobra.place(x=500, y=193)

        # Next button
        Button(self.root, text='Next', bg='#F0F8FF', font=('arial', 17, 'bold'),
               command=self.btnClickFunction).place(x=400, y=503)

        # main loop start
        self.root.mainloop()

    def exceptionPopUp(self, message):
        # Create a new top-level window for the exception message
        exception_window = tk.Toplevel()
        exception_window.title("Error")

        # Center the window on the screen
        exception_window.geometry("300x150")

        # Add a label with the exception message
        label = tk.Label(exception_window, text=message, wraplength=250)
        label.pack(pady=20)

        # Add an "OK" button to close the exception window
        ok_button = tk.Button(exception_window, text="OK", command=exception_window.destroy)
        ok_button.pack(pady=10)

        # Make the window modal (it will block interaction with other windows)
        exception_window.transient()
        exception_window.grab_set()
        exception_window.wait_window()

    def getCheckboxValue(self):  # Check of the status of selected checkboxes
        checkboxes = [
            self.cbRocket,
            self.cbDuck,
            self.cbPaint,
            self.cbJelly,
            self.cbRocketTwo,
            self.cbHat,
            self.cbOwl,
            self.cbBroom,
            self.cbLazer,
            self.cbWand,
            self.cbDragon,
            self.cbBaloons,
            self.cbLightning,
            self.cbLeprichaun,
            self.cbBug,
            self.cbGeneral,
            self.cbTrain,
            self.cbSpray,
            self.cbRobot,
            self.cbUFO,
            self.cbCobra
        ]

        # Check if any checkbox is checked
        checkedOrNot = any(checkbox.get() for checkbox in checkboxes)
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
            (self.powerSpray, self.cbSpray),
            (self.powerRobot, self.cbRobot),
            (self.powerUFO, self.cbUFO),
            (self.powerCobra, self.cbCobra),
        ]

        any_selected = any(var.get() for _, var in checkboxes)

        for checkbox, var in checkboxes:
            if var.get():
                # If this checkbox is selected, leave it enabled
                checkbox.config(state=NORMAL)
            else:
                # Otherwise, disable it if any checkbox is selected
                checkbox.config(state=DISABLED if any_selected else NORMAL)

    # Functionality of NEXT BUTTON
    def btnClickFunction(self):
        checkboxes = [
            ('Rocket', self.cbRocket), ('Duck', self.cbDuck), ('Paint', self.cbPaint), ('Jelly', self.cbJelly),
            ('RocketTwo', self.cbRocketTwo), ('Hat', self.cbHat), ('Owl', self.cbOwl), ('Broom', self.cbBroom),
            ('Lazer', self.cbLazer), ('Wand', self.cbWand), ('Dragon', self.cbDragon), ('Baloons', self.cbBaloons),
            ('Lightning', self.cbLightning), ('Leprichaun', self.cbLeprichaun), ('Bug', self.cbBug),
            ('General', self.cbGeneral), ('Train', self.cbTrain), ('Robot', self.cbRobot), ('UFO', self.cbUFO),
            ('Cobra', self.cbCobra)
        ]

        selected_checkboxes = [name for name, var in checkboxes if var.get()]
        try:
            self.selected_power = selected_checkboxes[0]
            self.open_new_window(self.root)
        except IndexError as e:
            m = 'You need to select a power-up!'
            self.exceptionPopUp(m)

    def btnClickNewWindow(self):
        if len(self.selected_mode) > 1:
            self.selected_mode.clear()
            m = 'Select only 1 game mode!'
            self.exceptionPopUp(m)
            self.open_new_window(self.new_window)
        elif len(self.selected_mode) == 0:
            m = 'Select at least 1 game mode!'
            self.exceptionPopUp(m)
        else:
            # Goes into manipulation mode, where decision on further action is made.
            Manipulator(self.selected_power, self.selected_mode)
            self.new_window.destroy()

    def getGameModeSelection(self, game_mode):
        self.selected_mode.append(game_mode)

    def open_new_window(self, current_window):
        # Close the current window
        current_window.destroy()

        # Create a new window
        self.new_window = tk.Tk()
        self.new_window.title('Auto Match Master')
        self.new_window.geometry('880x570')
        self.new_window.configure(background='#008B00')

        # Labels
        Label(self.new_window, text='SOLO', bg='#008B00', font=('arial', 12, 'bold')).place(x=11, y=7)
        Label(self.new_window, text='MATCH RUMBLE', bg='#008B00', font=('arial', 12, 'bold')).place(x=11, y=127)
        Label(self.new_window, text='TOURNAMENT', bg='#008B00', font=('arial', 12, 'bold')).place(x=11, y=257)
        Label(self.new_window, text='PvP', bg='#008B00', font=('arial', 12, 'bold')).place(x=11, y=387)

        # Button
        Button(self.new_window, text='NEXT', bg='#F0F8FF', font=('arial', 12, 'normal'),
               command=self.btnClickNewWindow).place(x=391, y=517)

        # Checkboxes
        # solo
        self.MutationLab_solo = Checkbutton(self.new_window, text='Mutation Lab', variable=self.cbMutationLab_solo,
                                            bg='#F0F8FF', font=('arial', 12, 'normal'),
                                            command=lambda: self.getGameModeSelection('SOLO_MutationLab'))
        self.MutationLab_solo.place(x=11, y=27)
        #
        self.MultiplierMadnes_solo = Checkbutton(self.new_window, text='Multiplier Madnes',
                                                 variable=self.cbMultiplierMadnes_solo, bg='#F0F8FF',
                                                 font=('arial', 12, 'normal'),
                                                 command=lambda: self.getGameModeSelection('SOLO_MultiplierMadnes'))
        self.MultiplierMadnes_solo.place(x=141, y=27)
        #
        self.BombAway_solo = Checkbutton(self.new_window, text='Bomb Away', variable=self.cbBombAway_solo, bg='#F0F8FF',
                                         font=('arial', 12, 'normal'),
                                         command=lambda: self.getGameModeSelection('SOLO_BombAway'))
        self.BombAway_solo.place(x=301, y=27)
        #
        self.MightyMushrooms_solo = Checkbutton(self.new_window, text='Might Mushrooms',
                                                variable=self.cbMightyMushrooms_solo, bg='#F0F8FF',
                                                font=('arial', 12, 'normal'),
                                                command=lambda: self.getGameModeSelection('SOLO_MightyMushrooms'))
        self.MightyMushrooms_solo.place(x=423, y=27)
        #
        self.ColorCrystals_solo = Checkbutton(self.new_window, text='Color Crystals',
                                              variable=self.cbColorCrystals_solo, bg='#F0F8FF',
                                              font=('arial', 12, 'normal'),
                                              command=lambda: self.getGameModeSelection('SOLO_ColorCrystals'))
        self.ColorCrystals_solo.place(x=585, y=27)
        #
        self.ColorCrush_solo = Checkbutton(self.new_window, text='Color Crush',
                                           variable=self.cbColorCrush_solo, bg='#F0F8FF',
                                           font=('arial', 12, 'normal'),
                                           command=lambda: self.getGameModeSelection('SOLO_ColorCrush'))
        self.ColorCrush_solo.place(x=722, y=27)
        #
        self.Rainbow_solo = Checkbutton(self.new_window, text='Rainbow', variable=self.cbRainbow_solo,
                                        bg='#F0F8FF', font=('arial', 12, 'normal'),
                                        command=lambda: self.getGameModeSelection('SOLO_Rainbow'))
        self.Rainbow_solo.place(x=11, y=65)

        # Match Rumble
        self.ColorCrush_mr = Checkbutton(self.new_window, text='Color Crush', variable=self.cbColorCrush_mr,
                                         bg='#F0F8FF',
                                         font=('arial', 12, 'normal'),
                                         command=lambda: self.getGameModeSelection('MatchRumble_ColorCrush'))
        self.ColorCrush_mr.place(x=11, y=157)
        #
        self.DrillingDown_mr = Checkbutton(self.new_window, text='Drilling Down', variable=self.cbDrillingDown_mr,
                                           bg='#F0F8FF',
                                           font=('arial', 12, 'normal'),
                                           command=lambda: self.getGameModeSelection('MatchRumble_DrillingDown'))
        self.DrillingDown_mr.place(x=134, y=157)

        # Tournament
        self.ColorCrystals_tour = Checkbutton(self.new_window, text='Color Crystals',
                                              variable=self.cbColorCrystals_tour,
                                              bg='#F0F8FF',
                                              font=('arial', 12, 'normal'),
                                              command=lambda: self.getGameModeSelection('Tournament_ColorCrystals'))
        self.ColorCrystals_tour.place(x=11, y=277)
        #
        self.ColorCrush_tour = Checkbutton(self.new_window, text='Color Crush', variable=self.cbColorCrush_tour,
                                           bg='#F0F8FF', font=('arial', 12, 'normal'),
                                           command=lambda: self.getGameModeSelection('Tournament_ColorCrush'))
        self.ColorCrush_tour.place(x=148, y=277)

        # PvP
        self.MightyMushrooms_pvp = Checkbutton(self.new_window, text='Mighty Mushrooms',
                                               variable=self.cbMightyMushrooms_pvp,
                                               bg='#F0F8FF',
                                               font=('arial', 12, 'normal'),
                                               command=lambda: self.getGameModeSelection('PVP_MightyMushrooms'))
        self.MightyMushrooms_pvp.place(x=11, y=407)
        #
        self.MovesMulti_pvp = Checkbutton(self.new_window, text='Moves Multiplier',
                                          variable=self.cbMovesMulti_pvp,
                                          bg='#F0F8FF',
                                          font=('arial', 12, 'normal'),
                                          command=lambda: self.getGameModeSelection('PVP_MovesMulti'))
        self.MovesMulti_pvp.place(x=180, y=407)
        #
        self.DrillingDown_pvp = Checkbutton(self.new_window, text='Drilling Down',
                                            variable=self.cbDrillingDown_pvp,
                                            bg='#F0F8FF',
                                            font=('arial', 12, 'normal'),
                                            command=lambda: self.getGameModeSelection('PVP_DrillingDown'))
        self.DrillingDown_pvp.place(x=332, y=407)
        #
        self.ColorCrush_pvp = Checkbutton(self.new_window, text='Color Crush',
                                          variable=self.cbColorCrush_pvp,
                                          bg='#F0F8FF',
                                          font=('arial', 12, 'normal'),
                                          command=lambda: self.getGameModeSelection('PVP_ColorCrush'))
        self.ColorCrush_pvp.place(x=464, y=407)
        #
        self.Classic_pvp = Checkbutton(self.new_window, text='Classic',
                                       variable=self.cbClassic_pvp,
                                       bg='#F0F8FF',
                                       font=('arial', 12, 'normal'),
                                       command=lambda: self.getGameModeSelection('PVP_Classic'))
        self.Classic_pvp.place(x=586, y=407)

        # Start the Tkinter event loop for the new window
        self.new_window.mainloop()
