import re

from greeceficator_ru import greeceficator_russian
from greecificator_en import greeceficator_english


def greeceficator_all_langs(text: str):
    text = greeceficator_russian(text)
    text = greeceficator_english(text)
    # Replace '?' at the end of a sentence with ';'
    text = re.sub(r'\?(?=\s*$)', ';', text)
    # Replace sigma at the end of words or before punctuation with the correct end sigma
    text = re.sub(r'σ(?=\s|;|$)', 'ς', text)
    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    print(greeceficator_all_langs('проверка связи'))
    print(greeceficator_all_langs('Hi how are you Sergios?'))
