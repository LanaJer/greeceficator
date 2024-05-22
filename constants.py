from string import punctuation

ANY_LETTER_GR = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψω'
ANY_LETTER_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
ANY_LETTER_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ANY_LETTER = ANY_LETTER_RU + ANY_LETTER_GR + ANY_LETTER_EN
NO_LETTER = ' \t\n\r\x0b\x0c' + punctuation  # all possible whitespace characters and punctuation
ANY = ''
