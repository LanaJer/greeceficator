# Add English letters to the ANY_LETTER constant
import re

from constants import ANY, NO_LETTER
from utils import replace_first, find_with_context


english_to_greek_vowels_lower = {
    'ow': 'αυ',
    'a': 'α',
    'e': 'ε',
    'i': 'ι',
    'o': 'ο',
    'u': 'υ',
}
english_to_greek_vowels = {**english_to_greek_vowels_lower,
                           **{k.capitalize(): v.capitalize() for k, v in english_to_greek_vowels_lower.items()}}

english_to_greek_consonants_lower = [
    ('ee', 'οι', ANY, ANY),
    ('b', 'μπ', ANY, ANY),
    ('c', 'κ', ANY, ANY),
    ('d', 'ντ', ANY, ANY),
    ('w', 'ου', ANY, ANY),
    ('f', 'φ', ANY, ANY),
    ('g', 'γ', ANY, ANY),
    ('h', 'χ', ANY, ANY),
    ('j', 'ζ', ANY, ANY),
    ('k', 'κ', ANY, ANY),
    ('l', 'λ', ANY, ANY),
    ('m', 'μ', ANY, ANY),
    ('n', 'ν', ANY, ANY),
    ('p', 'π', ANY, ANY),
    ('q', 'κ', ANY, ANY),
    ('r', 'ρ', ANY, ANY),
    ('s', 'σ', ANY, ANY),
    ('t', 'τ', ANY, ANY),
    ('v', 'β', ANY, ANY),
    ('x', 'ξ', ANY, ANY),
    ('y', 'υ', ANY, ANY),
    ('z', 'ζ', ANY, ANY),
]
substitutions = []
for row in english_to_greek_consonants_lower:
    caps_row = (row[0].capitalize(), row[1].capitalize(), row[2], row[3])
    substitutions.append(row)
    substitutions.append(caps_row)


def greeceficator_english(text: str):
    # Specific replacement for 'hi' at the beginning of words
    text = re.sub(r'\bHi', 'Χαϊ', text)
    text = re.sub(r'\bhi', 'χαϊ', text, flags=re.IGNORECASE)

    # Direct replacement for 'oo'
    text = re.sub(r'oo', 'ου', text, flags=re.IGNORECASE)

    # Contextual replacements for 'ch'
    text = re.sub(r'ch\b', 'χ', text, flags=re.IGNORECASE)  # 'ch' at the end of words (like in 'loch')
    text = re.sub(r'ch', 'τσ', text, flags=re.IGNORECASE)  # Default 'ch' to 'τσ' for common cases like 'church'

    # Contextual replacements for 'c', 'g', 'th', 'ch', 'ph', 'sh', 'y', 'x'
    text = re.sub(r'c(?=[iey])', 'σ', text, flags=re.IGNORECASE)
    text = re.sub(r'c', 'κ', text, flags=re.IGNORECASE)
    text = re.sub(r'gio', 'γιο', text, flags=re.IGNORECASE)
    text = re.sub(r'g(?=[iey])', 'τζ', text, flags=re.IGNORECASE)
    text = re.sub(r'g', 'γ', text, flags=re.IGNORECASE)
    text = re.sub(r'th(?=[^aeiou])', 'θ', text, flags=re.IGNORECASE)
    text = re.sub(r'th', 'δ', text, flags=re.IGNORECASE)
    text = re.sub(r'ch', 'κ', text, flags=re.IGNORECASE)
    text = re.sub(r'ph', 'φ', text, flags=re.IGNORECASE)
    text = re.sub(r'sh', 'σ', text, flags=re.IGNORECASE)
    text = re.sub(r'(?<=\b)y', 'γι', text, flags=re.IGNORECASE)
    text = re.sub(r'y', 'υ', text, flags=re.IGNORECASE)
    text = re.sub(r'x', 'ξ', text, flags=re.IGNORECASE)

    # Apply vowel transliteration
    for en_char, gr_char in english_to_greek_vowels.items():
        text = text.replace(en_char, gr_char)

    # Apply consonant transliteration
    for en_char, gr_char, allowed_before, allowed_after in substitutions:
        index, char_before, char_after = find_with_context(text, en_char)
        while index != -1:
            if allowed_before == ANY and allowed_after == ANY:
                text = replace_first(text, en_char, gr_char)
            elif char_before in allowed_before and allowed_after == ANY:
                text = replace_first(text, en_char, gr_char)
            elif allowed_before == ANY and char_after in allowed_after:
                text = replace_first(text, en_char, gr_char)
            elif char_before in allowed_before and char_after in allowed_after:
                text = replace_first(text, en_char, gr_char)
            index, char_before, char_after = find_with_context(text, en_char, skip_first=index + 1)
    return text
