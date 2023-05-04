# get-my-palette-from-image
get-my-palette-from-image is a python library for extracting and manipulating palettes from images   
 
![GitHub](https://img.shields.io/github/license/ys3593/my-palette)
![GitHub issues](https://img.shields.io/github/issues/ys3593/my-palette)
![Build Status](https://github.com/ys3593/my-palette/actions/workflows/build.yml/badge.svg)
[![codecov](https://codecov.io/gh/ys3593/get-my-palette-from-image/branch/main/graph/badge.svg?token=PZ1MROE5N6)](https://codecov.io/gh/ys3593/get-my-palette-from-image)
![PyPI](https://img.shields.io/pypi/v/get-my-palette-from-image)
![Docs](https://img.shields.io/readthedocs/get-my-palette-from-image)


## Overview
- Input: image, URL
- Functions:  
  - extract palettes with self-defined numbers of colors from given images
  - shuffle/modify extracted palettes
  - obtain the percentages of colors from given images
  - find/generate posters/images based on extracted palettes   
 
### Installation

```
pip install get-my-palette-from-image
```
### Usage
```
from my_palette import PaletteCreation

palette = PaletteCreation()

# load image locally
modified_image = palette.load_image('down.jpg')

# load image via url
modified_image_url = palette.load_image_url(
    'https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')

# obtain the percentage of colors from the given image
percentage = palette.get_color_percentages(modified_image, 5)

# get a palette from given image with a self-defined number of colors
the_palette = palette.get_palette(modified_image, 5)

# get a complementary palette from given image with a self-defined number of colors
complementary_palette = palette.get_complementary_palette(
    modified_image, 5)

# get a palette consisted of a self-defined number of colors with the least percentages
least_palette = palette.get_least_palette(modified_image, 3)

# get a palette consisted of a self-defined number of colors with the most percentages
most_palette = palette.get_most_palette(modified_image, 3)

# get a palette with consisted of a self-defined number of similar colors from the given image and given color schema.
# the color schema includes red, blue, green, yellow, black, white, purple, orange, and pink
similar_palette = palette.get_similar_palette(modified_image, 3, 'black')
```

### Development
Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
