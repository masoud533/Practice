class Shooter:
    def __init__(self) -> None:
        self.selectedGun = None
        self.selectedBullet = None
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
            raise Exception("the gun is not available")


    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        Bullets = {
            0.5: {"size":0.5, "dmage":1, "count":10},
            1.0: {"size":1, "dmage":1.5, "count":10},
            3.0: {"size":3, "dmage":3, "count":10},
            4.0: {"size":4, "dmage":2, "count":10}}
        if self.selectedGun == None:
            raise Exception("please select your gun first!")
        elif self.selectedGun['bullet size'] != size:
            raise Exception("Please pay attention to the selected bullet size!")
        elif size not in list(Bullets.keys()):
            raise Exception("we don't have this bullet")
        elif Bullets[size]["count"] - count <= -1:
            raise Exception("We don't have enough bullets")
        else:
            self.selectedBullet = Bullets[size]
            Bullets[size]["count"] -= Bullets[size]["count"] - count 
    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        if self.selectedGun['range'] < target_distance:
            return 0
        else:
           return self.selectedGun["power"] * self.selectedBullet["dmage"]