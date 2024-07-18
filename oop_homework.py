class Car:
    def __init__(self, made_by: str, brand: str, fuel_per_km: float, year_of_manufacture: int = 2020):
        self.made_by = made_by.title()
        self.brand = brand.title()
        self.fuel_per_km = fuel_per_km
        self.year_of_manufacture = year_of_manufacture
        self.car_mileage = 0

    def __str__(self) -> str:
        return f"{self.brand}"

    __repr__ = __str__


mercedes_benz_c_class = Car(made_by="Mercedes-Benz", brand="mercedes", fuel_per_km=1.69)
bwm_5_series = Car(made_by="BMW AG", brand="BWM", fuel_per_km=2.035, year_of_manufacture=2010)
bwm_5_series.car_mileage = 300
print(mercedes_benz_c_class.__dict__)
print(bwm_5_series.__dict__)
