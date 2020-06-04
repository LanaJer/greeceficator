
def greeceficator(text: str):
    """Перевод с русского на греческий."""
    lower_vowels = {
        'а': 'α',
        'о': 'ω',
        'э': 'αι',
        'и': 'οι',
        'у': 'ου',
        'я': 'για',
    }
    caps_vowels = {k.capitalize(): v.capitalize() for k, v in lower_vowels.items()}

    substitutions = {**lower_vowels, **caps_vowels}  # объединяет два словаря

    for key, value in substitutions.items():
        text = text.replace(key, value)

    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    text = 'Яблоко висит на ветке. Кэб приехал в Лондон.'
    text = greeceficator(text)
    print(text)
