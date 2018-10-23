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


def batch_convert(mode, include_orig):
    # setting the folders
    in_path = Path('input')
    out_path = Path('output')
    in_path.mkdir(exist_ok=True)
    out_path.mkdir(exist_ok=True)

    if len(list(in_path.glob('*.txt'))) == 0:
        exit(print('There are no .txt files to convert'))

    # conversion
    to_convert = list(in_path.glob('*.txt'))
    args = []
    if mode == 'u2w':
        args.append('-u')
    if include_orig:
        args.append('-r')
        args.append('\n\t')

    current = os.getcwd()
    os.chdir('Lingua-BO-Wylie/bin/')
    for f in to_convert:
        in_file = str(Path.resolve(Path.cwd() / '..' / '..' / f))
        out_file = str(Path.resolve(Path.cwd() / '..' / '..' / str(out_path / f.name)))
        Popen(['perl', 'wylie.pl', '-r', '\n\t'] + args + [in_file, out_file])
    os.chdir(current)


if __name__ == '__main__':
    if 2 > len(sys.argv) > 3:
        print('requires the following:\n"u2w" for unicode2wylie\n"w2u" for wylie2unicode\n\noptional:'
              '\n"true" to include the original string')
    mode = sys.argv[1]
    include_orig = False

    if mode != 'u2w' and mode != 'w2u':
        print('argument should be:\n"u2w" for unicode2wylie\n"w2u" for wylie2unicode'
              '\n"true" to include the original string')
    else:
        if len(sys.argv) == 3 and sys.argv[2] == 'true':
            include_orig = True
        batch_convert(mode, include_orig=include_orig)
