""" Testing a quadratic equation based on "equation_data.json"
The results of solving the equation are displayed in "quadratic_solution_json.log"
For using open the Terminal and type
'python hw_6_main_json.py --path edata_v1 or (_v2, _v3).json ' """
import logging
import argparse
import json
import math
import utils as uts


logging.basicConfig(level=logging.DEBUG,
                    filename="quadratic_solution_json.log",
                    filemode="w")
logging.info("Start program")


def parse_args():
    """ Function used "equation_data_v1 or (_v2, _v3).json"  """
    parser = argparse.ArgumentParser(description='quadratic solution')
    parser.add_argument('--path',
                        type=str,
                        required=True,
                        help='path to specification *.json file')

    return parser.parse_args()


args = parse_args()
path_config = args.path
configs = open(path_config)
config = json.loads(configs.read())


A = config['data_A']
B = config['data_B']
C = config['data_C']


def discriminant():
    """ Calculating the discriminant
    and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(A, B, C)
    logging.info(f'discriminant = {dis_t}')


def get_roots():
    """ Calculating the roots
        and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(A, B, C)
    if dis_t > 0:
        x_1 = (-B + math.sqrt(dis_t)) / (2 * A)
        x_2 = (-B - math.sqrt(dis_t)) / (2 * A)
        logging.info(f'the equation has 2 roots = {x_1}, {x_2}')


def get_root():
    """ Calculating the root
        and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(A, B, C)
    if dis_t == 0:
        x_3 = -B / 2 * A
        logging.info(f'the equation has 1 root {x_3}')


def no_roots():
    """ Outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(A, B, C)
    if dis_t < 0:
        logging.info(' no roots !')
