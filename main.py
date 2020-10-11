""" For using open the Terminal and type 'python main.py'
Files "persons.py", "tutors.py", "students.py"  have to be in one directory,
 All project functions are in the files "persons.py", "tutors.py", "students.py" """
from tutors import Tutor
from students import Students


def run():
    """  Data value:
    Y - this year,
    S - year of start of study or career,
    A - year of birth
       """
    ttr = Tutor(Y=2020, S=2010, A=1980)
    std = Students(Y=2020, S=2017, A=2000)
    print('Age of Tutor:', ttr.get_age())
    print('Experience of Tutor:', ttr.get_experience())
    print('Age of Student:', std.get_age())
    print('Course of Student:', std.get_course())


print(dir())


if __name__ == "__main__":
    run()
