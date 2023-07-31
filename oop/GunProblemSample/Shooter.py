class Shooter:
    def set_gun_by_name(self, name: str) -> None:
        Guns = {
            "Submachine Gun" : {"range":100, "power":10, "bullet size": 0.5},
            "Assault Rifle" : {"range":200, "power":20, "bullet size": 1},
            "Pistol" : {"range":80, "power":8, "bullet size": 0.5},
            "Shotgun" : {"range":50, "power":40, "bullet size": 4},
            "Sniper Rifle" : {"range":1000, "power":30, "bullet size": 3}}
        if name in list(Guns.keys()):
            self.selectedGun = Guns[name]
        else:
            Exception("the gun is not available")


    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        pass

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        pass


Submachine = Shooter()

Submachine.set_gun_by_name('Submachine gun')