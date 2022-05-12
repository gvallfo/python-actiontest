'''
Test for the do_things module
'''
import pytest
import do_things


@pytest.fixture
def text():
    '''
    A text used in test
    '''
    return "Apa Boll Citron"


@pytest.fixture
def text_lower():
    '''
    The test text as lower case
    '''
    return "apa boll citron"


def test_format_some_text_to_lower_case(text, text_lower):
    '''
    Verify output from format_some_text_to_lower_case()
    '''
    formatted_text = do_things.format_some_text_to_lower_case(text)
    assert formatted_text == text_lower
