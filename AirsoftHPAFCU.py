fire = 0
fps = 0
rof = 0

def firing():
    settings = int(input("Type 1 to shoot \nType 2 to go back menu:"))
    if settings == 1:
        print(fire)
        print(fps)
        print(rof)
        firing()
    elif settings == 2:
        menu()
    else:
        print ("Wrong Input")
        firing()

def settings():
    setFIRE = int(input("Type 1 for safety, 2 for semi, 3 for auto: "))
    if setFIRE == 1:
        fire = "LOCKED"
        menu()
    elif setFIRE == 2:
        fire = "PEW"
        menu()
    elif setFIRE == 3:
        fire = "PEW PEW PEW"
        menu()
    else:
        print("Wrong Input")
        settings()


def df():
    psi = int(input("PSI: "))
    dwell = int(input("Dwell (1-15): "))
    if dwell > 15 or dwell <0:
        dwell = 0
        print ("Wrong input")
        df()
    else:
        rof = int(input("ROF (1-60)"))
        if rof > 30 or rof <0:
            rof = 0
            print ("Wrong input")
            df()
        else:
            fps = dwell + psi * 4
            menu()
    

def menu():
    print("1. To fire")
    print("2. To settings")
    print("3. Dwell/ROF")
    choose = int(input("Type number to select option:"))
    if choose == 1:
        firing()
    elif choose == 2:
        settings()
    elif choose == 3:
        df()
    else:
        print ("Wrong input")
        menu()

menu()