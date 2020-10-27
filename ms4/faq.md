# Lego Mindstorms Robot Inventor "Mindstorms 4" 51515 FAQ

This FAQ has been written from the perspective of using a _Windows PC_ as host, not e.g. a tablet.


## How to switch off the brick?
I opened the box, and one of the first things I did was to power on the brick.
However, I could not figure out how to switch it off.

You have the first download the "IDE" (next question) on your PC (probably MAC also works, but phone doesn't) and then
upgrade the Hub OS. Only then I was able to switch the hub off.

How? Keep the big button pressed, it gives three beeps, and then you can release.
In some cases (Python program running instead of a Word Block) I do not hear the three beeps.


## Where is the Lego software?
The booklet tells you to visit [https://www.lego.com/devicecheck](https://www.lego.com/devicecheck).
I skipped that, because I have a brand new PC and a brand new Android device.
But then I wondered where should I _download_ the Mindstorms software?

Well, go to [devicecheck](https://www.lego.com/devicecheck), select mindstorms,
and click on of the "stores" to download the app.

You might like to try the [Spike prime software](https://education.lego.com/en-us/downloads/spike-prime/software).
It seems identical, and it has support for the force sensor, whcih is missing in the Mindstorms app. Did not try.

## How to make a shortcut to the app on my Windows Desktop?
I don't like "apps" from the Windows store. They are special in all kind of ways.
For example how do you create a shortcut on your desktop?

Go to Start > Run (e.g. Windows-R) and enter `shell:AppsFolder`.
This pops up a folder with app, and you can drag a shortcut to e.g. your Desktop.

Found [here](https://winaero.com/desktop-shortcut-store-app-windows-10/).


## What are the technical specs of Mindstorms 4?
Lego has leaflets on [Spike prime](https://education.lego.com/en-us/support/spike-prime/technical-specifications), which
is largely the same.

- **hub**: 5x5 LEDs, 6 ports, Gyro, 3 buttons one with RGB LED, beeper, Bluetooth, USB, MicroPython
  **cpu:** 100MHz M4, 320 kB RAM, 1M FLASH; 32MB RAM extern
  **battery**:  2100 mAh @ 7.3 V  >500 cycles
- **color sensor**: 100 Hz sample rate,  color sensing (RGB/HSV), reflectivity sensing, ambient sensing, white led emission
- **distance sensor**: 100 Hz sample rate, range 50..2000 mm, resolution 1 mm, 4 LEDs for decoration
- **motor**: torque 0..18 Ncm, speed 0..185 RPM, current 110..800 mA;
  **rotation sensor**: 360 ticks per revolution, 3 degrees accuracy, 100 Hz sampling


## Which projects can I build?
Of course, there are the five robots that come with the box.
Building instructions are digital only, you can find them in the app via Help > Settings > Building instructions.
Or you can click the robot in the home screen, and go from there in smaller steps.
Do note that the robots come with add-ons, which are really great,
for example [charly drum master](https://youtu.be/EAHvnpIGu1U)
or [tricky chain reaction](https://youtu.be/szFxBSRUh7c?t=167)

If you like more, or simpler builds, you could have a look at [Spike prime instructions](https://education.lego.com/en-us/support/spike-prime/building-instructions)


## Where are my recent projects?
When you start the Lego Mindstorms Robot inventor app, you get a screen with pictures (links) to the 5 robots.
At first this is nice, but after a while you want to continue with your own projects.

You have to click PROJECTS at the bottom of the app's home screen.
Unfortunately, thw list of projects starts with the standard lego ones, and not with e.g. the most recent ones.
You have to scroll all the way down.

The Lego app is very limited in using _keys_. The DownArrow doesn't work. Fortunately PageDown does work.
So does the scroll wheel. The scroll bar itself is too thin to easily grab with the mouse. Grr.


## How should I name my projects?
Most projects end up with a name like `Project 17`, because the Lego app does not ask for a name.
By default it just numbers them, using the lowest free number.

You have to explicitly remember to press Save As (preferably right after you create a new project). Grr.


## How do I start a new project?
Want to start a new project? Press CODE at the bottom of the home screen. You get an empty new Word Block
program. Rather have a Python program? In the Word Block editor (top) create a new tab.
Or, in the home screen click File > New Project.

Now you are _asked_ for the type of project (Word Block or Python).

After creating the project I suggest to immediately rename with File > Save As.


## Where are my projects saved?
The lego app made a directory `C:\Users\maarten\Documents\LEGO MINDSTORMS` for my (Maarten's) projects.
If you Save As `xxx`, the file ends up there, as `xxx 1.lms`.

The extension probably refers to Lego MindStorms. The "space-one" suffix is automatically appended.
The next time you Save As a project and _type_ `xxx` it gets the name `xxx 2.lms` (note the `2`).
Non standard windows behavior. Grr.

You can however Save As and _select_ the existing `xxx 1.lms`.
That pops up an "are you sure you want to overwrite" dialogue.


## How to save my project?
There is no Save button.

It seems the project is saved constantly when you interact with it (clicking the tab is enough).
I see the time stamp change in the file explorer.

The only condition is that the project is non-empty, or that you did a Save As.
So, an empty project that is not renamed does not yet get saved.


## Can I "remote control" my robot?
A bit hidden feature in the Word Block IDE are the two icons on the right hand side.

The top one (Remote Control) allows you to create a "Remote Control" pane in the IDE, with _widgets_.
The widgets on the PC pane communicate via Bluetooth to the Hub.
On the hub they trigger events that can be used in your program.

Great feature! Missing are widgets that _output_ content; most _input_ events in you program.
For example a virtual LED would be nice, or a string box, or a string list (dare I say "console").

There is one serious drawback: the program [needs](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946#:~:text=Because%20Streaming,running) to execute in streaming mode (ie live connection to the PC).

The remote control is not present in Python - probably because it has no streaming mode.

![Remote Control](images/remotecontrol.png)


## Can I remote control my robot with a game controller?
At this moment in beta, there is the option to add support for game controllers (Sony, XBox).

Click the Block Extension button and then either enable the DualShock or XBox One controller.
New blocks will pop-up in your palette (left).

I assume the controllers send their "button presses" via bluetooth to the PC, the stream to the hub.
I don't have one so can not test.

There is one serious drawback: the program [needs](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946#:~:text=Because%20Streaming,running) to execute in streaming mode (ie live connection to the PC).

The remote control is not present in Python - probably because it has no streaming mode.

![game controller](images/btcontroller.png)


## How can I debug my Word Block program?
A bit hidden feature in the Word Block IDE are the two icons on the right hand side.

The bottom one (Show/Hide Monitor) allows you to show (hide) a pane with a live view of the variables.

Great feature! Not present in Python, but Python has a better feature: the console!
A downside is that the monitor updates periodically (timed), so you do not see all changes.

The monitor feature does work in "download mode", you  do not have to use "streaming mode". I did expect that...

![Monitor](images/monitor.png)


## How can I debug my Python program?
Python lacks the monitor feature. Bummer!
But it does have something better: a console.

You can just `print()` in the hub code, and the print result is send to the PC console.

![Console](images/console.png)

I have not yet found a way to `input()` - that is a pity.


## How to send my project to the Hub?
There are actually three ways to do that.

- The most straighforward way is to press the Play button.
  Your program is compiled, uploaded and run. if a program was running on the hub, it is stopped.
  Note that the Hub has 20 slots(0..19), the app calls them "storage positions".
  By default your program goes to slot 0, but if you click the slot select button, you can specify another one.

  If you open the Hub connection on the PC, and then select tab Programs,
  you see the slots with the names of the project they store. Plus the option to delete or reorder slots.

- Another way it to only download, not _run_: press the Download button in the slot selection pane.

- A special way to run is _streaming_ mode.
  It does not save the project in a slot. So code is lost after stopping the program.
  Python does not support streaming.

![Play](images/play.png)


## What is streaming?
I'm not entirely sure of all the details of [streaming mode](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946).

- The program you’re creating is not stored in a slot on the hub as is with download mode.
- Instead, the PC maintains a connection with the hub, and the instructions will stream to the hub as they are executed.
- You can make "live" changes in your program (see figure).
- Streaming is faster.
- Remote control (pane in Mindstorms app, or Game controller) requires streaming mode.
- Somehow, showing the monitor does not require streaming mode.
- Also, sound via PC does not require streaming mode.
- I don't know yet if e.g. the "weather" extension needs streaming.

![Streaming](images/streaming.png)


## Isn't streaming mode slow?
In streaming mode, the code is streamed from the PC to the hub, while the program is executed.
This sounds a bit like an interpreter, and thus it sounds slow.

It isn't. In fact, it is the other way around: streaming is nearly 1000x faster.
Disclaimer: my test program does not execute a balanced set of blocks, and that is an understatement.

I guess the reason for this is that in streaming mode, all the code is run on the PC, and only _actuator commands_ and _sensor reads_ are streamed to the hub.

![Speed comparison](images/speed.png)


## Is there help (API documentation) for Word Blocks?
Yes, sort off. If you press Settings in the home screen, or Help > Setting, you can pick _Help and Support_ and then
_Word block description_. This has a two or three lines of help per block.

It has a very bad document structure (hard to see sections), does not support copy and paste, and worst of all,
can not be opened while programming. Grr.

![Word block help](images/wordblockhelp.png)


## Is there help (API documentation) for Python?
The help for Python is found on the right had side in the Python editor.

It is better than the help for Word Blocks. Document structure is better but not good.
Does support copy and paste (although not for every piece of text).
Can be open during programming (pfeew).

![Python help](images/pythonhelp.png)


## How to stop my program?
Good question: if you program doesn't stop, the hub will not power down, so stopping is important.

In Word block, there is an explicit stop block.

![Stopping in Word block](images/wordblockstop.png)

In Python, I haven't found a good one yet. I did find `sys.exit(0)` (don't forget the `import sys`).
It does stop the program, but with a sort-of error.
You can see this in the console (red message), but also the center LED on the hub flashes red 3 times.

![Stopping in Python](images/pythonstop.png)


## How to update the hub firmware?
I see people talk about hub firmware updates, but the Mindstorms app does not have a feature for that - at least I couldn't find it. Maybe the Spike prime app allows explicit firmware updates (downgrades, alternatives...).

However, when lego releases a new version, you will get a message in the app. If you accept it the hub will be updated.
This updates the hub’s OS, not the user data (saved projects).


## What are the hotkeys?
I think lego did a bad job here. Many functions are not operatable by key.
Probably lego aims at touch screens.

Note #=shift, ^=ctrl, @=alt

Word blocks is horrible
  - ^Z for undo is working, but ^Y for redo isn't (it is available in bottom menu or right click menu)
  - @F4 stops aplication.
  - @F or @H (for file or help menu) is _not_ working.
  - Cut and paste (^C, ^V) is _not_ working. You can right-click and Duplicate, but this duplicates the whole stack.
  - I found no hotkey for Run or Download.
  - Cursor keys (panning) do nothing.

Python is better. But not due to Lego, but because they took a standard control for the editor.
It behaves much like [Microsoft Studio Code](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
  - ^C, ^V, ^X for copy, paste, cut.
  - ^Z, ^Y for undo, redo.
  - Cursor movement with arrow or page keys, optionally in combination with ^.
  - Select by pressing # while moving cursor.
  - ^F, ^H for find and replace (grr: the hub bar overlaps with the find bar).
  - **^#P issues a play**.
  - ^#D issues a download.
  - **There is no way to clear the console other than to restart the whole mindstorms app - grr**.
  - **You can only walk up (arrow-up, page-up) in the console, not down, and the scroll bar sucks - grr**.
  - Fancy line commenting: ^K^C add line comment, ^K^U delete line comment, ^/ toggle line comment.
  - #@A to toggle block comment.
  - Very fancy multi cursor (bit over the top) with @click, or ^#@ with cursor movement.
  - **There is no rich languages editing, ^SPC appears to work but it doesn't know the object, it just shows all occuring strings.**


## What software version is current?
What is "current"? 

At the moment of writing this answer (2020 oct 27):

- The IDE version is 4.0.4-dev.99999
- The Hub OS version is 2.1.4.10

This can be seen from a screenshot

![IDE and OS Version](images/version.png)


## Which Python is used?
Let's write a script for that! See screenshot.
- Micro Python 1.11.0
- on system 3.4.0

No idea how that relates to the Hub OS version.

![Python Version](images/pythonversion.png)


## Can I connect to REPL - interactive Python?
Yes you can ([instructbale](https://www.instructables.com/MicroPython-on-SPIKE-Prime/)).
The Python interpreter in the Hub has an interactive command shell that executes a so-called read-eval-print loop (REPL).
The Hub has two serial links, one over Bluetooth and one over USB. Both are enabled for REPL.

Connect the Hub to your PC either via Bluetooth, or, easier, a USB cable.
Right click on the Windows start button and select Device Manager, and fold open the _Ports (COM & LPT)_ section. It requires some experimentation (e.g unplug USB to see which port disappears) to determine which port(s) connect to the Hub. In my case it is COM4 (serial over the USB link) and COM5 (serial over Bluetooth).

![COM ports](images/com.png)

Next, we need a terminal program to send an receive commands over serial. I happen to use an oldy [realterm](https://realterm.sourceforge.io/), [putty](https://www.putty.org/) is popular.

Configure the COM port (115200/8/N/1), and connect.
The hub is running a program that spits out data, and this now floods the terminal.
Stop the program by sending a CTRL-C.
We get a prompt from `MicroPython v1.11-1139-gf7407e5a0 on 2020-06-19; LEGO Technic Large Hub with STM32F413xx`

![Connect](images/connect.png)


## What can I do in REPL - interactive Python?

A good start is the trusted `dir()` command.

```text
>>> dir()
['hub_runtime', 'gc', '__name__', 'micropython']
```

The `gc` object [controls the garbage collector](https://docs.micropython.org/en/latest/library/gc.html),
variable `__name__` holds the value `'__main__'`, and
object `micropython` helps in [access and control of the internals](https://docs.micropython.org/en/latest/library/micropython.html).
Our best candidate is `hub_runtime`.

If you want to know what such an object offers, use `dir` again (`dir(hub_runtime)`).
Even better, this REPL offers command completion with the TAB key.
For example, after type `hu`TAB, we get `hub_runtime`, if we then type `.`TAB we get

```text
>>> hub_runtime.
__class__       __name__        start           __file__
BT_VCP          Timer           USB_VCP         hub
init            LightMethods    LinegraphMonitorMethods
MotorMethods    MoveMethods     SoundMethods    WaitMethods
ProgramMethods  HubMethods      get_event_loop  register_ports
TIMER_PACE_HIGH                 error_handler   pop_force_reset
RTTimer         notify_gesture_event            RPCProtocol
system          ProgramRunner   HubUI           runtime
scratch         sensors         __connection_changed
>>> hub_runtime.
```

After some searching, we can get the current yaw via a call to the `position`.
We called twice, rotating the hub in between.
First number looks like the yaw.

```
>>> hub_runtime.hub.motion.position()
(25, -1, 0)
>>> hub_runtime.hub.motion.position()
(44, -1, 0)
>>>
```

The suggested `help()` command is _not_ very useful.

```text
>>> help()
Welcome to MicroPython!

For online help please visit http://micropython.org/help/.

Quick overview of commands for the board:
  hub.info()    -- print some general information
  hub.status()  -- print sensor data

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
  CTRL-F        -- on a blank line, enter filetransfer mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
>
```

The `hub.info()` does not work: `name 'hub' isn't defined` (we already knew that, `hub` was not listed by `dir`).
The CTRL commands seem a bit advanced now.
There is one good hint though: `help("modules")`.

```text
>>> help("modules")
__main__          math              uerrno            urandom
_onewire          micropython       uhashlib          ure
builtins          sys               uheapq            uselect
cmath             uarray            uio               ustruct
firmware          ubinascii         ujson             utime
gc                ucollections      umachine          utimeq
hub               uctypes           uos               uzlib
Plus any modules on the filesystem
```

This lists the module `hub`! Let's try to import it, and give the status command.

```text
>>> import hub
>>> hub.status()
{'gyroscope': (2, 8, 3), 'position': (51, 0, 0), 'accelerometer': (15, -8, 1026)
, 'port': {'C': [0, -2, 12, 0], 'D': [], 'B': [0, 2, 70, 0], 'E': [], 'A': [0, -
1, 168, 0], 'F': [14]}, 'display': '09000:09900:09990:09900:09000'}
>>> hub.sound.beep()
>>>
```

We see that we moved the robot a bit (yaw is now 51).
The `.`TAB trick made us find the beep command, which works!


## Which modules are available in Python?

The REPL help suggests to use the `hub` module.
However, the Lego app suggest to use `mindstorms.MSHub`.
And a `dir` of both shows they are different.
This is very confusing.

With the `help("modules")` we found the `hub` module.
But it also gave the hint `Plus any modules on the filesystem`.
And we see there is a module `uos` for [basic "operating system" services](https://docs.micropython.org/en/latest/library/uos.html).
This micro-OS includes a filesystem!

```text
>>> import uos
>>> uos.listdir('/')
['projects', 'runtime', 'system', '_api', 'commands', 'event_loop', 'mindstorms'
, 'programrunner', 'protocol', 'sounds', 'spike', 'ui', 'util', 'boot.py', 'hub_
runtime.mpy', 'main.py', 'version.py', '.runtime_hash', 'extra_files', '.extra_f
iles_hash', 'bt-lk1.dat', 'bt-lk2.dat', 'runtime.log']
>>> uos.listdir('/mindstorms')
['__init__.mpy', 'control.mpy', 'operator.mpy', 'util.mpy']
>>> print( open('/mindstorms/__init__.mpy','r').read() )
M uP
,mindstorms/__init__.py€apii€"large_technic_hub*T2
MSHubLargeTechnicHub4QcT
        Qc
>>>
```

Reading the file `__init__.mpy` is not very succseful.
And `mpy` file is "a binary container file format that holds precompiled code, and which can be imported like a normal .py module",
see [doucmentation](https://docs.micropython.org/en/latest/reference/mpyfiles.html#:~:text=a%20binary,module).

But its presence is important: we have a directory `mindstorms` with a file `__init__.[m]py`, and this means we have a package:
"The `__init__.py` files are required to make Python treat directories containing the file as packages.", see [documentation](https://docs.python.org/3/tutorial/modules.html#:~:text=The%20__init__.py,packages.). 

We even see the string `MSHub` in the `__init__.mpy`. Let's try to import and get the yaw.

```text
>>> from mindstorms import MSHub                                                
>>> h=MSHub()                                                                   
>>> h.motion_sensor.get_yaw_angle()                                             
50                                                                              
>>> h.motion_sensor.get_yaw_angle()                                             
62                                                                              
>>>
```





(end)
