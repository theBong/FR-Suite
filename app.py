import cv2
import multiprocessing

def ticket(source):
    '''
    Scans through camera for a ticket object.
    On detection, it will open up another camera window for face registration.

    Upon face registration, system will retrain model and create notification in AOMS

    Database will register face and save zones it is allowed in
    '''
    