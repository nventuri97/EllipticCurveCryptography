"""Implementation of NonValidHException"""

class NonValidHException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)