# mediainfoparser
###### Parser or mediainfo command output

## Installation
The software is developed in Python 3.8, so you should use it. However, it is regularly compiled also in Python 3.7 which you can use too.

Clone the repo and go to its root directory.

install wheel: `pip install wheel`
run: `python setup.py sdist bdist_wheel`
install the wheel: `pip install dist/mediainfoparser-{{version}}-py3-none-any.whl`

(Note: Input a correct {{version}}.)

There will be a script in your 
`Python/Scripts` directory. On Windows, you can find it as `C:\Program Files\Python38\Scripts\mediainfoparser.exe`.


## Usage
Running
`python mediainfoparser/mediainfoparser.py -h`
or on Windows:
`mediainfoparser.exe -h`
you will get:

```
usage: mediainfoparser.py [-h] [--file FILE] [--json-all] [--json-general-only] [--track-type {Audio,Video,Text}] [--track-numbers TRACK_NUMBERS [TRACK_NUMBERS ...]] [--number-of-tracks]
                          [--fields FIELDS [FIELDS ...]]

Parse mediainfo output

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           Input file
  --json-all            Print all as Json
  --json-general-only   Print General section only as Json
  --track-type {Audio,Video,Text}
                        Track type of interest
  --track-numbers TRACK_NUMBERS [TRACK_NUMBERS ...]
                        Track numbers of interest
  --number-of-tracks    Returns number of tracks of given type
  --fields FIELDS [FIELDS ...]
                        fields to output, one per line

```

### Example

The command

`python mediainfoparser/mediainfoparser.py < input.txt`

will parse a file input.txt
