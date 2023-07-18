from collections.abc import Iterable
from csv import writer
from dataclasses import astuple, dataclass, fields
from pathlib import Path
from typing import cast

from beartype import beartype
from bs4 import BeautifulSoup, Tag
from utilities.more_itertools import one


@beartype
@dataclass(frozen=True)
class Feed:
    type: str  # noqa: A003
    text: str
    title: str
    xml_url: str
    html_url: str


@beartype
def parse(markup: str, /) -> list[Feed]:
    soup = BeautifulSoup(markup=markup, features="xml")
    body = one(cast(Iterable[Tag], soup.find_all(name="body")))
    all_attrs = (tag.attrs for tag in body.find_all(name="outline"))
    feeds = (
        Feed(
            type=attrs["type"],
            text=attrs["text"],
            title=attrs["title"],
            xml_url=attrs["xmlUrl"],
            html_url=attrs["htmlUrl"],
        )
        for attrs in all_attrs
    )

    @beartype
    def key(feed: Feed, /) -> str:
        return feed.title

    return sorted(feeds, key=key)


@beartype
def convert(feeds: Iterable[Feed], path: Path, /) -> None:
    with path.open(mode="w") as fh:
        csv_writer = writer(fh)
        headers = [f.name for f in fields(Feed)]
        csv_writer.writerow(headers)
        for feed in feeds:
            csv_writer.writerow(astuple(feed))
