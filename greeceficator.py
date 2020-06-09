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
        'ю':'υ',
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
        ('б', 'μπ', NO_LETTER, ANY_LETTER),
        ('д', 'ντ', NO_LETTER, ANY),
        ('оло', 'ολω', ANY_LETTER, ANY_LETTER),
        ('ожо', 'οζο', ANY_LETTER, ANY_LETTER),
        ('иси', 'ιση', ANY_LETTER, ANY_LETTER),
        ('иро', 'υρο', ANY_LETTER, ANY_LETTER),
        ('мп', 'μπ', ANY_LETTER, ANY_LETTER),
        ('мб', 'μπ', ANY_LETTER, ANY_LETTER),
        ('кс', 'ξ', ANY, ANY),
        ('пс', 'ψ', ANY, ANY),
        ('дз', 'τζ', ANY, ANY),
        ('тф', 'θ', ANY, ANY),
        ('ъе', 'γι', ANY, ANY),
        ('нт', 'ντ', ANY, ANY),
        ('нд', 'ντ', ANY, ANY),
        ('аф', 'αυ', ANY, ANY),
        ('ни', 'νι', ANY, ANY),
        ('им', 'ημ', ANY, ANY),
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


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон. Бурундук съел бомбу. Пирожок'
    text = greeceficator_consonants(text)
    text = greeceficator_vowels(text)
    print(text)
