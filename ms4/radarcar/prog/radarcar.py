# Radar car - this car drives only north<->south or east<->west, when hitting a wall rotating to where is the most space.
from mindstorms import MSHub, Motor, MotorPair, DistanceSensor
import math
import sys

# Setup hardware
hub = MSHub()
mradar = Motor("C")
sradar = DistanceSensor("F")
mdrive = MotorPair("A", "B")

# Lights up 5x5 matrix. 
# Parameter `bits` is a 25 bits vector: a 1 switches on that led.
# Bit 24 is upper left, bit 0 is lower right.
def set_image(bits):
    hub.light_matrix.off()
    cur=1<<24
    for y in range(5):
        for x in range(5):
            if bits & cur : hub.light_matrix.set_pixel(x,y,100)
            cur >>= 1

# Emits 3 tone fancy beep
def beep():
    hub.speaker.beep(60, 0.1)
    hub.speaker.beep(70, 0.1)
    hub.speaker.beep(62, 0.1)

# Returns distance (in cm) from ultra sonic sensor `sradar`
# Takes 10 samples and averages. If distance is too far, returns 999.
def get_distance():
    numsamples = 10 # How many samples to avarage
    sumsamples = 0.0
    for i in range(numsamples):
        sample= sradar.get_distance_cm()
        if sample==None: sample=999 # Convert out-of-range to big number
        sumsamples += sample
    result = sumsamples / numsamples
    return result

# Rotates rader (mradar) to `angle` (0, 90, 270) and returns measured distance - using get_distance().
# Shows radar position also on 5x5 matrix.
def set_radar(angle):
    if angle==  0 : set_image( 0b_01110_00000_00100_00000_00000 )
    if angle== 90 : set_image( 0b_00000_00001_00101_00001_00000 )
    if angle==270 : set_image( 0b_00000_10000_10100_10000_00000 )
    correction = 10 # My motor has a 0-position that is 10 degrees off; correct yours here 
    mradar.run_to_position( angle+correction, direction="shortest path",speed=40)
    return get_distance()

# Swings radar to west (-90 deg, 270 deg, left) and east (90 deg, right).
# Returns either "WEST" or "EAST" depending which of the two has obstacle furthest away.
# Animates 5x5 matrix during swing.
# Leaves radar in position north (0 deg) and 5x5 matrix with arrow to new direction.
def best_direction() :
    d0   = set_radar(  0) # move to 270 and 90 always via 0, so that shortest path does not go via 180 (and radar hits car)
    d270 = set_radar(270)
    d0   = set_radar(  0)
    d90  = set_radar( 90)
    d0   = set_radar(  0) # leave NORTH as last so that the radar looks forward
    best= "EAST" if d90>d270 else "WEST"
    hub.light_matrix.show_image("ARROW_"+best[0] )
    return best

# Rotates the car on its place so that its yaw() becomes `target` (using P-control).
# When routine ends, drive motors are stopped and car faces direction `target`.
def rotate(target):
    ntarget = (180+target) % 360 - 180 # normalize target to be in -180..+180 range
    print("rotate: target=", target,"(", hub.motion_sensor.get_yaw_angle()," --> ",ntarget,")")
    kp = 0.1
    power0 = 20
    cont = True
    while cont:
        yaw = hub.motion_sensor.get_yaw_angle()
        error = ntarget - yaw
        if error > +180: error = -(error - 180)
        if error < -180: error = -(error + 180)
        control = kp * error
        power = int(math.copysign(power0,control)+control)
        cont = math.fabs(error)>4
        mdrive.start_tank_at_power(power,-power)
    mdrive.stop()

# Drives car until distance to obstacle is too low.
# Keeps yaw() to angle `target` (using P-controller).
# When routine end, drive motors are stopped and car faces near collision with obstacle in front.
def drive(target):
    ntarget = (180+target) % 360 - 180 # normalize target to be in -180..+180 range
    print("drive: target=", target,"(", hub.motion_sensor.get_yaw_angle()," --> ",ntarget,")")
    kp = 0.7
    power0 = 30
    while get_distance()>5 :
        yaw = hub.motion_sensor.get_yaw_angle()
        error = ntarget - yaw
        if error > +180: error = -(error - 180)
        if error < -180: error = -(error + 180)
        control = kp * error
        leftpower = int(power0+control)
        rightpower = int(power0-control)
        mdrive.start_tank_at_power(leftpower,rightpower)
    mdrive.stop()

# Begin
print("Radar car - python ", sys.version)
set_radar(0) # Set radar position to front facing (0 deg, north)
curdir = 0   # Set the current dir - relative to inital yaw())

while True :
    # Drive until to "close to wall"
    hub.light_matrix.show_image("ARROW_N") # north arrow
    hub.status_light.on("green") # green: driving
    drive(curdir)
    hub.status_light.on("red") # red: stopped
    beep()
    # Which turn to make
    best = best_direction() # east or west arrow
    if best=="EAST" : curdir= (curdir+90)%360
    if best=="WEST" : curdir= (curdir-90)%360
    print("Turn ",best)
    # Make turn
    rotate(curdir)
