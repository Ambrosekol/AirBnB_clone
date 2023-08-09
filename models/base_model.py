#!/usr/bin/python3
"""
base_model module
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    class BaseModel
    """
    def __init__(self):
        """
        doc
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """
        doc
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        update the updated_at attribute
        to the last time it was saved
        """
        self.updated_at = datetime.now().isoformat()
        
    def to_dict(self):
        """
        doc
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

