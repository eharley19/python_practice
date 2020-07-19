def word_frame(word_list):
    width = max(len(word) for word in word_list)
    print('*' * (width + 4))
    for word in word_list:
        print('* {:<{}} *'.format(word, width))
    print('*' * (width + 4))


word_frame(["Hello", "World", "in", "a", "frame"])