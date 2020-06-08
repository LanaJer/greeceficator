def find_with_context(text: str, search: str):
    """Возвращает индекс, символ до и символ после найденного."""
    index = text.find(search)
    if index == -1:
        return index, '', ''
    char_before = text[index - 1]
    char_after = text[index + len(search)]
    return index, char_before, char_after


def replace_first(text: str, search: str, replace: str):
    """Заменяет первое вхождение. """
    index_start = text.find(search)
    index_end = index_start + len(search)
    text = text[:index_start] + replace + text[index_end:]
    return text


if __name__ == '__main__':
    # text = 'Яблоко висит на ветке. Кэб приехал в Лондон. Тф'
    # print(find_with_context(text, 'ppp'))
    text = 'Яблоко висит на ветке. Яблоко висит на ветке. Кэб приехал в Лондон. Тф'
    print(replace_first(text, 'висит', 'сидит'))
