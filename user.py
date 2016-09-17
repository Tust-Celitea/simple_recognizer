#!/usr/bin/python2
import dbc
from faceplus.facepp import API,File
import requests
from config import *
# initialize face++ api.
api=API(API_KEY,API_SECRET)

class DummyDB:
    ''' A dummy DB,not execute any action'''
    def __init__(self,target):
        pass
    def execute(self,*args):
        pass

class User(object):
    '''
    Present a User,include names and faceplus api information.
    '''
    def faceplus_createperson(self,image,username):
        '''
        Create a faceplus person.
        return person_id.
        '''
        face=self.faceplusapi.detection.detect(File(image))
        person=self.faceplusapi.person.create(person_name = username, face_id = face['face'][0]['face_id'])
        rst=self.faceplusapi.train.identify(person_id=person['person_id'])
        return person['person_id']

    def faceplus_revokeperson(self):
        '''
        Delete a faceplus person.
        '''
        self.faceplusapi.person.delete(self.person_id)

    def __init__(name,username,init_image,dbc,faceplusapi):
        self.name=name
        self.username=username
        self.init_image=init_image
        self.dbc=dbc
        self.faceplusapi=faceplusapi
        self.person_id=faceplus_createperson(self.init_image,self.username)
        self.dbc.execute()

    def __eq__(self,another):
        return self.person_id==another.person_id

    def __str__(self):
        return "{}(@{})".format(self.name,self.username)

    def __repr__(self):
        return "{}\nface_id:{}".format(str(self),self.person_id)

    def jsonify(self):
        return {'name':self.name,
                'username':self.username,
                'person_id':self.person_id}

if __name__=="__main__":
    test_user=User()
