#!/usr/bin/python
import time

print("prog3 - time")

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

# Seconds since startup - used for logging
clock = Timer()

# The main function for a cooperative task (voluntarily yielding). 
# Implements an infinite loop, which increments a local counter every `sec` seconds and logs under label `lbl`.
def inc_main(lbl="label",sec=1) :
    t = Timer()
    t.reset(-sec) # Fire now
    n = 0
    while True:
        if t.now() >= sec :
            t.reset()
            print( f"  {int(clock.now())}: {lbl}={n}" )
            n += 1
        yield

task_a = inc_main("a",2)
task_b = inc_main("b",3)

for _ in range(500_000_00):
    next(task_a)
    next(task_b)


# prog3 - time
#   0: a=0
#   0: b=0
#   2: a=1
#   3: b=1
#   4: a=2
#   6: b=2
#   6: a=3
#   8: a=4
#   9: b=3
#   10: a=5
#   12: b=4
#   12: a=6
#   14: a=7
#   15: b=5
#   16: a=8
#   18: b=6
#   18: a=9
#   20: a=10
#   21: b=7
#   22: a=11
