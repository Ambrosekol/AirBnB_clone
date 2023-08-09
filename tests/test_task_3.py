#!/usr/bin/python3
"""
tests
"""

import unittest
from models.base_model import BaseModel

obj = BaseModel()


class TestBaseModel(unittest.TestCase):
    """
    doc
    """
    def test_task_3(self):
        """
        doc
        """
        attributes = ["id", "created_at", "updated_at", "to_dict", "save"]
        self.assertTrue(all(hasattr(obj, attr) for attr in attributes))
