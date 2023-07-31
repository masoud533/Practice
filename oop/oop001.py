class Cars:
    # def __init__(self) -> None:
    #     pass
    
    def __init__(self,CarCompany: str, CarModel: str):
        self.CarComoany = CarCompany
        self.CarModel = CarModel


Benz = Cars()

print(type(Benz))