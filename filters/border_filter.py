from filters.base_filter import BaseFilter


class BorderFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    def process(self):
        for i in range(self.width-1):
            for j in range(self.height-1):
                self.pixels[i, j] = self.count_for_pixel(i, j)

    def count_for_pixel(self, i, j):
        val = abs(self.pixels[i, j][0] - self.pixels[i + 1, j + 1][0]) + abs(
            self.pixels[i, j + 1][0] - self.pixels[i + 1, j][0])
        return val, val, val
