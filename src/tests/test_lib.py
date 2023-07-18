from beartype import beartype
from utilities.git import get_repo_root

from parse_opml.lib import parse


@beartype
def test_parse() -> None:
    path = get_repo_root().joinpath("src", "tests", "assets", "overcast.opml")
    assert path.exists()
    with path.open(mode="r") as fh:
        markup = fh.read()
    feeds = parse(markup)
    assert len(feeds) == 88
    for title in ["TED Talks Daily", "Cosmique"]:
        assert any(feed.title == title for feed in feeds)
