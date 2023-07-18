from collections.abc import Iterable
from typing import cast

from beartype import beartype
from bs4 import BeautifulSoup, Tag
from utilities.more_itertools import one


@beartype
def parse(markup: str, /) -> list[str]:
    soup = BeautifulSoup(markup=markup, features="xml")
    body = one(cast(Iterable[Tag], soup.find_all(name="body")))
    return sorted(tag.attrs["title"] for tag in body.find_all(name="outline"))
