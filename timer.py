import time as t
from _thread import start_new_thread
from threading import Thread
    
class GameClock(object):
    
    def __init__(self, name):
        self.name = name
        print(t.time())
        self.time = 100
        Thread(target=self.timer_thread).start()

    def timer_thread(self):
        now = t.time()
        print(f'now: {t.time}')
        while self.time > 0:
            print(self.time)
            t.sleep(0.1)
            self.time -= 1
        print("timer ended.", t.time()-now)

def timer_thread():
    now = float(t.time())
    print('now: ', float(t.time()))
    x = 20
    while x > 0:
        print(x)
        t.sleep(0.1)
        x -= 1
    print("timer ended.", t.time()-now)     

GameClock("test")
GameClock("test2")
#start_new_thread(timer_thread, (20,))
#Thread(target=timer_thread).start()
#Thread(target=timer_thread).start()