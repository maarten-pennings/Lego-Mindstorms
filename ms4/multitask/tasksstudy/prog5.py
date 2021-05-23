#!/usr/bin/python
import time

print("prog5 - globals")

class Timer():
    def __init__(self):
        """Creates a Timer and resets it."""
        self.reset()
    def now(self):
        """Returns the time in seconds since the timer was last reset."""
        return time.time() - self.sec0
    def reset(self,target=0):
        """Resets the timer (to `target` seconds)."""
        self.sec0 = time.time()+target

def wait(sec):
    t = Timer()
    while t.now() < sec :
        yield

# Seconds since startup - used for logging
clock = Timer()

led_a = 0  
def led_a_main(onsec, offsec) :
    global led_a
    while True:
        led_a = 1
        yield from wait(onsec)
        led_a = 0
        yield from wait(offsec)

led_b = 0  
def led_b_main(onsec, offsec) :
    global led_b
    while True:
        led_b = 1
        yield from wait(onsec)
        led_b = 0
        yield from wait(offsec)

def log_main():
    while True:
        print( f"  {clock.now():4.1f}: {led_a} {led_b}" )
        yield from wait(0.3)
        
task_a = led_a_main(2,5)
task_b = led_b_main(5,7)
task_c = log_main()

for _ in range(250_000_00):
    next(task_a)
    next(task_b)
    next(task_c)


# prog5 - globals
#    0.0: 1 1
#    0.3: 1 1
#    0.6: 1 1
#    0.9: 1 1
#    1.3: 1 1
#    1.6: 1 1
#    1.9: 1 1
#    2.2: 0 1
#    2.5: 0 1
#    2.8: 0 1
#    3.1: 0 1
#    3.4: 0 1
#    3.7: 0 1
#    4.0: 0 1
#    4.3: 0 1
#    4.6: 0 1
#    4.9: 0 1
#    5.3: 0 0
#    5.6: 0 0
#    5.9: 0 0
#    6.2: 0 0
#    6.5: 0 0
#    6.8: 0 0
#    7.1: 1 0
#    7.5: 1 0
#    7.8: 1 0
#    8.1: 1 0
#    8.4: 1 0
#    8.7: 1 0
#    9.0: 1 0
#    9.3: 0 0
#    9.6: 0 0
#    9.9: 0 0
#   10.2: 0 0
#   10.6: 0 0
#   10.9: 0 0
#   11.2: 0 0
#   11.5: 0 0
#   11.8: 0 0
#   12.1: 0 1
#   12.4: 0 1
#   12.7: 0 1
#   13.0: 0 1
#   13.4: 0 1
#   13.7: 0 1
#   14.0: 0 1
#   14.3: 1 1
#   14.6: 1 1
#   14.9: 1 1
#   15.2: 1 1
#   15.5: 1 1
#   15.8: 1 1
#   16.2: 0 1
#   16.5: 0 1
#   16.8: 0 1
#   17.1: 0 0
#   17.4: 0 0
#   17.7: 0 0
#   18.0: 0 0

