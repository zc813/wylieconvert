import sys
from wylieconvert import batch_convert

# command line wrapper to wylieconvert/batch_convert

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
