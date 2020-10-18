""" For using program "Face detected" open the Terminal and type
'python main.py --folder ( with the name of the folder with the photo,
which should be in the same directory)'
You will see the detection data in the file with the name 'detected_info.log'
Face detection data is contained in the file with the name 'faces_dump.pickle' """
import logging_parse as lp
import face_recognition as fr


def run():
    """ All project functions are in the files 'logging_pars.py' & 'face_recognition.py'  """
    lp.parse_args()
    fr.reading_files()


if __name__ == "__main__":
    run()
