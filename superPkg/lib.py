from art import *


def type_it(text=None):
    if type(text) == list:
        print(type(text), text)
        org_art = text2art(str(' '.join(text)), font='random')
        print(org_art)
    else:
        print(type(text), text)
        example_art = text2art('Type something!', font='random')
        print(example_art)


if __name__ == "__main__":
    type_it()
