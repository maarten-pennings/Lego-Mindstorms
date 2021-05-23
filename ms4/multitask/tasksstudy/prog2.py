#!/usr/bin/python
import random

print("prog2 - writer reader")

queue = []

# The task function for the writer.
# A change of 1 in 100 to add 1 to 5 values to `queue`.
def task_writer() :
    val = 100
    while True:
        arrive = random.randrange(100)<1
        if arrive :
            count = random.randrange(1,6)
            yield
            print( f"  w: {count}" )
            for _ in range(count) :
                queue.append(val)
                val += 1
        yield 

# The task function for the reader.
def task_reader() :
    while True:
        while len(queue)>0 :
            elem = queue.pop(0)
            print( f"  r: {elem}" )
        yield 
        
# Create the two tasks (with label and start value).
task_w = task_writer()
task_r = task_reader()

# Start the "kernel", let it run for 100 units.
for _ in range(1000):
    next(task_w)
    next(task_r)


# prog2 - writer reader
#   w: 3
#   r: 100
#   r: 101
#   r: 102
#   w: 1
#   r: 103
#   w: 1
#   r: 104
#   w: 5
#   r: 105
#   r: 106
#   r: 107
#   r: 108
#   r: 109
#   w: 4
#   r: 110
#   r: 111
#   r: 112
#   r: 113
#   w: 2
#   r: 114
#   r: 115
