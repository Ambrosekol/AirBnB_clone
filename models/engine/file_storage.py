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
        return FileStorage.__objects

    def save(self):
        """
        doc
        """
        with open(FileStorage.__file_path, "a") as f:
            json.dump(FileStorage.__objects, f)

    def new(self, obj):
        """
        doc
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj.to_dict()

    def reload(self):
        """
        doc
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass
