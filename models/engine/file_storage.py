#!/usr/bin/python3
"""
doc
"""
import json


class FileStorage():
    """
    doc
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        doc
        """
        from models.base_model import BaseModel
        my_dict = {}
        for k, v in FileStorage.__objects.items():
            my_dict[k] = eval(k.split(".")[0])(**v)
        return my_dict

    def save(self):
        """
        doc
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def new(self, obj):
        """
        doc
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects[class_name + "." + obj.id] = obj.to_dict()

    def reload(self):
        """
        doc
        """
        #print("called")
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass
