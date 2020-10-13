# Lego NXT
Hints, tips, and tricks for the LEGO NXT Mindstorms robotics system.


## Links
- [8527 retail 1.0](https://www.lego.com/biassets/bi/4520729.pdf)
- [8547 retail 2.0](https://www.lego.com/biassets/bi/4589647.pdf)
- [Hints by Coert Vonk](https://coertvonk.com/family/school/inquiries/lego-mindstorms-nxt-g-6107)




## The Lego NXT-G IDE

NXT-G is the IDE (integrated development environment) that comes with Lego Mindstorms NXT.
It does have its quirks; this chapter has some tips.

First tip: ctrl-drag to duplicate a block.
![](images/duplicate-block.png)

A not so convenient feature: blocks are auto selected.
![](images/auto-block-select.png)

Autoselection of blocks makes selecting wires harder. Tip: double click the wire.
![](images/select-wire.png)

If a wire is selected, a press on [Delete] deletes the whole tree. Tip: click the input port to delete just the branch.
![](images/delete-wire-branch.png)

Want to make some space on the beam? Just drag a technic pin. If you hoover to long before clicking, it _branches_ the beam instead of making place (see next tip).
This dragging also works to remove space.
![](images/drag-for-space.png)

Branching a bea, is very subtle. First hoover over the branch point until it "highlights" (very subtle). Then drag towards a new block that you placed before.
![](images/drag-for-beam.png)


Some hotkeys:
- 1, 2, 3: selects the "common palette", the "complete palette" and the "custom palette"
- ArrowLeft, ArrowRight, ArrowUp, ArrowDown, PgUp, PgDn, home, end: pans the paper
- Holding CTRL and SHIFT down, the mouse changes into a hand; it grabs the "paper" for panning.
- ^B build (?)
- ^D (build and) download
- ^R (build, download and) run
- ^I NXT window


## Blocks 

### Integer math

NXT 1.0 uses integer math, but NXT 2.0 uses floating point. However the _Integer Math_ block is also installed but not published in the LEGO IDE.
To add the Integer Math Block, create an empty file `Numeric Operations.txt` in the `Data` directory in

`C:\Program Files (x86)\LEGO Software\LEGO MINDSTORMS NXT\engine\EditorVIs\BlockRegistry\`**`Data\Numeric Operations.txt`**

By the way, all installed blocks can be found here `C:\Program Files (x86)\LEGO Software\LEGO MINDSTORMS NXT\engine\vi.lib\LEGO\Blocks`.

Found this tip See [here](http://linearactuator.blogspot.com/2009/08/interger-blocks-in-nxt-g-20.html).


### Div and mod

One of the math operations I'm missing is `mod`. So I made my own My Block called `divmod`: 
it computes the mod and the div: 21 div 4 = 5 and 21 mod 4 = 1.

This My Block uses the Integer Math block above, as can be seen in the diagram below.

![divmod](images/divmod.png)

Download the [code](My%20Blocks/divmod.rbt).

### Sinus (half period).

For fancy "rocking" motor movement, a sinus is useful. Unlike EV3, NXT-G doesn't provide that function.
The indian mathematician Bhaskara I devised a relatively simple 
[formula](https://en.wikipedia.org/wiki/Bhaskara_I%27s_sine_approximation_formula) to approximate 
the first half period of the sinus function.

This formula is accurate to about 0.2% on the range 0<=x<=180.

|   x  | sin1h(x) |  sin(x) |  error |
|-----:|---------:|--------:|-------:|
|   0  |   0.000  |  0.000  |  0.000 |
|   5  |   0.088  |  0.087  | -0.001 |
|  10  |   0.175  |  0.174  | -0.002 |
|  15  |   0.260  |  0.259  | -0.002 |
|  20  |   0.343  |  0.342  | -0.001 |
|  25  |   0.423  |  0.423  | -0.001 |
|  30  |   0.500  |  0.500  |  0.000 |
|  35  |   0.573  |  0.574  | +0.001 |
|  40  |   0.642  |  0.643  | +0.001 |
|  45  |   0.706  |  0.707  | +0.001 |
|  50  |   0.765  |  0.766  | +0.001 |
|  55  |   0.818  |  0.819  | +0.001 |
|  60  |   0.865  |  0.866  | +0.001 |
|  65  |   0.905  |  0.906  | +0.001 |
|  70  |   0.939  |  0.940  | +0.001 |
|  75  |   0.966  |  0.966  | +0.000 |
|  80  |   0.985  |  0.985  | +0.000 |
|  85  |   0.996  |  0.996  | +0.000 |
|  90  |   1.000  |  1.000  |  0.000 |
|  95  |   0.996  |  0.996  | +0.000 |
| 100  |   0.985  |  0.985  | +0.000 |
| 105  |   0.966  |  0.966  | +0.000 |
| 110  |   0.939  |  0.940  | +0.001 |
| 115  |   0.905  |  0.906  | +0.001 |
| 120  |   0.865  |  0.866  | +0.001 |
| 125  |   0.818  |  0.819  | +0.001 |
| 130  |   0.765  |  0.766  | +0.001 |
| 135  |   0.706  |  0.707  | +0.001 |
| 140  |   0.642  |  0.643  | +0.001 |
| 145  |   0.573  |  0.574  | +0.001 |
| 150  |   0.500  |  0.500  |  0.000 |
| 155  |   0.423  |  0.423  | -0.001 |
| 160  |   0.343  |  0.342  | -0.001 |
| 165  |   0.260  |  0.259  | -0.002 |
| 170  |   0.175  |  0.174  | -0.002 |
| 175  |   0.088  |  0.087  | -0.001 |
| 180  |   0.000  |  0.000  |  0.000 |


I converted this formula to a My Block with the following diagram.

![sin1h(x)](images/sin1h(x).png)

Download the [code](My%20Blocks/sin1h(1).rbt).


### Sinus

The `sin1h(x)` is only accurate on the range 0..180. To make it periodic, I used the `divmod` from above.

![sin(x)](images/sin(x).png)

Download the [code](My%20Blocks/sin1h.rbt).


### Sinus application: test

To test the sinus, I wrote the following program; it draws
[Lissajous](https://en.wikipedia.org/wiki/Lissajous_curve) figures.

![Lissajous](images/lissajous.png)

This is an example output

![Lissajous](images/lissajous.jpg)

Download the [code](Progs/lissajous.rbt).


### Sinus application: motor control

The real application of the sinus block is "swinging" motion, e.g. wind shield wipers, swing, etc.
See [AntonsMindstorms](https://antonsmindstorms.com/2019/01/24/how-to-program-two-synchronised-ev3-motors/) for an explanation.

In a nutshell: there are two tasks. 
One task uses an continuously increasing timer as argument of the sinus function. The result (after multiplying with an amplitude constant) is the target angle of the wiper.
The second task is a P(ID) controller: it computes the error between the actual motor angle and the current target, and uses a proportional control for the power of the motor.

![wiper](images/wiper.png)

Download the [code](Progs/wiper.rbt).


### Sinus application: synchronized motors

A key aspect of the timer-target setup, is that a second motor can be incorporated - meaning that the two motors run in sync!

That is demoed by this parent pushing its child on a swing [swing](https://www.youtube.com/watch?v=0GbMUhZlRqk).

Download the [code](Progs/swing.rbt).


### Create your own blocks
Never tried it, but it seems you can make your own block using [labview](ftp://ftp.ni.com/evaluation/mindstorms/NXT_Creating_MINDSTORMS_Blocks.pdf).




## Firmware problems

### Firmware versions

My NXT brick (Settings > NXT Version) reports
- FW 1.31
- AVR 1.01
- BC4 1.01
- BUILD 1903101214

My NXT-G IDE reports
- v2.0.f4

See [lego](https://www.lego.com/en-us/themes/mindstorms/downloads) for the latest firmware or the IDE.


### Resetting the NXT
If the running icon stops spinning, the NXT has frozen and you must reset it. Follow these steps to reset the NXT:
1. Make sure that the NXT is turned on.
2. Press the reset button that is located on the back of your NXT in the Technic hole in the upper left corner. 
3. If you press the reset button for more than 4 seconds, you will need to update the firmware.

### Clicking brick
The NXT firmware has either been deleted or is corrupty. But the brick and its bootloader is still working.
See [here](http://www.legoengineering.com/clicking-brick-syndrome/) for details.

In some cases you have a driver problem.
1. Open device manager and find under `Ports (COM & LPT)` the `Bossa Program Port` driver and select `Update driver`.
2. Via `Browse my computer for driver software` then `Let me pick from a list...` find `LEGO MINDSTORMS NXT` driver instead. 
3. Then it is possible to connect to the NXT and update firmware.

Found this tip [here](https://home.et.utwente.nl/slootenvanf/2016/04/15/lego-firmware/). Here is a procedure from [Lego service desk](https://bricks.stackexchange.com/questions/2624/nxt-brick-will-not-update-firmware).

(end)
