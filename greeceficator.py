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
        ('д', 'ντ', NO_LETTER, ANY),
        ('б',  'μπ', NO_LETTER, ANY_LETTER),
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
    caps_consonants = [(x[0].capitalize(), x[1].capitalize(), x[2], x[3]) for x in lower_consonants]

    substitutions = [*caps_consonants, *lower_consonants]  # объединяет два списка

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
            else:
                break  # Нечего менять - завершаем while и переходим к следующей букве (цикл for)

            index, char_before, char_after = find_with_context(text, rus_char)

    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон. Бурундук съел бомбу.'
    text = greeceficator_vowels(text)
    text = greeceficator_consonants(text)
    print(text)
