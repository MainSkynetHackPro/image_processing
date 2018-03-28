import math

from filters.base_filter import BaseFilter


class CurveFilter(BaseFilter):
    def __init__(self):
        super().__init__()

        def default_tune_function(r, g, b):
            return r, g, b

        self.__tune_function = default_tune_function

    def set_tune_function(self, func):
        self.__tune_function = func

    def set_sqrt_filter(self):
        def f(r, g, b):
            new_r, new_g, new_b = r, g, b
            if r > 0:
                new_r = int(round(math.sqrt(r) * 16))
            if g > 0:
                new_g = int(round(math.sqrt(g) * 16))
            if b > 0:
                new_b = int(round(math.sqrt(b) * 16))

            return new_r, new_g, new_b

        self.__tune_function = f

    def set_grayscale_binary_filter(self):
        def f(r, g, b):
            b = (r + g + b) // 3
            if b > 255 / 2:
                b = 255
            else:
                b = 0
            return b, b, b

        self.__tune_function = f

    def set_chroma_binary_filter(self):
        def f(r, g, b):
            r = 0 if r < 255/2 else 255
            g = 0 if g < 255/2 else 255
            b = 0 if b < 255/2 else 255
            return r, g, b

        self.__tune_function = f

    def set_chroma_half_binary_filter(self):
        def f(r, g, b):
            r = r if r < 255/2 else 255
            g = g if g < 255/2 else 255
            b = b if b < 255/2 else 255
            return r, g, b

        self.__tune_function = f

    def process(self):
        for i in range(self.width):
            for j in range(self.height):
                try:
                    r, g, b = self.pixels[i, j]
                    self.pixels[i, j] = self.__tune_function(r, g, b)
                except:
                    pass
