def generate_frame(word_list):
    width = max(len(word) for word in word_list)
    yield '*' * (width + 4)
    for word in word_list:
        yield '* {:<{}} *'.format(word, width)
    yield '*' * (width + 4)


def word_frame(word_list):
    for line in generate_frame(word_list):
        print(line)


word_frame(["Hello", "World", "in", "a", "frame"])


def test_generate_frame():
    assert list(generate_frame(["The", "cow", "jumped", "over", "the", "moon"])) == ["**********", "* The    *", "* cow    *", "* jumped *", "* over   *", "* the    *", "* moon   *", "**********"]
