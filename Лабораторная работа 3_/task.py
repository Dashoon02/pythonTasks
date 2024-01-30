class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    # метод __str__ выполняет одинаковую функцию для всех трех классов - выводит название книги и автора,
    # поэтому оставляем его реализацию только в базовом классе, а дочерние классы унаследуют
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        """Устанавливает название книги."""
        self.name = name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self.author

    @author.setter
    def author(self, author: str) -> None:
        """Устанавливает автора книги."""
        self.author = author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    # печатная книга обладает дополительными свойствами по сравнению с обычной, поэnому перегружаем метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц печатной книги."""
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """Устанавливает количество страниц печатной книги."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    # аудио книга обладает дополительными свойствами по сравнению с обычной, поэnому перегружаем метод __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.duration!r})"

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудио книги."""
        return self.duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """Устанавливает продолжительность аудио книги."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудио книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")
        self.duration = duration
