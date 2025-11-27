def reverse_string(s: str) -> str:
    return s[::-1]

def to_upper(s: str) -> str:
    return s.upper()

def to_lower(s: str) -> str:
    return s.lower()

def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")