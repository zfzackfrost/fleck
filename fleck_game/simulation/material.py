import numpy as np
import uuid


class FleckMaterial:
    """Describes the physical and visual properties of a particle in the world

    All materials are loaded from JSON files when the game starts. This lets the
    player easily create new materials.
    """

    def __init__(self):
        self.__display_name = ''
        self.__display_name_written = False
        self.__id = -1
        self.__id_written = False
        self.__color = np.ones(3, dtype=numpy.float16)

    @property
    def display_name(self):
        return self.__display_name

    @property.setter
    def display_name(self, value):
        if not self.__display_name_written:
            if type(value) == type(str) and len(value) > 0:
                self.__display_name = value
                self.__display_name_written = True

    @property
    def color(self):
        return self.__color.tolist()

    @property.setter
    def color(self, value):
        self.__color = np.array(value)

    @property
    def id(self):
        return self.__id

    @property.setter
    def id(self, value):
        if not self.__id_written:
            if type(value) == type(int) and value >= 0:
                self.__id = value
                self.__id_written = True
