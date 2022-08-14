from abc import (
    abstractmethod,
)

"""
To create a new page for the app:
  - Make a file here (newpage.py)
  - Add in in `picker.py` Factory class (self.current_pages)
  - Make an according folder in /templates and /static

  - Put the `Username` and `Password` fields in a <form method="post">
  - For the `Username` field give the atttribute `name="name"`
  - For the `Password` filed give the attribute of `name="password"`
  - ^^ The last 2 steps are there because Flask is set to look for those
       2 fields in the html and log the Username and Password.
"""

class IPage:
    @abstractmethod
    def __init__(self) -> None:
        self._page = ...

    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def __repr__(self) -> str: ...

    @abstractmethod
    def __hash__(self) -> int: ...

    @abstractmethod
    def create(self) -> str: ...
