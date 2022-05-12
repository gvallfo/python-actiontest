import pytest
import do_things


@pytest.fixture
def text():
    return "Apa Boll Citron"


@pytest.fixture
def text_lower():
    return "apa boll citron"


def test_format_some_text_to_lower_case(text, text_lower):
    formatted_text = do_things.format_some_text_to_lower_case(text)
    assert formatted_text == text_lower
