from abc import abstractclassmethod
from random import sample


class Temerature:
    def __init__(self, temp):
        self.__temperature = temp

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        self.__temperature = temp

    def __str__(self) -> str:
        return f'{round(self.temperature,2)}º{self.__class__.__name__[0].capitalize()}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.temperature})'

    def freezing(self) -> bool:
        return self.convert_to_celsius().temperature <= 0

    @abstractclassmethod
    def convert_to_fahrenheit(self):
        pass

    @abstractclassmethod
    def convert_to_celsius(self):
        pass

    @abstractclassmethod
    def convert_to_kelvin(self):
        pass


class Celsius(Temerature):
    def __init__(self, temp):
        super().__init__(temp)

    def convert_to_celsius(self):
        return self

    def convert_to_fahrenheit(self):
        return Farenheit(self.temperature * 9 / 5 + 32)

    def convert_to_kelvin(self):
        return Kelvin(self.temperature + 273.16)


class Farenheit(Temerature):
    def __init__(self, temp):
        super().__init__(temp)

    def convert_to_fahrenheit(self):
        return self

    def convert_to_celsius(self):
        return Celsius(self.temperature - 32 * 5 / 9)

    def convert_to_kelvin(self):
        return Kelvin(self.temperature + 459.67 * 5 / 9)


class Kelvin(Temerature):
    def __init__(self, temp):
        super().__init__(temp)

    def convert_to_kelvin(self):
        return self

    def convert_to_celsius(self):
        return Celsius(self.temperature - 273.16)

    def convert_to_fahrenheit(self):
        return Farenheit(self.temperature * 9 / 5 - 459.67)


def print_temp_list(l, name, ony_frozen=False):
    print(f"{name}:")
    for t in l:
        if ony_frozen and t.freezing():
            print(t, end="\t")
        elif t.freezing():
            print(f'{t} poniżej zera', end="\t\t")
        elif not ony_frozen:
            print(t, end="\t\t\t")

    print()


def main():
    temperatures = []
    temperatures += [Celsius(t) for t in sample(range(-100, 100), 4)]
    temperatures += [Farenheit(t) for t in sample(range(-50, 150), 4)]
    temperatures += [Kelvin(t) for t in sample(range(400), 4)]

    print_temp_list(temperatures, "Pierwotna lista:")

    all_Celsius = [t.convert_to_celsius() for t in temperatures]
    all_Farenheit = [t.convert_to_fahrenheit() for t in temperatures]
    all_Kelvin = [t.convert_to_kelvin() for t in temperatures]

    print_temp_list(all_Celsius, "All Celsius", True)
    print_temp_list(all_Farenheit, "All Farenheit", True)
    print_temp_list(all_Kelvin, "All Kelvin", True)


if __name__ == "__main__":
    main()
