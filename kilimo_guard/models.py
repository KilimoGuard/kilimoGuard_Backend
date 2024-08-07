from datetime import datetime
from mongoengine import *

# Create your models here.

class Users(Document):    
    firebase_id = StringField(required=True)                        
    # Add other fields....
    date_modified = DateTimeField(default=datetime.utcnow, required=True) # Each model should have this field
    created_at = DateTimeField(required=True)              # Each model should have this field