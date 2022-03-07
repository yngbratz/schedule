from tkinter import *
import datetime   
import json
import days_of_the_week.monday as monday
import days_of_the_week.tuesday as tuesday
import days_of_the_week.wednesday as wednesday
import days_of_the_week.thursday as thursday
import days_of_the_week.friday as friday
from PIL import Image
from tkinter import messagebox

class MainWindow(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        width = round(Frame.winfo_screenwidth(self)/2)
        height = round(Frame.winfo_screenheight(self)/2)
    
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        enter_class = Button(self, text="Enter class", width = int(width*0.02), height = int(height*0.02), command=self.enter_class)
        enter_class.pack(side = LEFT)

        schedule = Button(self, text="Schedule", width = int(width*0.02), height = int(height*0.02), command=self.show_schedule)
        schedule.pack(side = RIGHT)

    def enter_class(self):
        day = datetime.datetime.today().weekday()

        if day == 0:
            monday.monday()    
        if day == 1:
            tuesday.tuesday()
        if day == 2:
            wednesday.wednesday()
        if day == 3:
            thursday.thursday()
        if day == 4:
            friday.friday()

    def show_schedule(self):
        img = Image.open("img/fmi_schedule.png")
        img.show()


def noclass():
    messagebox.showinfo(title = "Info", message = "You have no class to attend to right now")


def main_window():
    root = Tk()

    width = round(root.winfo_screenwidth()/2)
    height = round(root.winfo_screenheight()/2)

    app = MainWindow(root)
    root.wm_title("FMI Schedule")

    root.geometry(str(0) + 'x' + str(0))
    root.minsize(int(width*0.2)*3, int(width*0.02)*20)

    root.mainloop()