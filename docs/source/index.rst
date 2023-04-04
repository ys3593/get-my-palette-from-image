.. get-my-palette-from-image documentation master file, created by
   sphinx-quickstart on Mon Apr  3 21:05:53 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to get-my-palette-from-image's documentation!
=====================================================

Installation
=====================================================

Install the library::

   pip install get-my-palette-from-image
=====================================================

Usage
=====================================================

Use the library::

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
=====================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
