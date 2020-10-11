""" Solving a quadratic equation based on your input
The results of solving the equation are displayed in "quadratic_solution.log"
For using open the Terminal and type 'python hw_6_main.py --h' """
import logging
import argparse
import math
import utils as uts


logging.basicConfig(level=logging.DEBUG,
                    filename="quadratic_solution.log",
                    filemode="w")
logging.info("Start program")


def parser_args():
    """ Function used to enter data through the terminal """
    parser = argparse.ArgumentParser(description='quadratic solution')

    parser.add_argument('--a',
                        type=float,
                        required=True,
                        help='enter the data "a" to solve the quadratic equation')

    parser.add_argument('--b',
                        type=float,
                        required=True,
                        help='enter the data "b" to solve the quadratic equation')

    parser.add_argument('--c',
                        type=float,
                        required=True,
                        help='enter the data "c" to solve the quadratic equation')

    return parser.parse_args()


arg = parser_args()


def discriminant():
    """ Calculating the discriminant
    and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(arg.a, arg.b, arg.c)
    logging.info(f'discriminant = {dis_t}')


def get_roots():
    """ Calculating the roots
        and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(arg.a, arg.b, arg.c)
    if dis_t > 0:
        x_1 = (-arg.b + math.sqrt(dis_t)) / (2 * arg.a)
        x_2 = (-arg.b - math.sqrt(dis_t)) / (2 * arg.a)
        logging.info(f'the equation has 2 roots = {x_1}, {x_2}')


def get_root():
    """ Calculating the root
        and outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(arg.a, arg.b, arg.c)
    if dis_t == 0:
        x_3 = -arg.b / 2 * arg.a
        logging.info(f'the equation has 1 root {x_3}')


def no_roots():
    """ Outputting the result to "quadratic_solution.log" """
    dis_t = uts.D(arg.a, arg.b, arg.c)
    if dis_t < 0:
        logging.info(' no roots !')
