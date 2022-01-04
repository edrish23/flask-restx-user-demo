import os
from datetime import datetime
from . import db 

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    FullName=db.Column(db.String(80),nullable=False)
    Email=db.Column(db.String(40),nullable=False)
    Mobile=db.Column(db.String(40),nullable=False)
    DateOfBirth=db.Column(db.String(40),nullable=False)
    Password=db.Column(db.String(40),nullable=False)
    
    def __repr__(self):
        return self.FullName
