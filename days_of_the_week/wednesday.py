import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

def wednesday():
    tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

    if tm >= clock.clock(7, 55) and tm <= clock.clock(9, 30):
        webbrowser.open(t.teachers["biris_larisa"])
        exit()

    elif tm >= clock.clock(11, 15) and tm <= clock.clock(12, 50):
        webbrowser.open(t.teachers["biris_larisa"])
        exit()

    elif tm >= clock.clock(14, 35) and tm <= clock.clock(16, 10):
        webbrowser.open(t.teachers["bonchis_cosmin"])
        exit()

    else:
        main_window.noclass()     