""" Created class 'Person'
 with 2 sublass 'Tutor' & 'Student'
 The results are displayed in "persons.log"
 """
import json
import logging

logging.basicConfig(level=logging.DEBUG, filename="persons.log", filemode='w')


class Person():
    """ Main class 'Person' """
    def __init__(self, filepath):
        """
        Properties
        :param name: name person
        :param surname: surname person
        :param sex: sex person
        """
        configs = open(filepath)
        config = json.loads(configs.read())

        self.name = config['name']
        self.surname = config['surname']
        self.sex = config['sex']


students = Person(filepath='student.json')
logging.info(f'student: {students.surname}')


tutors = Person(filepath='tutor.json')
logging.info(f'tutor: {tutors.surname}')
