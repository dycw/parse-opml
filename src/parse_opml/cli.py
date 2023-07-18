from pathlib import Path

import click
from beartype import beartype
from click import argument, command

from parse_opml.lib import convert, parse


@command()
@argument(
    "path_opml",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
@argument("path_csv", type=click.Path(exists=False, path_type=Path))
@beartype
def main(*, path_opml: Path, path_csv: Path) -> None:
    with path_opml.open(mode="r") as fh:
        markup = fh.read()
    feeds = parse(markup)
    convert(feeds, path_csv)
