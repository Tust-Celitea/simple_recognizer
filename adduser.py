#!/usr/bin/python2
'''Add a user to server's database'''
from __future__ import print_function
import config
import os.path
import requests

from faceplus.facepp import API,File,APIError

api = API(config.API_KEY, config.API_SECRET)

def getface(image):
    '''
    Get a face_id from a face image.
    '''
    try:
        if os.path.exists(image):
            print("Using local file:{}".format(os.path.abspath(image)))
            face=api.detection.detect(img=File(image))
        else:
            print("Using external file:{}".format(image))
            face=api.detection.detect(url=image)
    except APIError as err:
        print("Face++ API Exception:{}".format(str(err)))
        return None
    else:
        return face

def create_person(face,username):
    '''
    Use a username and a face_id to create a person.
    '''
    try:
        person=api.person.create(person_name = username, face_id = face['face'][0]['face_id'])
        api.train.identify(person_name = username)
    except APIError as err:
        print("Face++ API Exception:{}".format(str(err)))
        return None
    else:
        return person

def send_person(person,server=config.LOG_SERVER):
    '''
    Send username and face_id to server.
    '''
    request=requests.post("{}/register/{}".format(server,person['person_name']),data={'username':person['person_name'],'person_id':person['person_id']})
    result=request.json()
    print(result)

if __name__=="__main__":
    image="http://cn.faceplusplus.com/static/resources/python_demo/1.jpg"
    username="for_baz"
    current_face=getface(image)
    print(current_face)
    current_person=create_person(current_face,username)
    print(current_person)
    send_person(current_person)
    api.person.delete(person_name = username)

