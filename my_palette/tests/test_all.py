from collections import Counter
from my_palette import PaletteCreation
from unittest.mock import patch


def test_get_colors_counter():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    count, rgb_colors = palette.get_colors(modified_image, 5)
    assert count == Counter({2: 775114, 0: 604989, 1: 575733, 3: 420526, 4: 181590})


def test_get_color_percentages():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    percentage = palette.get_color_percentages(modified_image, 5)
    assert percentage == {'#3f3b25': 0.24, '#5f5c4d': 0.23, '#1b1106': 0.3, '#948161': 0.16, '#c1c85b': 0.07}


def test_get_palette():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    the_palette = palette.get_palette(modified_image, 5)
    assert the_palette == ['#3f3b25', '#5f5c4d', '#1b1106', '#948161', '#c1c85b']


def test_get_complementary_palette():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    complementary_palette = palette.get_complementary_palette(modified_image, 5)
    assert complementary_palette == ['#bfc3d9', '#9fa2b1', '#e3edf8', '#6a7d9d', '#3d36a3']


def test_get_least_palette():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    least_palette = palette.get_least_palette(modified_image, 3)
    assert least_palette == ['#ae9060', '#191005', '#c3d859']


def test_get_most_palette():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    most_palette = palette.get_most_palette(modified_image, 3)
    assert most_palette == ['#7a725d', '#555345', '#3b361f']


def test_get_similar_palette():
    palette = PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    most_palette = palette.get_similar_palette(modified_image, 3, 'black')
    assert most_palette == ['#120802', '#241b0a', '#392f12']