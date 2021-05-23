#!/usr/bin/python

print("prog1 - tick tock")

# The task function
def task_main(lbl="label",start=0) :
    counter = start
    while True:
        print( f"  {lbl} {counter}")
        counter += 1
        yield 

# Create the two tasks (with label and start value)
task_a = task_main("tick",0)
task_b = task_main("tock",100)

# Start the "kernel", let it run for 5 units
for _ in range(5):
    next(task_a)
    next(task_b)


# prog1 - tick tock
#   tick 0
#   tock 100
#   tick 1
#   tock 101
#   tick 2
#   tock 102
#   tick 3
#   tock 103
#   tick 4
#   tock 104
