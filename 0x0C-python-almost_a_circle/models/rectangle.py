#!/usr/bin/python3
"""import base class"""


from models.base import Base


"""Rectangle child class"""


class Rectangle(Base):
    """Rectangle child class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle attr"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
