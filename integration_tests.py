import functions

def test_get_palette():
    palette = functions.PaletteCreation()
    modified_image = palette.load_image_url('https://apod.nasa.gov/apod/image/2212/SkyArt_Cobianchi_2048.jpg')
    the_palette = palette.get_palette(modified_image, 5)
    assert the_palette == ['#3f3b25', '#5f5c4d', '#1b1106', '#948161', '#c1c85b']