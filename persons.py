""" Main class"""


class Person:
    """ Main class Person of subclasses tutors & students"""
    def __init__(self, Y, S, A):
        """ Y - this year,
        S - year of start of study or career,
        A - year of birth
        """
        self.year = Y
        self.standing = S
        self.year_birth = A
