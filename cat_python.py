"""Basic cat in python - with extra emojis"""


def cat(*args, encoding=None):
    for fn in args:

        meow = b''
        f = open(fn, 'rb')
        try:
            meow += f.read()
        finally:
            f.close()

        if encoding:
            meow.decode(encoding)

        return meow


def onelinecat(*args):
    return b''.join(open(fn, 'rb').read() for fn in args)
