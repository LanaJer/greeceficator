from string import punctuation

from utils import find_with_context, replace_first


ANY_LETTER_GR = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψω'
ANY_LETTER_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
ANY_LETTER = ANY_LETTER_RU + ANY_LETTER_GR
NO_LETTER = ' \t\n\r\x0b\x0c' + punctuation  # все варианты пробелов и все символы пунктуации
ANY = ''


def greeceficator_vowels(text: str):
    """Транслитерация гласных букв с русского на греческий."""
    lower_vowels = {
        'а': 'α',
        'о': 'ω',
        'э': 'ε',
        'и': 'οι',
        'у': 'ου',
        'я': 'για',
        #'ю':'υ',
        'ю': 'γιου',
        'ё': 'γιο',
    }
    caps_vowels = {k.capitalize(): v.capitalize() for k, v in lower_vowels.items()}

    substitutions = {**lower_vowels, **caps_vowels}  # объединяет два словаря

    for key, value in sorted(substitutions.items(), reverse=True, key=get_key_len):
        text = text.replace(key, value)

    return text

def get_key_len(x):
    """Возвращает длину ключа."""
    return len(x[0])


def greeceficator_consonants(text: str):
    """Транслитерация согласных букв с русского на греческий."""
    lower_consonants = [
        ('б', 'μπ', NO_LETTER, ANY),
        ('г', 'γκ', NO_LETTER, ANY),
        ('о', 'ο', NO_LETTER, ANY),
        ('ди', 'ντι', ANY, NO_LETTER),  # Τζον Κένεντι
        ('енне', 'ενε', ANY_LETTER, ANY_LETTER),
        ('ене', 'ενε', ANY_LETTER, ANY_LETTER),
        ('оло', 'ολω', ANY_LETTER, ANY_LETTER),
        ('ожо', 'οζο', ANY_LETTER, ANY_LETTER),
        ('иси', 'ιση', ANY_LETTER, ANY_LETTER),
        ('иро', 'υρο', ANY_LETTER, ANY_LETTER),
        ('мп', 'μπ', ANY_LETTER, ANY_LETTER),
        ('мб', 'μπ', ANY_LETTER, ANY_LETTER),
        ('кс', 'ξ', ANY, ANY),
        ('пс', 'ψ', ANY, ANY),
        ('дз', 'τζ', ANY, ANY),
        ('дж', 'τζ', ANY, ANY),
        ('д', 'ντ', NO_LETTER, ANY),
        ('тф', 'θ', ANY, ANY),
        ('ъе', 'γι', ANY, ANY),
        ('нт', 'ντ', ANY_LETTER, ANY),
        ('нд', 'ντ', ANY_LETTER, ANY),
        ('нг', 'γκ', ANY_LETTER, ANY),
        ('аф', 'αυ', ANY, ANY),
        ('ни', 'νι', ANY, ANY),
        ('им', 'ημ', ANY, ANY),
        ('нг', 'γγ', ANY, ANY),
        ('нх', 'γχ', ANY, ANY),
        ('он', 'ον', ANY, ANY),
        ('в',  'β', ANY, ANY),
        ('г',  'γ', ANY, ANY),
        ('д',  'δ', ANY, ANY),
        ('з',  'ζ', ANY, ANY),
        ('к',  'κ', ANY, ANY),
        ('л',  'λ', ANY, ANY),
        ('м',  'μ', ANY, ANY),
        ('н',  'ν', ANY, ANY),
        ('п',  'π', ANY, ANY),
        ('р',  'ρ', ANY, ANY),
        ('с',  'σ', ANY, ANY),
        ('т',  'τ', ANY, ANY),
        ('ф',  'φ', ANY, ANY),
        ('х',  'χ', ANY, ANY),
        ('ч', 'τσ', ANY, ANY),
        ('ц', 'τζ', ANY, ANY),
    ]

    substitutions = []
    for row in lower_consonants:
        caps_row = (row[0].capitalize(), row[1].capitalize(), row[2], row[3])
        substitutions.append(row)
        substitutions.append(caps_row)

    for rus_char, greek_char, allowed_before, allowed_after in substitutions:

        index, char_before, char_after = find_with_context(text, rus_char)
        while index != -1:
            # Разрешен любой контекст
            if allowed_before == ANY and allowed_after == ANY:
                text = replace_first(text, rus_char, greek_char)
            # Ограничение по символам до
            elif char_before in allowed_before and allowed_after == ANY:
                text = replace_first(text, rus_char, greek_char)
            # Ограничение по символам после
            elif allowed_before == ANY and char_after in allowed_after:
                text = replace_first(text, rus_char, greek_char)
            # Ограничение по символам до и после
            elif char_before in allowed_before and char_after in allowed_after:
                text = replace_first(text, rus_char, greek_char)

            index, char_before, char_after = find_with_context(text, rus_char, skip_first=index+1)

    return text


# Add English letters to the ANY_LETTER constant
ANY_LETTER_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ANY_LETTER += ANY_LETTER_EN

# Define English to Greek transliteration rules
english_to_greek_vowels = {
    'a': 'α', 'e': 'ε', 'i': 'ι', 'o': 'ο', 'u': 'υ',
    'A': 'Α', 'E': 'Ε', 'I': 'Ι', 'O': 'Ο', 'U': 'Υ'
}

english_to_greek_consonants = [
    ('b', 'β', ANY, ANY), ('c', 'κ', ANY, ANY), ('d', 'δ', ANY, ANY),
    ('f', 'φ', ANY, ANY), ('g', 'γ', ANY, ANY), ('h', 'η', ANY, ANY),
    ('j', 'ζ', ANY, ANY), ('k', 'κ', ANY, ANY), ('l', 'λ', ANY, ANY),
    ('m', 'μ', ANY, ANY), ('n', 'ν', ANY, ANY), ('p', 'π', ANY, ANY),
    ('q', 'κ', ANY, ANY), ('r', 'ρ', ANY, ANY), ('s', 'σ', ANY, ANY),
    ('t', 'τ', ANY, ANY), ('v', 'β', ANY, ANY), ('w', 'ω', ANY, ANY),
    ('x', 'ξ', ANY, ANY), ('y', 'υ', ANY, ANY), ('z', 'ζ', ANY, ANY),
    ('B', 'Β', ANY, ANY), ('C', 'Κ', ANY, ANY), ('D', 'Δ', ANY, ANY),
    ('F', 'Φ', ANY, ANY), ('G', 'Γ', ANY, ANY), ('H', 'Η', ANY, ANY),
    ('J', 'Ζ', ANY, ANY), ('K', 'Κ', ANY, ANY), ('L', 'Λ', ANY, ANY),
    ('M', 'Μ', ANY, ANY), ('N', 'Ν', ANY, ANY), ('P', 'Π', ANY, ANY),
    ('Q', 'Κ', ANY, ANY), ('R', 'Ρ', ANY, ANY), ('S', 'Σ', ANY, ANY),
    ('T', 'Τ', ANY, ANY), ('V', 'Β', ANY, ANY), ('W', 'Ω', ANY, ANY),
    ('X', 'Ξ', ANY, ANY), ('Y', 'Υ', ANY, ANY), ('Z', 'Ζ', ANY, ANY)
]

# Modify the existing functions or create new ones to include these rules
def greeceficator_english(text: str):
    # Apply vowel transliteration
    for en_char, gr_char in english_to_greek_vowels.items():
        text = text.replace(en_char, gr_char)
    
    # Apply consonant transliteration
    for en_char, gr_char, allowed_before, allowed_after in english_to_greek_consonants:
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
               index, char_before, char_after = find_with_context(text, en_char)
    return text


def greeceficator_all_langs(text: str):
    text = greeceficator_consonants(text)
    text = greeceficator_vowels(text)
    text = greeceficator_english(text)
    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон. Бурундук съел бомбу. Джон Кеннеди'
    text = greeceficator_all_langs(text)
    print(text)
