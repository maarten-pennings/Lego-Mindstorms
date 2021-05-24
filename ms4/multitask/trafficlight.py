# trafficlight.py - demo of cooperative multi-tasking 
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds
from mindstorms.control import Timer

hub = MSHub()

print("Welcome to traffic light")
print("Pedestrian button is left button on hub")
while hub.left_button.was_pressed() :
    # presses are buffered, consume them all
    pass 

# This is the state for the pedestrian: "none" -> "waiting" -> "walking" -> "none"
pedestrian = "none" 

def wait(sec):
    t = Timer()
    while t.now() < sec :
        yield

def task_trafficlight() :
    global pedestrian
    while True:
        hub.status_light.on('red')
        if pedestrian=="none" : 
            # no pedestrian, short red
            yield from wait(4)
        else :
            # longer red, so pedestrian can walk
            yield from wait(2) # red but not yet walking
            pedestrian = "walking"; hub.light_matrix.show_image("STICKFIGURE")
            yield from wait(4)
            pedestrian = "none"; hub.light_matrix.show_image("NO")
            yield from wait(2) # no longer walking, still red
        hub.status_light.on('green')
        yield from wait(6)
        hub.status_light.on('yellow')
        yield from wait(2)

def task_pedestrian() :
    global pedestrian
    hub.light_matrix.show_image("NO")
    while True:
        if hub.left_button.was_pressed() :
            pedestrian = "waiting"
            while pedestrian=="waiting" :
                hub.speaker.beep(70,0.1)
                yield from wait(1)
            while pedestrian=="walking" :
                hub.speaker.beep(70,0.1)
                hub.speaker.beep(45,0.1)
                yield
            while hub.left_button.was_pressed() :
                # presses are buffered, consume them all
                yield
        yield

# Create the cooperative tasks
task_a = task_trafficlight()
task_b = task_pedestrian()

# Start the main loop
while True:
    next(task_a)
    next(task_b)
    # print(pedestrian)
    