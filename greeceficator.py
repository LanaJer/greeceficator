from utils import find_with_context, replace_first

ANY_LETTER = 'αβγδεζηθικλμνξοπρςστυφχψω'
NO_LETTER = ' \n'
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
    lower_consonants = {
        'мп': (ANY_LETTER, 'μπ', ANY_LETTER),
        'мб': (ANY_LETTER, 'μπ', ANY_LETTER),
        'б': (NO_LETTER, 'μπ', ANY),
        'в': (ANY,  'β', ANY),
        'г': (ANY,  'γ', ANY),
        'д': (ANY,  'δ', ANY),
        'з': (ANY,  'ζ', ANY),
        'тф': (ANY,  'θ', ANY),
        'к': (ANY, 'κ', ANY),
        'л': (ANY, 'λ', ANY),
        'м': (ANY, 'μ', ANY),
        'н': (ANY, 'ν', ANY),
        'кс': (ANY, 'ξ', ANY),
        'п': (ANY, 'π', ANY),
        'р': (ANY, 'ρ', ANY),
        'с': (ANY, 'σ', ANY),
        'т': (ANY, 'τ', ANY),
        'ф': (ANY, 'φ', ANY),
        'х': (ANY, 'χ', ANY),
        'пс': (ANY, 'ψ', ANY),
    }
    # caps_consonants = {k.capitalize(): v[1].capitalize() for k, v in lower_consonants.items()}

    substitutions = {**lower_consonants}  # объединяет два словаря

    for key, values in substitutions.items():
        before, replace, after = values

        index, char_before, char_after = find_with_context(text, key)
        while index != -1:

            if before == ANY and after == ANY:
                text = replace_first(text, key, replace)
            else:
                break

            index, char_before, char_after = find_with_context(text, key)

    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон. б'
    text = greeceficator_vowels(text)
    text = greeceficator_consonants(text)
    print(text)
