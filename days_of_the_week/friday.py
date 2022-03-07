import time
import webbrowser
import teachers as t
import clock
import gui.main_window as main_window

def friday():
    tm = clock.clock(time.localtime().tm_hour, time.localtime().tm_min)

    if tm >= clock.clock(12, 55) and tm <= clock.clock(14, 30):
        webbrowser.open(t.teachers["brandibur_oana_practica"])
        exit()

    else:
        main_window.noclass()