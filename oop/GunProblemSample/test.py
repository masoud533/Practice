Guns = {
            "Submachine Gun" : {"range":100, "power":10, "bullet size": 0.5},
            "Assault Rifle" : {"range":200, "power":20, "bullet size": 1},
            "Pistol" : {"range":80, "power":8, "bullet size": 0.5},
            "Shotgun" : {"range":50, "power":40, "bullet size": 4},
            "Sniper Rifle" : {"range":1000, "power":30, "bullet size": 3}}

print("Submachine gun" in list(Guns.keys()))
print(Guns["Submachine Gun"])