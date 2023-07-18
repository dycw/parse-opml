from parse_opml import __version__


def test_main() -> None:
    assert isinstance(__version__, str)
