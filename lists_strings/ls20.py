
def to_pig_latin(word: str):
    a = word[0].lower()
    if word[0].isupper():
        if len(word) > 1:
            b = word[1].upper()
            new_word = b + word[2:] + a + "ay"
        else:
            a = word[0].upper()
            new_word = word[1:] + a + "ay"
    else:
        new_word = word[1:] + a + "ay"
    return new_word


def translate_text_to_pig_latin(text: str):
    words = text.split()
    new_words = []
    for word in words:
        if '.' in word:
            new_word = to_pig_latin(word[:-1]) + '.'
        else:
            new_word = to_pig_latin(word)
        new_words.append(new_word)
    new_text = ' '.join(new_words)
    return new_text


def pig_latin_word(word: str):
    first_letter = word[0]
    is_cap = first_letter.isupper()
    new_word = "".join([word[1:], first_letter.lower(), "ay"])
    if is_cap:
        new_word = new_word.capitalize()
    return new_word


def test_translate_text_to_pig_latin():
    assert translate_text_to_pig_latin("The quick brown fox") == "Hetay uickqay rownbay oxfay"
    assert translate_text_to_pig_latin("Hi. My name is X") == "Ihay. Ymay amenay siay Xay"
    assert translate_text_to_pig_latin("I run good. I run real good.") == "Iay unray oodgay. Iay unray ealray oodgay."
