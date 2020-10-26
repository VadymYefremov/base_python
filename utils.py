""" UTIL contains used modules in file
'fd_speed_test.py' """
import logging
import cv2

logging.basicConfig(level=logging.DEBUG, filename="testing_info.log", filemode="w")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
