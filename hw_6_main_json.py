""" For testing open the Terminal and type
'python hw_6_main_json.py --path equation_data_v1 or (_v2, _v3).json ''
The results of solving the equation are displayed in "quadratic_solution_json.log"""
import hw_6_quadratic_equation_json as qe_j


def run():
    """ All project functions are in the file 'hw_6_quadratic_equation.py' """
    qe_j.parse_args()
    qe_j.discriminant()
    qe_j.get_roots()
    qe_j.get_root()
    qe_j.no_roots()


if __name__ == "__main__":
    run()
