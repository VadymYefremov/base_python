""" Logging module and function parse_args
 Used in files main.py & face_recognition.py """
import logging
import argparse
import os


logging.basicConfig(level=logging.DEBUG, filename="detected_info.log", filemode="w")


def parse_args():
    """ Function used "face_recognition.py"  """
    parser = argparse.ArgumentParser(description='folder selection')
    parser.add_argument('--folder',
                        type=str,
                        required=True,
                        help='type name folder with faces image')

    return parser.parse_args()


args = parse_args()
fold = args.folder
os.listdir(fold)
