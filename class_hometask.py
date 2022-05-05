class Car():
    '''Простая модель автомобиля.'''
    def __init__(self, make, model, year, color):
        '''Инициализация атрибутов авто.'''
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer_reading = 0

    def get_name(self):
        '''Возвращает отформатированое описание авто.'''
        long_name = f'{self.make} {self.model} - {self.year} года. Цвет кузова - {self.color}'
        return long_name.title()

    def read_odometer(self):
        '''Вывод пробега авто.'''
        print(f'У этой машины - {self.odometer_reading} км пробега')

    def update_odometer(self, km):
        '''Функция проверки скручивания счетчика одометра.'''
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Скручивать пробег нельзя!')

    def increment_odometer(self, km):
        self.odometer_reading += km

    def get_range(self):
        '''Вывод приблизительного запаса хода авто с электрическим двигателем.'''
        if self.battery_size <= 80:
            range = 240
        elif self.battery_size >= 81:
            range = 300
        message = f'Приблизительный запас хода - {range} km, если батарея полностью заряжена'
        print(message)

class Nissan(Car):
    '''Ниссан'''
    def __init__(self, make, model, year, color ):
        '''Инициализируем атрибуты класса-родителя.'''
        super().__init__(make, model, year, color)
        self.battery_size = 70

    def fill_gas_tank(self):
        '''Тип авто'''
        print(f'Этот автомобиль электрический!')

    def describe_battery(self):
        '''Вывод мощности батареии электрического авто'''
        print(f'Мощность батареи - {self.battery_size} kWh')


class Honda(Car):
    def __init__(self, make, model, year, color ):
        '''Инициализируем атрибуты класса-родителя.'''
        super().__init__(make, model, year, color)
        self.battery_size = 100

    def fill_gas_tank(self):
        '''Тип авто'''
        V = 30
        print(f'Этот автомобиль гибридный!Обьем бака - {V} l')
        print(f'Мощность батареи - {self.battery_size} kWh')




class PlaneBoing(Car):
    '''Представляем аспекты машины, специфические для самолета.'''
    def __init__(self, make, model, year, color):
        '''Инициализируем атрибуты класса-родителя.'''
        super().__init__(make, model, year, color)
        self.start_speed = 0
        self.max_speed = 100
        self.max_hight = 12000



    def describe_speed_s(self):
        '''Описание скорости самолета в статитческом состоянии.'''
        print(f'Скрость самолета в статическом состоянии - {self.start_speed} km')

    def describe_speed_d(self):
        '''Описание скорости самолета в динамическом состоянии'''
        print(f'Скрость самолета в динамическом состоянии - {self.max_speed} km')

    def describe_max_hight(self):
        '''Описание на какой максимальной высоте может летать самолет'''
        print(f'Максимальная скорость самолета = {self.max_hight} m')

class F11(Car):
    def __init__(self, make, model, year, color):
        '''Инициализируем атрибуты класса-родителя.'''
        super().__init__(make, model, year, color)
        self.start_speed = 0
        self.max_speed = 180
        self.max_hight = 18000
        self.min_hight = 10000

    def describe_speed_s(self):
        '''Описание скорости самолета в статитческом состоянии.'''
        print(f'Скрость самолета в статическом состоянии - {self.start_speed} km')

    def describe_speed_d(self):
        '''Описание скорости самолета в динамическом состоянии'''
        print(f'Скрость самолета в динамическом состоянии - {self.max_speed} km')

    def describe_max_hight(self):
        '''Описание на какой максимальной высоте может летать самолет'''
        print(f'Максимальная высота самолета = {self.max_hight} m')

    def describe_min_hight(self):
        '''Описание на какой максимальной высоте может летать самолет'''
        print(f'Минимальная  высота самолета = {self.min_hight} m')

    def describe_mean_hight(self):
        mean_hight = (self.max_hight + self.min_hight)/2
        print(f'Среднее значение высоты самолета - {mean_hight} m')





my_car_1 = Car('Audi', 'B6', 2001, 'Белый')
print(my_car_1.get_name())
my_car_1.update_odometer(200_000)
my_car_1.read_odometer()
my_car_1.increment_odometer(100)
my_car_1.read_odometer()

nissan = Nissan('\nNissan', 'E', 2021, 'Черный')
print(nissan.get_name())
nissan.fill_gas_tank()
nissan.describe_battery()
nissan.get_range()

honda = Honda('\nHonda', 'Gybrid', 2010, 'Синий')
print(honda.get_name())
honda.fill_gas_tank()
honda.get_range()

boing432 = PlaneBoing('\nBoing', '432', 2005, 'Красно-синий')
print(boing432.get_name())
boing432.describe_speed_s()
boing432.describe_speed_d()
boing432.describe_max_hight()

f11 = F11('\nF11', 'M', 2019, 'Черный')
print(f11.get_name())
f11.describe_speed_s()
f11.describe_speed_d()
f11.describe_max_hight()
f11.describe_min_hight()
f11.describe_mean_hight()



