""" Face detected function
for correct work is necessary file
'haarcascade_frontalface_default.xml' must be in the directory """
import os
import pickle
import cv2
import logging_parse as lp


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def reading_files():
    """ Function opens images (jpg) files
       for detect face in images
       and records results in files
       'detected_info.log' & 'faces_dump.pickle' """
    data = []
    for file in os.listdir(lp.fold):
        img = cv2.imread(os.path.join(lp.fold, file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        tp_data = type(faces)
        if tp_data is tuple:
            lp.logging.info(f'in file {file} face(s) not detected ')
        else:
            lp.logging.info(f'in file {file} face(s) detected \n {faces}')
        data.append(faces)
    with open('faces_dump.pickle', 'wb') as fl_l:
        pickle.dump(data, fl_l)
