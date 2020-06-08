
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
        'б': 'β',
        'в': 'β',
        'г': 'γ',
        'д': 'δ',
        'з': 'ζ',
        'тф': 'θ',
        'к':'κ',
        'л':'λ',
        'м':'μ',
        'н':'ν',
        'кс':'ξ',
        'п':'π',
        'р':'ρ',
        'с':'σ',
        'т':'τ',
        'ф':'φ',
        'х':'χ',
        'пс':'ψ',
    }
    caps_consonants = {k.capitalize(): v.capitalize() for k, v in lower_consonants.items()}

    substitutions = {**lower_consonants, **caps_consonants}  # объединяет два словаря

    for key, value in sorted(substitutions.items(), reverse=True, key=get_key_len):
        text = text.replace(key, value)
    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон. Тф'
    text = greeceficator_vowels(text)
    text = greeceficator_consonants(text)
    print(text)
