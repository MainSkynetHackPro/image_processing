from filters.base_filter import BaseFilter


class MedianFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        self.radius = 2

    def process(self):
        for i in range(self.width - self.radius):
            for j in range(self.height - self.radius):
                self.pixels[i, j] = self.count_for_pixel(i, j)

    def count_for_pixel(self, i, j):

        return self.count_for_pixel_color(i, j, 0), \
               self.count_for_pixel_color(i, j, 1), \
               self.count_for_pixel_color(i, j, 2)

    def count_for_pixel_color(self, i, j, index):
        items = list()
        for offset in range(0, self.radius):
            items.append(self.pixels[i + offset, j][index])
            items.append(self.pixels[i, j + offset][index])
        items.sort()
        return items[self.radius]
