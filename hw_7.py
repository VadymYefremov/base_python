""" Sort list
 The results are displayed in "hw_7_list.py"
 """
import os
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename="hw_7_list.log",
                    filemode="w")

# Displays & sort list data
file_list = os.listdir('.')
file_list.sort()
for ns in file_list:
    logging.info(f'sort list: {ns}')
logging.info(f'amount of elements: {len(file_list)}')
