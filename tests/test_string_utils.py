from src.string_utils import reverse_string, to_upper, to_lower, count_vowels
def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_to_upper():
    assert to_upper("hello") == "HELLO"

def test_to_lower():
    assert to_lower("HELLO") == "hello"

def test_count_vowels():
    assert count_vowels("hello") == 2