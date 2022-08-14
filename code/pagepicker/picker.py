#!/bin/env python3
import sys
import time
from .abcpage import IPage
from .google import Google
from .twitter import Twitter
from .facebook import Facebook
from .instagram import Instagram
from actions.actions import log_error
from actions.constants import theme_color


class Exit:
    def __repr__(self) -> str:
        return "Exit"

    @property
    def _page(self):
        print(theme_color("\nABORTING...\n"))
        time.sleep(1)
        sys.exit(0)


class PageFactory:
    def __init__(self) -> None:
        self.current_pages = [
            Exit(),
            Google(),
            Twitter(),
            Facebook(),
            Instagram(),
        ]

    def __getitem__(self, i: int):
        return self.current_pages[i]

    def pick(self, i: int) -> IPage:
        return self.current_pages[i]


@log_error
def page_picker() -> IPage:
    pages = PageFactory()
    for idx, page in enumerate(pages):
        print(theme_color(f"[{idx}]:\t{page}\n"))
    selection = int(input("Select a page by number: "))

    final_page = pages.pick(selection)
    print(theme_color(f"You selected: {final_page._page.title()}\n"))
    return final_page
