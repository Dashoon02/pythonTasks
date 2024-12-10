if __name__ == "__main__":
    class SocialNetwork:
        """ Базовый класс социальных сетей. """

        def __init__(self, login: str, password: str):
            self.login = login
            self.password = password

        def __str__(self):
            return f"Логин {self.login}. Пароль {self.password}"

        def __repr__(self):
            return f"{self.__class__.__name__}(login={self.login!r}, password={self.password!r})"

        @property
        def login(self) -> str:
            """Возвращает логин пользователя."""
            return self.login

        @login.setter
        def login(self, login: str) -> None:
            """Устанавливает логин пользователя."""
            self.login = login

        @property
        def password(self) -> str:
            """Возвращает пароль пользователя."""
            return self.password

        @password.setter
        def password(self, password: str) -> None:
            """Устанавливает пароль пользователя."""
            self.password = password


    class VK(SocialNetwork):
        """ Дочерний класс VK."""
        def __init__(self, login: str, author: str, music: dict):
            super().__init__(login, author)
            self.music = music

        # не все социальные сети могут иметь музыку, а VK может, поэтому перегружаем метод __repr__
        def __repr__(self):
            return f"{self.__class__.__name__}(login={self.login!r}, password={self.password!r}, music={self.music!r})"

        @property
        def music(self) -> int:
            """Возвращает музыку аккаунта."""
            return self.music

        @music.setter
        def music(self, music: dict) -> None:
            """Записывает музыку аккаунта."""
            if not isinstance(music, dict):
                raise TypeError("Музыка должна быть записана в формате dict")


    class Facebook(SocialNetwork):
        """ Дочерний класс Facebook."""
        def __init__(self, login: str, password: str, country: str):
            super().__init__(login, password)
            self.country = country

        # Facebookу принципиально знать страну в отличии от других социальных сетей, поэnому перегружаем метод __repr__
        def __repr__(self):
            return f"{self.__class__.__name__}(login={self.login!r}, password={self.password!r}, country={self.country!r})"

        @property
        def country(self) -> str:
            """Возвращает страну пользователя."""
            return self.country

        @country.setter
        def country(self, country: str) -> None:
            """Записывает страну пользователя."""
            if not isinstance(country, str):
                raise TypeError("Страна должна быть типа str")
            if country == "Russia":
                raise TypeError("Доступ пользователям из России закрыт.")


    pass
