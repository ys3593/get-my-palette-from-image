from collections import Counter
import numpy
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import cv2
from PIL import Image
import requests
from io import BytesIO
import seaborn as sns


class PaletteCreation:
    # load image
    def load_image(self, path):
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

    # get given number of rgb colors from the given image using kmeans
    def get_colors(self, image, number):
        kmeans = KMeans(n_clusters=number, n_init=10, random_state=1)
        kmeans.fit(image)
        y_kmeans = kmeans.predict(image)
        count = Counter(y_kmeans)
        centers = kmeans.cluster_centers_

        rgb_colors = []
        for i in count.keys():
            rgb_colors.append(centers[i])

        return count, rgb_colors

    # obtain the percentage of colors from the given image
    def get_color_percentages(self, image, number):
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

    # get a palette from given image
    def get_palette(self, image, number):
        count, rgb_colors = self.get_colors(image, number)

        hex_colors = []
        for i in count.keys():
            color = rgb_colors[i]
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        return hex_colors

    # get a complementary palette from given image
    def get_complementary_palette(self, image, number):
        count, rgb_colors = self.get_colors(image, number)

        hex_colors = []
        for i in count.keys():
            color = 255 - rgb_colors[i]
            hex_color = "#"
            for j in color:
                hex_color += "{:02x}".format(int(j))
            hex_colors.append(hex_color)

        return hex_colors

    # get a palette consisted of colors with the least percentages
    def get_least_palette(self, image, number):
        percentage_dic = self.get_color_percentages(image, 2 * number)
        sorted_percentage_dic = sorted(percentage_dic.items(), key=lambda x: x[1])[
            :number
        ]
        palette = []
        for i in sorted_percentage_dic:
            palette.append(i[0])

        return palette

    # get a palette consisted of colors with the most percentages
    def get_most_palette(self, image, number):
        percentage_dic = self.get_color_percentages(image, 2 * number)
        sorted_percentage_dic = sorted(
            percentage_dic.items(), key=lambda x: x[1], reverse=True
        )[:number]
        palette = []
        for i in sorted_percentage_dic:
            palette.append(i[0])

        return palette

    # # obtain a palette with similar colors from the given image
    # def get_similar_palette(self, image, number):
    #     count, rgb_colors = self.get_colors(image, number)
    #     palette = []
    #
    #     return palette
    #
    # # obtain a palette with contrast colors from the given image
    # def get_contrast_palette(self, image, number):
    #     count, rgb_colors = self.get_colors(image, number)
    #     palette = []
    #
    #     return palette

    def present_palette(self, palette):
        sns.palplot(sns.color_palette(palette))
        plt.show()

    def present_percentage(self, percentage):
        plt.pie(percentage.values(), labels=percentage.keys(),
                colors=percentage.keys())
        plt.show()


def main():
    palette = PaletteCreation()

    # load image locally
    modified_image = palette.load_image('down.jpg')

    # obtain the percentage of colors from the given image
    percentage = palette.get_color_percentages(modified_image, 5)

    print(percentage)
