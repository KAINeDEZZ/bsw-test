from schema import Event
from provider import share_event


class EventStorage(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key: int, value: Event):
        super().__setitem__(key, value)
        share_event(value)
