# Radar car

## Introduction

This car has a "radar" (ultrasonic distance sensor).
It drives straight, until it sees an obstacle close by.
Then it stops driving, it uses it sensor to see if either left or right has the most free space.
It makes a turn that way, and continues to drive straight again.

There is one more peculiarity: this car only makes "exact" 90 degree turns (using the built-in yaw sensor).
When driving straight, it also uses the yaw sensor to keep it direction.

Here is a [short video](https://youtu.be/--oO_Eg1EDk) with a close-up of the car.

Here is a [long video](https://youtu.be/2BKyWezTPEI) with a top-view of the driving area.


## Steps

**Step 01** Mount brackets on radar motor, ...
![step 1](steps/step01.jpg)

**Step 02** ... add drive motors ...
![step 2](steps/step02.jpg)

**Step 03** and add the wheels.
![step 3](steps/step03.jpg)

**Step 04** Put pegs in the hub ...
![step 4](steps/step04.jpg)

**Step 05** and mount the hub on top of the motors.
![step 5](steps/step05.jpg)

**Step 06** Turn the car up side down ...
![step 6](steps/step06.jpg)

**Step 07** ... and tidy the cables using the clip (left drive motor in A, right drive motor in B, radar motor in C) ...
![step 7](steps/step07.jpg)

**Step 08** ... optionally using a beam to secure the cables.
![step 8](steps/step08.jpg)

**Step 09** A sub assembly for the castor wheel
![step 9](steps/step09.jpg)

**Step 10** ... assembled ...
![step 10](steps/step10.jpg)

**Step 11** and mounted at the bottom.
![step 11](steps/step11.jpg)

**Step 12** Turn the car upside again for the radar motor. It needs to be in zero position.
![step 12](steps/step12.jpg)

**Step 13** Brackets for the sensor ...
![step 13](steps/step13.jpg)

**Step 14** ... and mounted on the motor (cable in port F).
![step 14](steps/step14.jpg)

**Step 15** Finished result.
![step 15](steps/step15.jpg)


## Software

In the directory [prog](prog) you find the [file](prog/radarcar.lms) that you can open in the mindstorms app.

This program is writte in Python. For the reader's convenience I have included the [Python source](prog/radarcar.py). I hope to keep them in sync!

(end)
