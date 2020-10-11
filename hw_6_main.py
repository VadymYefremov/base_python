""" For using open the Terminal and type 'python hw_6_main.py --h'
You will see the answer in the file with the name "quadratic_solution.log"""
import hw_6_quadratic_equation as qe


def run():
    """ All project functions are in the file 'hw_6_quadratic_equation.py' """
    qe.parser_args()
    qe.discriminant()
    qe.get_roots()
    qe.get_root()
    qe.no_roots()


if __name__ == "__main__":
    run()
