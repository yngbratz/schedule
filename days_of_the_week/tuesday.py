import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

def tuesday():
    tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

    if tm >= clock.clock(9, 35) and tm <= clock.clock(11, 10):
        webbrowser.open(t.teachers["gabriel_arnautu"])
        exit()

    elif tm >= clock.clock(11, 15) and tm <= clock.clock(12, 50):
        webbrowser.open(t.teachers["casu_ioan"])
        exit()

    elif tm >= clock.clock(12, 55) and tm <= clock.clock(14, 30):
        webbrowser.open(t.teachers["zaharia_claudia"])
        exit()

    elif tm >= clock.clock(16, 15) and tm <= clock.clock(17, 50):
        webbrowser.open(t.teachers["ivan_oana"])
        exit()

    else:
        main_window.noclass()     