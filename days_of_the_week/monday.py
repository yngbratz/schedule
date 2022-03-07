import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

def monday():
    tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

    if tm >= clock.clock(7, 55) and tm <= clock.clock(9, 30):
        webbrowser.open(t.teachers["popovici_dan"])
        exit()

    elif tm >= clock.clock(9, 35) and tm <= clock.clock(11, 10):
        webbrowser.open(t.teachers["popovici_dan"])
        exit()
    
    elif tm >= clock.clock(11, 15) and tm <= clock.clock(12, 50):
        webbrowser.open(t.teachers["bonchis_cosmin"])
        exit()

    else:
        main_window.noclass()     