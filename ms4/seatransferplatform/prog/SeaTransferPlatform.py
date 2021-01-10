import hub

rollcorrection  = 5 # Compensate for 0 position not being O
pitchcorrection = 5 # Compensate for 0 position not being O
pitchmotor= hub.port.E
rollmotor= hub.port.F

# Normalizes PWM values. For positive values
#  - clips values close to 0 to 0
#  - clips small values to a minimum PWM value that makes the motor move
#  - clips large values to a maximum value allowed for PWM
def normalize(val) :
    if val < -3 :
        val -= 25
        if val<-100 : val=-100
    elif val > +3 :
        val += 25
        if val>+100 : val=+100
    else : val = 0
    return int(val)

def rolllevel():
    roll1= hub.motion.accelerometer()[1]/10 # approx ship roll in degrees (port down is positive)
    roll2= rollmotor.motor.get()[2] - rollcorrection # approx platform roll in degrees
    duty = normalize( (roll1 - roll2) * 0.6 )
    rollmotor.pwm(duty)

def pitchlevel():
    pitch1= hub.motion.accelerometer()[0]/10 # approx ship pitch in degrees (back up is positive)
    pitch2= pitchcorrection - pitchmotor.motor.get()[2] # approx platform pitch in degrees
    duty = normalize( (pitch2 - pitch1) * 0.8 )
    pitchmotor.pwm(duty)

def main():
    hub.sound.beep(440, 200)
    print("SeaTransferPlatform")
    hub.sound.beep(880, 200)
    while True:
        roll = rolllevel()
        pitch = pitchlevel()

main()
