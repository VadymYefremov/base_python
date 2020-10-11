""" Main class "Person" ,SubClass "Student"
 project functions are in the files "persons.py" """
from persons import Person


class Students(Person):
    """ Subclass Students, main class Person """
    def get_course(self):
        """ Counts the course of students """
        return self.year - self.standing

    def get_age(self):
        """ Counts the age of students """
        return self.year - self.year_birth
