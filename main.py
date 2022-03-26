# import
import time
import threading
from pynput.keyboard import Controller, Listener, KeyCode

# assign stop and start key
start_stop_key = KeyCode(char='q')
exit_key = KeyCode(char='e')


class PlayGame(threading.Thread): # PlayGame class extends Thread
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

    def moveBegin(self): # code for snake game
        keyboard.type('d')
        time.sleep(0.55)
        keyboard.type('w')
        time.sleep(0.37)
        counter = 0
        while True: 
            keyboard.type('a')
            time.sleep(0.79)
            keyboard.type('s')
            time.sleep(0.72)
            keyboard.type('d')
            for i in range(4):
                self.loop()
            time.sleep(0.08)
            keyboard.type('w')
            time.sleep(0.791)
            time.sleep(counter)
            counter += 0.0005

    def loop(self): # code for the loop portion
        time.sleep(0.08)
        keyboard.type('w')
        time.sleep(0.6584)
        keyboard.type('d')
        time.sleep(0.08)
        keyboard.type('s')
        time.sleep(0.658035)
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
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_playing()
        else:
            click_thread.start_playing()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
