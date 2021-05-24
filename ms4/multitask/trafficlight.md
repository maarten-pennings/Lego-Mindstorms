# Traffic light

This is a demonstrator project, implementing a traffic light with pedestrian button, 
on Lego Mindstorms 4 Robot inventor, using generators with yield to implement cooperative multi-tasking.

## Introduction

The Python concepts behind this project can be found in two [studies](readme.md).

The Lego build is non-existing, the whole project is software-only using just the hub.

The status light on the hub is used as the traffic light for the cars.
Typically it is 4 seconds red, 6 seconds green, 2 seconds yellow and then repeats.

The led matrix on the hub is used as the light for the pedestrian.
Typically is shows a cross (for stop, red) or a stick figure (for walk, green).
But the pedestrian light never automatically goes "walk".

When a pedestrian wants to cross s/he has to press the request button (left arrow on hub).
After this, the traffic light will start a slow paced beeping ("waiting").
When the car cycle is completed, the request is honored.

Two seconds after the car light goes red, the pedestrian light goes walk/green.
Also the beeping becomes fast paced.
Four seconds later, the pedestrian light goes stop/red, and the beeping stops.
two seconds later, the car cycle restarts (with green).

See the traffic light in action on this [video](https://youtu.be/ViPouN8wFCM).

## Software

There is a global variable that indicates if there is a pedestrian.

```python
# This is the state for the pedestrian: "none" -> "waiting" -> "walking" -> "none"
pedestrian = "none" 
```

- `none` means no pedestrian, car traffic light cycling is going on.
- `waiting` means that pedestrian request button is pressed. Slow paced beeping. Waiting for car light to go red.
- `walking` means pedestrian is walking. Fast paced beeping. Car light is red.

The car cycle is implemented by this task.

```python
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
```

The pedestrian button is implemented by this task.

```python
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
        yield
```

The built-in `Timer` only accepts integer seconds.

As explained in [studies](readme.md), the `yield` is where the task switching takes place.

See the traffic light in action on this [video](https://youtu.be/ViPouN8wFCM).

The complete software is available as [lms](trafficlight.lms) file or as straight [python](trafficlight.py).

(end)