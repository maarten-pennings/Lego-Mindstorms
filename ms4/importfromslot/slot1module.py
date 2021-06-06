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
