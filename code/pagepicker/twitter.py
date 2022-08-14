from .abcpage import IPage

class Twitter(IPage):
    def __init__(self) -> None:
        self._page = 'twitter'

    def __str__(self) -> str:
        return f"{self._page.title()}"

    def __repr__(self) -> str:
        return f"{self._page.title()}"

    def __hash__(self) -> int:
        return hash(self._page)

    def create(self) -> str:
        return self._page
