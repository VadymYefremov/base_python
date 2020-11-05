""" Start program """
import trace as tr
import util_nl as ut


def run():
    """ All project functions are in the files 'util_nl.py' & 'trace.py'  """
    ut.parse_args()
    tr.word_count()


if __name__ == "__main__":
    run()
