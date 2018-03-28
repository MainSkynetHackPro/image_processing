from abc import abstractmethod


class BaseFilter:
    def __init__(self):
        self.pixels = None
        self.width = None
        self.height = None

    def load_pixels(self, image):
        self.width = image.size[0]
        self.height = image.size[1]
        self.pixels = image.load()

    @abstractmethod
    def process(self):
        pass
