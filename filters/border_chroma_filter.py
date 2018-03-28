from filters.base_filter import BaseFilter


class BorderChromaFilter(BaseFilter):
    def __init__(self):
        super().__init__()

    def process(self):
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                self.pixels[i, j] = self.count_for_pixel_color(i, j, 0), self.count_for_pixel_color(i, j,
                                                                                                    1), self.count_for_pixel_color(
                    i, j, 2)

    def count_for_pixel_color(self, i, j, index):
        return abs(self.pixels[i, j][index] - self.pixels[i + 1, j + 1][index]) + abs(
            self.pixels[i, j + 1][index] - self.pixels[i + 1, j][index])
