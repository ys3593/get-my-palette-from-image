from collections import Counter
import numpy
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import cv2
from PIL import Image
import requests
from io import BytesIO
import seaborn as sns
from scipy import spatial


class PaletteCreation:
    """ This class is for creating a palette from an image.
    
    """

    def load_image(self, path):
        """ This method converts an image file into a ndarray for further process. 

        Args:
            path (str): The path of the image file

        Returns:
            ndarray: The reshaped image array that represents the original image file for further process

        """
        src = cv2.imread(path)
        # BGR is converted to RGB
        rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        # a: width, b: height, c: channel
        a, b, c = rgb_src.shape
        # resampling using pixel area relation
        image = cv2.resize(rgb_src, (a, b), interpolation=cv2.INTER_AREA)
        reshape = image.reshape(a * b, c)
        return reshape

    def load_image_url(self, url):
        """ This method converts an image url into a ndarray for further process. 

        Args:
            url (str): The image url

        Returns:
            ndarray: The reshaped image array that represents the original image file for further process

        """
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        src = numpy.asarray(img)

        rgb_src = src

        if img.mode == 'RGBA':
            rgb_src = cv2.cvtColor(src, cv2.COLOR_RGBA2RGB)
        if img.mode == 'BGR':
            rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        if img.mode == 'LAB':
            rgb_src = cv2.cvtColor(src, cv2.COLOR_LAB2RGB)
        if img.mode == 'HSV':
            rgb_src = cv2.cvtColor(src, cv2.COLOR_HSV2RGB)

        # a: width, b: height, c: channel
        a, b, c = rgb_src.shape
        # resampling using pixel area relation
        image = cv2.resize(rgb_src, (a, b), interpolation=cv2.INTER_AREA)
        reshape = image.reshape(a * b, c)
        return reshape

    def get_colors(self, image, number):
        """ This method gets a given number of rgb colors from the given image array using kmeans.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            dict: The dict that counts from the result of kmeans.predict(image)
            list: The list of rgb colors obtained from the image array
            
        """
        kmeans = KMeans(n_clusters=number, n_init=10, random_state=1)
        kmeans.fit(image)
        y_kmeans = kmeans.predict(image)
        count = Counter(y_kmeans)
        centers = kmeans.cluster_centers_

        rgb_colors = []
        for i in count.keys():
            rgb_colors.append(centers[i])

        return count, rgb_colors

    def get_color_percentages(self, image, number):
        """ This method obtains the percentage of colors in the palette from the given image array.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            dict: The dict with the colors in the palette as its key and the percentages as it value
            
        """
        count, rgb_colors = self.get_colors(image, number)

        hex_colors = []
        for i in count.keys():
            color = rgb_colors[i]
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        sum_p = sum(list(count.values()))
        percentage = []
        for v in list(count.values()):
            percentage.append(round(v / sum_p, 2))

        i = 0
        percentage_dic = {}
        while i < len(percentage):
            percentage_dic[hex_colors[i]] = percentage[i]
            i += 1

        return percentage_dic

    def get_palette(self, image, number):
        """ This method gets a palette from given image array.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            list: The palette with the extracted hex colors from the given image array.
            
        """
        count, rgb_colors = self.get_colors(image, number)

        hex_colors = []
        for i in count.keys():
            color = rgb_colors[i]
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        return hex_colors

    def get_complementary_palette(self, image, number):
        """ This method gets a complementary palette from given image array.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            list: The complementary palette with the extracted hex colors from the given image array.
            
        """
        count, rgb_colors = self.get_colors(image, number)

        hex_colors = []
        for i in count.keys():
            color = 255 - rgb_colors[i]
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        return hex_colors

    def get_least_palette(self, image, number):
        """ This method gets a palette consisted of colors with the least percentages.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            list: The palette with the least percentages of hex colors from the given image array.
            
        """
        percentage_dic = self.get_color_percentages(image, 2 * number)
        sorted_percentage_dic = sorted(percentage_dic.items(), key=lambda x: x[1])[
            :number
        ]
        palette = []
        for i in sorted_percentage_dic:
            palette.append(i[0])

        return palette

    def get_most_palette(self, image, number):
        """ This method gets a palette consisted of colors with the most percentages.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected

        Returns:
            list: The palette with the most percentages of hex colors from the given image array.
            
        """
        percentage_dic = self.get_color_percentages(image, 2 * number)
        sorted_percentage_dic = sorted(
            percentage_dic.items(), key=lambda x: x[1], reverse=True
        )[:number]
        palette = []
        for i in sorted_percentage_dic:
            palette.append(i[0])

        return palette

    def present_palette(self, palette):
        """ This method plots the obtained palette.

        Args:
            palette (list): The obtained palette

        """
        sns.palplot(sns.color_palette(palette))
        plt.show()

    def present_percentage(self, percentage):
        """ This method plots the palette and the percentages of colors in it via pie plotting.

        Args:
            palette (list): The obtained palette

        """
        plt.pie(percentage.values(), labels=percentage.keys(),
                colors=percentage.keys())
        plt.show()

    def get_similar_palette(self, image, number, given_color):
        """ This method obtain a palette with similar colors from the given image and given color schema.

        Args:
            image (ndarray): The image array obtained with load_image_url method in the class
            number (int): The number of rgb colors expected
            given_color (str): The color schema expected, 
            including red, blue, green, yellow, black, white, purple, orange, and pink

        """
        color_dict = {'red': [255, 0, 0], 'blue': [0, 0, 255], 
                      'green': [0, 255, 0], 'yellow': [255, 255, 0], 
                      'black': [0, 0, 0], 'white': [255, 255, 255], 
                      'purple': [127, 0, 255], 
                      'orange': [255, 128, 0], 
                      'pink': [255, 0, 255]}
        count, rgb_colors = self.get_colors(image, number * 5)
        hex_colors = []

        if color_dict.get(given_color):
            given_color_rgb = color_dict[given_color]

        # find the number most similar colors from these total number * 3 colors: kdtree
        tree = spatial.KDTree(rgb_colors)
        query_color = [given_color_rgb]
        d, i = tree.query(query_color, k=number)

        for color in tree.data[i][0]:
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        return hex_colors
