#!/usr/bin/python
import time

print("prog4 - no break up")

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

# Implements an infinite loop, which switches on LED `lbl` for `onsec` seconds, 
# then switches it off for `offsec` seconds.
# This propagates the yields from the sub-generator `wait()` to the main loop.
def led_main(lbl, onsec, offsec) :
    while True:
        print( f"  {int(clock.now())}: {lbl} on" )
        yield from wait(onsec)
        print( f"  {int(clock.now())}: {lbl} off" )
        yield from wait(offsec)

        
task_a = led_main("a",2,5)
task_b = led_main("b",5,7)

for _ in range(500_000_00):
    next(task_a)
    next(task_b)


# prog4 - no break up
#   0: a on
#   0: b on
#   2: a off
#   5: b off
#   7: a on
#   9: a off
#   12: b on
#   14: a on
#   16: a off
#   17: b off
#   21: a on
#   23: a off
#   24: b on
