""" Function parse_args
 Used in files main_nl.py"""
import argparse
import trace as ts


def parse_args():
    """ The function is used to analyze text :
    '--file' - for choosing file (.txt only) - is a mandatory function

    The following functions can be selected as needed:
    '--a' - conducts tokenize, lemmatize and stemming of text
    '--b' - stop word of text
    '--c' - counts all duplicate words in the text
    '--d' - displays the specified number of frequent words
    as un example: (Terminal) python main_nl.py --file (name.txt) --d (the right amount)
      """
    parser = argparse.ArgumentParser(description='text analysis')
    parser.add_argument('--file',
                        type=str,
                        required=True,
                        help='path to specification *.txt file')

    parser.add_argument("--a", action="store_true",
                        help="This is the 'a' variable")
    parser.add_argument("--b", action="store_true",
                        help="This is the 'a' variable")
    parser.add_argument("--c", action="store_true",
                        help="This is the 'a' variable")
    parser.add_argument("--d", action='store', type=int,
                        default=False, nargs='?',
                        help="This is the 'a' variable")

    return parser.parse_args()


args = parse_args()
path_config = args.file
data_op = open(path_config)
data_read = data_op.read()


a = args.a
if a is True:
    ts.token_file()
    ts.lemm_file()
    ts.stem_file()

b = args.b
if b is True:
    ts.stop_word()

c = args.c
if c is True:
    ts.word_count_all()

d = args.d
if d is True:
    ts.word_count()
