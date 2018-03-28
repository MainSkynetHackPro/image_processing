#!env/bin/python
from os import listdir

from PIL import Image
from multiprocessing import Process

from filters.border_chroma_filter import BorderChromaFilter
from filters.border_filter import BorderFilter
from filters.curve_filter import CurveFilter
from filters.median_filter import MedianFilter

processes = []

filename = '8.jpg'


def filter_0():
    img = Image.open(f'input/{filename}')
    median_filter = MedianFilter()
    median_filter.load_pixels(img)
    median_filter.radius = 5
    median_filter.process()
    # border_filter = BorderChromaFilter()
    # border_filter.load_pixels(img)
    # border_filter.process()
    # curves_filter = CurveFilter()
    # curves_filter.load_pixels(img)
    # curves_filter.set_sqrt_filter()
    # curves_filter.process()
    img.save(f'output/0_{filename}')


def filter_1():
    img = Image.open(f'input/{filename}')
    # border_filter = BorderChromaFilter()
    # border_filter.load_pixels(img)
    # border_filter.process()
    # curves_filter = CurveFilter()
    # curves_filter.load_pixels(img)
    # curves_filter.set_sqrt_filter()
    # curves_filter.process()
    img.save(f'output/1_{filename}')


p0 = Process(target=filter_0)
p1 = Process(target=filter_1)
p0.start()
p1.start()
p0.join()
p1.join()
