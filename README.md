# Convert to and from wylie with Python

This is a very thin wrapper on the Perl converter found on [THL website](http://www.thlib.org/cgi-bin/thl/lbow/wylie.pl).

The size limitation on the website(1Mb max) are lifted.

## Exposed functions

 - Within Python, `unicode2wylie(text)` and `wylie2unicode(text)` return the transcoded strings.
    
    **_Limitation:_**
     
    wylie2unicode and unicode2wylie both send the string to be transcoded as the commandline argument Perl receives.
    As such, strings should not be higher than the limit allowed for command-line arguments.
    
    For Windows: as seen [here](https://stackoverflow.com/a/14177376), 2047 or 8191 characters.
 
    For Posix systems: as seen [here](https://stackoverflow.com/a/14176172), 2097152 (my output of `getconf ARG_MAX`)

 - `batch_convert(mode, include_orig)` simply wraps `wylieconvert/Lingua-BO-Wylie/bin/wylie.pl` and converts all .txt files from `input/` to `output/`.
The folders are created if missing on the first run of the script.

 - `batch_converter.py` wraps `batch_convert` for the command line.
    
    Syntax: `python3 batch_converter.py <mode> <include_orig>`
            
    - `mode` can either be `w2u` or `u2w`
    - `include_orig` is optional and should be `true`
    
    Ex: `python3 batch_converter.py u2w` will convert all .txt files from unicode to wylie, not including the original.

# Licence

The [downloadable zip](http://www.digitaltibetan.org/tibetan/Lingua-BO-Wylie-dev.zip) does not contain any information about licence nor states the author.

Any help finding this information will be appreciated.
