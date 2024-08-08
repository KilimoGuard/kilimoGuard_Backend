from datetime import datetime

import bcrypt
from mongoengine import *


# Create your models here.

class Users(Document):
    # firebase_id = StringField(required=True)
    # Add other fields....
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    date_modified = DateTimeField(default=datetime.utcnow, required=True)  # Each model should have this field
    created_at = DateTimeField(default=datetime.utcnow(),required=True)  # Each model should have this field

    def save(self, *args, **kwargs):
        if self.password:
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return super(Users, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        is_valid = bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))
        return is_valid

