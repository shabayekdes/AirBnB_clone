#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If arguments are provided in kwargs,
        it populates the instance attributes.
        If no arguments are provided, it adds the new instance to the storage.

        Args:
            *args: Non-keyword variable-length argument list.
            **kwargs: Variable-length keyword argument list.
        """
        self.id = str(uuid4())
        TimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.updated_at = datetime.today()
        self.created_at = datetime.today()

        if len(kwargs) != 0:
            for Key, Value in kwargs.items():
                if Key == "created_at" or Key == "updated_at":
                    self.__dict__[Key] = datetime.strptime(Value, TimeFormat)
                else:
                    self.__dict__[Key] = Value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current date and time,
        then saves the changes to the storage.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: Dictionary containing the instance attributes.
        """
        result_dict = self.__dict__.copy()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation containing
            class name, instance id, and attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
