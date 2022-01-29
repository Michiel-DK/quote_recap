from quote.lib import get_quote

def test_type():
    assert type(get_quote()) == str