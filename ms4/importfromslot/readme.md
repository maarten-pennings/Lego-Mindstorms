# Import from slot

Reusing one python program in another.

## Introduction

I read this interesting [post](https://www.facebook.com/story.php?story_fbid=538084377549405&id=100461371311710).

How does this work?

If you write a python program in the Lego IDE, and you upload and/or run it, it gets stored in a so-called slot.
What this means in practice is that the IDE generates a random id xxx, 
and saves your (pre-compiled) Python file under `/projects/xxx/__init__.mpy`.

It also updates the "index", that is a the file `/projects/.slots`.

As you might know, you can make one Python `mmm.py` with "library" functions 
and then use those functions in another Python file via an `import mmm`.

Can we import slotted Python file in another slotted Python file.
Yes, that is what the above post is about.

## Setup

We will write a library in slot 2 and a main program in slot 1.

### Library slot2module

First we write our library, unimaginatively called `slot2module`.
Open up the Lego IDE, create a Python module, paste the below code, and save it (e.g. under `slot2module`).

Here is the [py source](slot2module.py) or [lms source](slot2module.lms).

```python
# slot2module - Put this is slot 2
import hub, time

def beep(count=1) :
    for _ in range(count) :
        hub.sound.beep(freq=1000,time=25)
        time.sleep_ms(100)

def f2():
    print("running f2")
    hub.display.show( hub.Image("99099:90099:99000:90099:90099") )
    beep(2)

print("loaded slot2module")
hub.display.show( hub.Image("99999:90909:00000:99099:99099") )
beep(2)
time.sleep_ms(1000)
```

Run the module from **slot 2**. That is very important, because the "2" is what our main program will use later.

If you run this program, you should see

```text
loaded slot2module
```

hear _two_ beeps, and see an "m with two dots" on the hub display.

![m2](m2.jpg)

This module publishes the function `f2()` that we need in the main program. 

### Main program slot1module

The main program is very similar. In this case, save as `slot1module` and run it from **slot 1** 
(does not really matter, as long as it is not slot 2).

Here is the [py source](slot1module.py) or [lms source](slot1module.lms).

```python
# slot1module - Put this is slot 1
import hub, time, sys, util

def beep(count=1) :
    for _ in range(count) :
        hub.sound.beep(freq=1000,time=25)
        time.sleep_ms(100)

def import_from_slot(slot) :
    # sys.path is typically ['', '_slash_lib']
    # add /projects, this is persistent until hub is rebooted
    if '/projects' not in sys.path :
        sys.path.append('/projects')
    # Now import the module
    path = util.storage.get_path(slot) # './projects/40117'
    names = path.split('/') # ['.','projects','40117']
    name = names[-1] # '40117'
    return __import__(name)

print("loaded slot1module")
hub.display.show( hub.Image("99999:90909:00000:00990:009900") )
beep(1)
time.sleep_ms(1000)

m = import_from_slot(2)

m.f2()
```

This is the output


```text
loaded slot1module
loaded slot2module
running f2
```

We see `loaded slot1module`, hear one beep, and see an "m with one dots" on the hub display.
After one second, we see `loaded slot2module`, hear two beep, and see an "m with two dots" on the hub display.
Again one second later, we see `running f2`, hear two beep, and see an "f with two dots" on the hub display.

![m1](m1.jpg) ![m2](m2.jpg) ![f2](f2.jpg)

## Save file

An experiment that seems feasible, is that a python scripts saves a python script to the file system
(or must that be a mpy file - or can we create an mpy file on the PC)?

And another Python script imports that.

To do...

(end)

