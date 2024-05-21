import tkinter as tk
from tkinter import Checkbutton, Button, Label
from tkinter import *

class AutoMatchMaster:

    def __init__(self):
        self.MutationLab = MutationLab


    def btnClickNewWindow(self):
        # Your button click logic here
        pass

    def open_new_window(self, current_window):
        # Declarations of the variables associated with checkboxes for modes
        cbMutationLab = tk.IntVar()
        cbMultiplierMadnes = tk.IntVar()
        cbBombAway = tk.IntVar()
        cbColorCrush = tk.IntVar()
        cbColorCrystals = tk.IntVar()
        cbMightyMushrooms = tk.IntVar()

    def updateCheckBoxesNewWindow(self):
        # List of all IntVar objects
        cbx = [
            (self.MutationLab, self.cbMutationLab),
            (self.MultiplierMadnes, self.cbMultiplierMadnes),
            (self.BombAway, self.cbBombAway),
            (self.ColorCrush, self.cbColorCrush),
            (self.ColorCrystals, self.cbColorCrystals),
            (self.MightyMushrooms, self.cbMightyMushrooms)
        ]

        any_selected = any(var.get() for _, var in cbx)

        for checkbox, var in cbx:
            if var.get():
                checkbox.config(state=NORMAL)
            else:
                checkbox.config(state=DISABLED if any_selected else NORMAL)

        # Close the current window
        current_window.destroy()

        # Create a new window
        new_window = tk.Tk()
        new_window.title('Auto Match Master')
        new_window.geometry('880x570')
        new_window.configure(background='#008B00')

        # Labels
        Label(new_window, text='SOLO', bg='#008B00', font=('arial', 12, 'bold')).place(x=11, y=7)
        Label(new_window, text='MATCH RUMBLE', bg='#008B00', font=('arial', 12, 'normal')).place(x=11, y=127)
        Label(new_window, text='TOURNAMENT', bg='#008B00', font=('arial', 12, 'normal')).place(x=11, y=257)
        Label(new_window, text='PvP', bg='#008B00', font=('arial', 12, 'normal')).place(x=11, y=387)

        # Button
        Button(new_window, text='NEXT', bg='#F0F8FF', font=('arial', 12, 'normal'),
               command=self.btnClickNewWindow).place(x=391, y=517)

        # Checkboxes
        MutationLab = Checkbutton(new_window, text='MutationLab', variable=cbMutationLab, bg='#F0F8FF',
                                  font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        MutationLab.place(x=11, y=27)

        MultiplierMadnes = Checkbutton(new_window, text='MultiplierMadnes', variable=cbMultiplierMadnes, bg='#F0F8FF',
                                       font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        MultiplierMadnes.place(x=141, y=27)

        BombAway = Checkbutton(new_window, text='BombAway', variable=cbBombAway, bg='#F0F8FF',
                               font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        BombAway.place(x=301, y=27)

        ColorCrush = Checkbutton(new_window, text='ColorCrush', variable=cbColorCrush, bg='#F0F8FF',
                                 font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        ColorCrush.place(x=11, y=157)

        ColorCrystals = Checkbutton(new_window, text='ColorCrystals', variable=cbColorCrystals, bg='#F0F8FF',
                                    font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        ColorCrystals.place(x=11, y=277)

        MightyMushrooms = Checkbutton(new_window, text='MightyMushrooms', variable=cbMightyMushrooms, bg='#F0F8FF',
                                      font=('arial', 12, 'normal'), command=updateCheckBoxesNewWindow)
        MightyMushrooms.place(x=11, y=407)

        checkbox_objects = [MutationLab, MultiplierMadnes, BombAway, ColorCrush, ColorCrystals, MightyMushrooms]

        new_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AutoMatchMaster()
    app.open_new_window(root)




    def updateCheckBoxesNewWindow(self, Mut, Mul, Bom, Col, ColC, Mig):
        # List of all IntVar objects
        cbx = [
            (Mut, self.cbMutationLab),
            (Mul, self.cbMultiplierMadnes),
            (Bom, self.cbBombAway),
            (Col, self.cbColorCrush),
            (ColC, self.cbColorCrystals),
            (Mig, self.cbMightyMushrooms)
        ]

        any_selected = any(var.get() for _, var in cbx)

        return any_selected

        for checkbox, var in cbx:
            if var.get():
                checkbox.config(state=NORMAL)
            else:
                checkbox.config(state=DISABLED if any_selected else NORMAL)

                command = lambda: self.updateCheckBoxesNewWindow(MutationLab,
                                                                 MultiplierMadnes,
                                                                 BombAway,
                                                                 ColorCrush,
                                                                 ColorCrystals,
                                                                 MightyMushrooms))