from datetime import datetime
from abc import ABC, abstractmethod


class CarBase(ABC):
    name = ""
    max_speed = 180
    """Простая модель автомобиля."""
    def __init__(self, year, color: str = "Черный"):
        """Инициализация атрибутов авто."""
        self.year = year
        self.color = color

    def get_info(self):
        print(f'Поздравляем с покупкой - {self.name}\n'
              f'Цвет авто - {self.color}\n'
              f'Максимальная скорость авто - {self.max_speed} км/ч'
              )

    @abstractmethod
    def open(self):
        print('Авто открыт!')

    @abstractmethod
    def running_engine(self):
        print("Машина заведена!")


class Audi(CarBase):
    name = "Audi A4 B5"
    year = "2000"
    color = "Синий"
    max_speed = 200
    odometer_reading = 259_000

    def open(self):
        print(f"Для тест-драйва -  {self.name}, нужно иметь водительское удостоверение")

    def running_engine(self):
        print(f"{self.name} - заведена.")

    def read_odometer(self):
        """Вывод пробега авто."""
        print(f'У этой машины - {self.odometer_reading} км пробега')

    def update_odometer(self, km):
        """Функция проверки скручивания счетчика одометра."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Скручивать пробег нельзя!')

    def increment_odometer(self, km):
        self.odometer_reading += km


class BMW(CarBase):
    name = "BMW E39"
    year = "2001"
    color = "Красный"
    max_speed = 250
    odometer_reading = 350_000

    def open(self):
        print(f"Для тест-драйва -  {self.name}, нужно иметь водительское удостоверение")

    def running_engine(self):
        print(f"{self.name} - заведена. ")

    def read_odometer(self):
        """Вывод пробега авто."""
        print(f'У этой машины - {self.odometer_reading} км пробега')

    def update_odometer(self, km):
        """Функция проверки скручивания счетчика одометра."""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Скручивать пробег нельзя!')

    def increment_odometer(self, km):
        self.odometer_reading += km

class Nissan:
    @staticmethod
    def info(model, date, color, probeg, coast):
        print(
            f"Марка авто: {model}\n"
            f"Год производства: {date}\n"
            f"Цвет: {color}\n"
            f"Пробег: {probeg}\n"
            f"Стоимость: {coast}"
        )

class Plane(ABC):
    """Представляем аспекты машины, специфические для самолета."""
    name = ""
    start_speed = 0
    max_speed = 100
    max_hight = 12000


    def __init__(self, company: str = ""):
        self.company = company

    def get_info(self):
        print(f"Модель самолета: {self.name}\n"
              f"Авиакомпания:{self.company}\n"
              f"Начальная скорость:{self.start_speed}\n"
              f"Максимальная скорость:{self.max_speed}\n"
              f"Максимальная высота:{self.max_hight}"
              )

    @abstractmethod
    def start(self):
        pass


class Boing(Plane):
    name = "Airbus"
    start_speed = 0
    max_speed = 300
    max_hight = 10000

    @classmethod
    def start(cls):
        return cls.max_speed



class F11(Plane):
    name = "F11"
    start_speed = 0
    max_speed = 500
    max_hight = 10000

    @classmethod
    def start(cls):
        return cls.max_speed

class SpaceX:
    def __init__(self, model, year: datetime):
        self.model = model
        self.year = year

    @staticmethod
    def info(model, date, color, probeg, coast,):
        print(
            f"Марка ракеты: {model}\n"
            f"Год производства: {date}\n"
            f"Цвет: {color}\n"
            f"Пробег: {probeg}\n"
            f"Стоимость: {coast}"
        )


car1 = Audi("2000", "Black")
car1.get_info()
car1.open()
car1.running_engine()
car1.read_odometer()
car1.update_odometer(260_000)
car1.read_odometer()
print()
car2 = BMW("2001", "Red")
car2.get_info()
car2.open()
car2.running_engine()
car2.update_odometer(200_000)
car2.read_odometer()
car2.increment_odometer(100)
car2.read_odometer()
print()
Nissan.info("Nissan Almera", "2000", "Black", "200_000", "$2000")
print()
plane1 = Boing("Belavia")
plane1.get_info()
print()
plane2 = F11("US Army")
plane2.get_info()
print()
SpaceX.info("SpaceX", "2022", "White", "0", "$1m")


