import screen_brightness_control as sbc
import time
from threading import Timer

class Reminder:
    def __init__(self):
        self.NUM_BLINKS = 5
        self.REM_FREQ = 1
        self.display_num = 0
        self.waiting = False
        self.main()
    
    def individual_blink(self, freq=0.1):
        print("Toggling screen")
        sbc.set_brightness(0, display=self.display_num)
        time.sleep(freq)
        sbc.set_brightness(100, display=self.display_num)
        print("Done toggling")

    def blink_monitor(self):
        for i in range(self.NUM_BLINKS):
            self.individual_blink()
    
    def start_waiting(self):
        for i in range(self.REM_FREQ, 0, -1):
            print("%s second remaining" % i)
            time.sleep(1)
        self.blink_monitor()
        self.waiting = False

    def main(self):
        while(True):
            if not self.waiting:
                self.waiting = True
                self.start_waiting()
            else:
                continue

if __name__ == "__main__":
    Reminder()
