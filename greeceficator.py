from greeceficator_ru import greeceficator_russian
from greecificator_en import greeceficator_english


def greeceficator_all_langs(text: str):
    text = greeceficator_russian(text)
    text = greeceficator_english(text)
    return text


if __name__ == '__main__':
    # text = input('Please enter smth: ')
    print(greeceficator_all_langs('проверка связи'))
    print(greeceficator_all_langs('hi how are you'))
