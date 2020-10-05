""" Sort list
 The results are displayed in "hw_7_list.py"
 """
import os
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename="hw_7_list.log",
                    filemode="w")

# Displays list data
file_list = os.listdir('.')
logging.info(f'list info: {file_list}')


# Sorts by name
file_list.sort()
for ns in file_list:
    logging.info(f'sort list & new string:{ns}')


# Shows the number of items
logging.info(f'amount of elements: {len(file_list)}')
