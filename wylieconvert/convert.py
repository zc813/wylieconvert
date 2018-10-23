from subprocess import Popen, PIPE
import os


def wylie2unicode(text, dir='Lingua-BO-Wylie'):
    current = os.getcwd()
    os.chdir(dir)
    out = Popen(['perl', 'wylie2unicode.pl', text], shell=False, stdout=PIPE)
    out = bytes.decode(out.communicate()[0])
    os.chdir(current)
    return out


if __name__ == '__main__':
    wylie = 'bkra shis bde legs/'
    unicode = wylie2unicode(wylie)
    print(unicode)

