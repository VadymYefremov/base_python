""" Testing face recognition software for time and correct operation.
The testing picture has 7 faces """
import os
import time
import cv2
import utils as utl


def benchmark(iters, correct_faces):
    """ Decorator for testing face recognition
    software for time and correct operation
     iters - the number of repetitions of the operation
     used for testing speed
     correct_faces - the number of faces in picture
     used for testing correct face recognition operation """
    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            total = 0
            for _i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            utl.logging.info('[*] среднее время выполнения: {} секунд.'.format(total / iters))
            faces = func(*args, **kwargs)
            if faces == correct_faces:
                utl.logging.info('количество распознанных лиц совпало, тест пройден')
            else:
                utl.logging.info('количество распознанных лиц не совпало, тест не пройден')

            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=1, correct_faces=7)
def proc_speed_conv():
    """ Test part of the program on speed
    and correct of work """
    for file in os.listdir('faces'):
        img = cv2.imread(os.path.join('faces', file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = utl.face_cascade.detectMultiScale(gray, 1.1, 4)
        inf_faces = len(faces)
        return inf_faces


proc_speed_conv()


@benchmark(iters=3, correct_faces=6)
def proc_speed_roi():
    """ Test part of the program on speed
    and correct of work """
    for file in os.listdir('faces'):
        img = cv2.imread(os.path.join('faces', file))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = utl.face_cascade.detectMultiScale(gray, 1.1, 4)
        for (_x, _y, _w, _h) in faces: # ROI  - region of interest
            cv2.rectangle(img, (_x, _y), (_x+_w, _y+_h), (255, 0, 0), 2)
        inf_faces = len(faces)
        return inf_faces


proc_speed_roi()
