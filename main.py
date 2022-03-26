# import
import time
import threading
from pynput.keyboard import Controller, Listener, KeyCode

# assign stop and start key
start_key = KeyCode(char='q')


class PlayGame(threading.Thread):  # PlayGame class extends Thread
    def __init__(self):
        super(PlayGame, self).__init__()
        self.running = False
        self.program_running = True

    def start_playing(self):
        self.running = True

    def stop_playing(self):
        self.running = False

    def exit(self):
        self.stop_playing()
        self.program_running = False

    def moveBegin(self):  # code for snake game
        t = 0.179  # number of tiles moving
        keyboard.type('d')
        time.sleep(t * 6)
        keyboard.type('w')
        time.sleep(t * 4)
        while True:
            keyboard.type('a')
            time.sleep(t * 9)
            keyboard.type('s')
            time.sleep(t * 8)
            keyboard.type('d')
            for i in range(4):
                self.loop(t)
            time.sleep(t)  # quick turns require smaller time frame
            keyboard.type('w')
            time.sleep(t * 8)

    def loop(self, t): # code for the loop portion
        time.sleep(t)
        keyboard.type('w')
        time.sleep(t * 7)
        keyboard.type('d')
        time.sleep(t)
        keyboard.type('s')
        time.sleep(t * 7)
        keyboard.type('d')

    def run(self):
        while self.program_running:
            while self.running:
                self.moveBegin()
            time.sleep(1)


keyboard = Controller()
click_thread = PlayGame()
click_thread.start()


def on_press(key):
    if key == start_key:
        if click_thread.running:
            click_thread.stop_playing()
        else:
            click_thread.start_playing()


with Listener(on_press=on_press) as listener:
    listener.join()
