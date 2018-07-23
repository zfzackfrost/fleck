from kivy.event import EventDispatcher
from kivy.properties import ListProperty


class FleckWorld(EventDispatcher):

    materials = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_init_materials(self):
        pass
