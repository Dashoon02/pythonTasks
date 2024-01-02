import doctest

# TODO Написать 3 класса с документацией и аннотацией типов
class Tree:
    def __init__(self, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")
        self.age: int = age
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной")
        self.height: float = height

    def grow(self, years: int) -> None:
        """
        Метод, описывающий рост дерева.

        :param years: Количество лет, на которое увеличится возраст дерева (целое число)
        :return: None

        >>> t = Tree(10, 5.0)
        >>> t.grow(5)
        >>> t.height
        6.5
        >>> t.age
        15
        """
        self.age += years
        self.height += years * 0.3  # Примерный прирост высоты за год

    def shed_leaves(self, season: str) -> bool:
        """
        Метод, описывающий процесс опадения листьев у дерева.

        :param season: Время года, когда начнется опадение листьев (строка)
        :return: Результат опадения листьев (логическое значение)

        >>> t = Tree(10, 5.0)
        >>> t.shed_leaves("autumn")
        True
        """
        if season.lower() == "autumn":
            return True
        else:
            return False


class Car:
    def __init__(self, brand: str, year: int):
        if year < 1886:  # Первый автомобиль был изготовлен в 1886 году
            raise ValueError("Год выпуска автомобиля должен быть не менее 1886")

        self.brand: str = brand
        self.year: int = year


    def start_engine(self) -> None:
        """
        Метод, описывающий запуск двигателя автомобиля.

        :return: None
        """
        print("Engine started")

    def drive(self, distance: float, speed: float) -> float:
        """
        Метод, описывающий поездку на автомобиле.

        :param distance: Пройденное расстояние (вещественное число)
        :param speed: Средняя скорость движения (вещественное число)
        :return: Время в пути (вещественное число)
        """
        if distance < 0:
            raise ValueError("Дистанция не может быть отрицательной")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        time = distance / speed
        return time
class Animal():
    def __init__(self, name: str, age: int, weight: float):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")

        self.name: str = name
        self.age: int = age
        self.weight: float = weight


    def make_sound(self) -> str:
        """
        Абстрактный метод, описывающий издание звука животным.

        :return: Звук, издаваемый животным (строка)
        """

    def move(self, distance: float) -> None:
        """
        Абстрактный метод, описывающий движение животного на заданное расстояние.

        :param distance: Расстояние, на которое животное должно переместиться (вещественное число)
        :return: None
        """

if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
