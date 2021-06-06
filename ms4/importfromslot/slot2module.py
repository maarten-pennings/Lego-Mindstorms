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

