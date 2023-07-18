from beartype import beartype
from utilities.git import get_repo_root

from parse_opml.lib import parse


@beartype
def test_parse() -> None:
    path = get_repo_root().joinpath("src", "tests", "assets", "overcast.opml")
    assert path.exists()
    with path.open(mode="r") as fh:
        markup = fh.read().strip("\n")
    contents = parse(markup)
    assert len(contents) == 88
    for title in ["TED Talks Daily", "Cosmique"]:
        assert title in contents
