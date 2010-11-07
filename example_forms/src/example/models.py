import grok
from zope.interface import Interface
from zope import schema

class Person(grok.Model):

    def __init__(self, name, date_of_birth, gender):
        self.name = name
        self.date_of_birth  = date_of_birth
        self.gender = gender
