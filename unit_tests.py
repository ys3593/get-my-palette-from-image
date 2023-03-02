from collections import Counter
import functions


def test_get_colors_counter():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    count, rgb_colors = palette.get_colors(modified_image, 5)
    assert count == Counter({0: 13877, 2: 13580, 3: 12314, 4: 7816, 1: 2943})


def test_get_color_percentages():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    percentage = palette.get_color_percentages(modified_image, 5)
    assert percentage == {'#57501e': 0.15, '#5197c1': 0.27, '#697985': 0.06, '#9d9f9d': 0.27, '#7f723a': 0.24}


def test_get_palette():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    the_palette = palette.get_palette(modified_image, 5)
    assert the_palette == ['#57501e', '#5197c1', '#697985', '#9d9f9d', '#7f723a']


def test_get_complementary_palette():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    complementary_palette = palette.get_complementary_palette(modified_image, 5)
    assert complementary_palette == ['#a7aee0', '#ad673d', '#958579', '#615f61', '#7f8cc4']


def test_get_least_palette():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    least_palette = palette.get_least_palette(modified_image, 3)
    assert least_palette == ['#5197c1', '#697985', '#9d9f9f']


def test_get_most_palette():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image('download.jpg')
    most_palette = palette.get_most_palette(modified_image, 3)
    assert most_palette == ['#6b622b', '#8a7c43', '#9d9f9f']