""" Main class "Person" ,SubClass "Tutors"
 project functions are in the files "persons.py" """
from persons import Person


class Tutor(Person):
    """ Subclass Tutors, main class Person """
    def get_experience(self):
        """ Counts experience of Tutors  """
        return self.year - self.standing

    def get_age(self):
        """ Counts age of Tutors """
        return self.year - self.year_birth
