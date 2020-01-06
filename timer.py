import time as t
from _thread import start_new_thread
    
class GameClock(object):
    
    def __init__(self, name):
        self.name = name
        print(self.name)
        self.time = 15
        start_new_thread(self.timer_thread(1), (1,))

    def timer_thread(self, x):
        print("timer_thread: ", x)
        while self.time > 0:
            print(self.time)
            t.sleep(1)
            self.time -= 1
        print("timer ended.")
        
GameClock("New Game")