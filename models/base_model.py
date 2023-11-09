#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
#import models

class BaseModel:
    def __init__(self , *arguments , **KeyWordArguments):
        self.id = str(uuid4())
        TimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.today()
        self.created_at = datetime.today()

        if len(KeyWordArguments) != 0:
            for Key, Value in KeyWordArguments.items():
                if Key == "created_at" or Key == "updated_at":
                    self.__dict__[Key] = datetime.strptime(Value, TimeFormat)
                else:
                    self.__dict__[Key] = Value
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """

        result_dict = self.__dict__.copy()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict
    
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
