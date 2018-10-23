from subprocess import Popen, PIPE
import os
import sys
from pathlib import Path


def wylie2unicode(text, dir='Lingua-BO-Wylie'):
    current = os.getcwd()
    os.chdir(dir)
    out = Popen(['perl', 'wylie2unicode.pl', text], shell=False, stdout=PIPE)
    out = bytes.decode(out.communicate()[0])
    os.chdir(current)
    return out


def unicode2wylie(text, dir='Lingua-BO-Wylie'):
    current = os.getcwd()
    os.chdir(dir)
    out = Popen(['perl', '-CA', 'unicode2wylie.pl', text], shell=False, stdout=PIPE)
    out = bytes.decode(out.communicate()[0])
    os.chdir(current)
    return out


def batch_convert(mode='u2w'):
    # setting the folders
    in_path = Path('input')
    out_path = Path('output')
    in_path.mkdir(exist_ok=True)
    out_path.mkdir(exist_ok=True)

    if not list(in_path.glob('*.txt')):
        exit(print('There are no .txt files to convert'))

    # conversion
    to_convert = in_path.glob('*.txt')
    if mode == 'u2w':
        for f in to_convert:
            content = f.read_text(encoding='utf-8-sig')
            converted = unicode2wylie(content)
            new = out_path / f.name
            new.write_text(converted)
    elif mode == 'w2u':
        for f in to_convert:
            content = f.read_text(encoding='utf-8-sig')
            converted = wylie2unicode(content)
            new = out_path / f.name
            new.write_text(converted)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('requires a single argument:\n"u2w" for unicode2wylie\n"w2u" for wylie2unicode')
    mode = sys.argv[1]
    if mode is not 'u2w' and mode is not 'w2u':
        print('argument should be:\n"u2w" for unicode2wylie\n"w2u" for wylie2unicode')
    else:
        batch_convert(mode)
