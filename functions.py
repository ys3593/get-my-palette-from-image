from collections import Counter
from sklearn.cluster import KMeans
import cv2


# load image
def load_image(path):
    src = cv2.imread(path)
    # BGR is converted to RGB
    rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    # a: width, b: height, c: channel
    a, b, c = rgb_src.shape
    # resampling using pixel area relation
    image = cv2.resize(rgb_src, (a, b), interpolation=cv2.INTER_AREA)
    return image.reshape(a * b, c)


# get given number of rgb colors from the given image using kmeans
def get_colors(image, number):
    kmeans = KMeans(n_clusters=number)
    kmeans.fit(image)
    y_kmeans = kmeans.predict(image)
    count = Counter(y_kmeans)
    centers = kmeans.cluster_centers_

    rgb_colors = []
    for i in count.keys():
        rgb_colors.append(centers[i])
    return count, rgb_colors


# obtain the percentage of colors from the given image
def get_color_percentages(image, number):
    count, rgb_colors = get_colors(image, number)

    hex_colors = []
    for i in count.keys():
        color = rgb_colors[i]
        hex_color = "#"
        for j in color:
            hex_color += ("{:02x}".format(int(j)))
        hex_colors.append(hex_color)

    sum_p = sum(list(count.values()))
    percentage = []
    for v in list(count.values()):
        percentage.append(round(v / sum_p, 2))

    print("The percentages of colors obtained from the image:")
    i = 0
    percentage_dic = {}
    while i < len(percentage):
        percentage_dic[hex_colors[i]] = percentage[i]
        print(hex_colors[i] + ": " + str(percentage[i] * 100) + " %")
        i += 1

    return percentage_dic


# get a palette from given image
def get_palette(image, number):
    count, rgb_colors = get_colors(image, number)

    hex_colors = []
    for i in count.keys():
        color = rgb_colors[i]
        hex_color = "#"
        for j in color:
            hex_color += ("{:02x}".format(int(j)))
        hex_colors.append(hex_color)

    print(hex_colors)
    return hex_colors


# get a complementary palette from given image
def get_complementary_palette(image, number):
    count, rgb_colors = get_colors(image, number)

    hex_colors = []
    for i in count.keys():
        color = 255 - rgb_colors[i]
        hex_color = "#"
        for j in color:
            hex_color += ("{:02x}".format(int(j)))
        hex_colors.append(hex_color)

    print(hex_colors)
    return hex_colors


# get a palette consisted of colors with the least percentages
def get_least_palette(image, number):
    percentage_dic = get_color_percentages(image, 2 * number)
    sorted_percentage_dic = sorted(percentage_dic.items(), key=lambda x: x[1])[:number]
    palette = []
    for i in sorted_percentage_dic:
        palette.append(i[0])

    print(palette)
    return palette


# get a palette consisted of colors with the most percentages
def get_most_palette(image, number):
    percentage_dic = get_color_percentages(image, 2 * number)
    sorted_percentage_dic = sorted(percentage_dic.items(), key=lambda x: x[1], reverse=True)[:number]
    palette = []
    for i in sorted_percentage_dic:
        palette.append(i[0])

    print(palette)
    return palette


# obtain a palette with similar colors from the given image
def get_similar_palette(image, number):
    count, rgb_colors = get_colors(image, number)
    palette = []

    print(palette)
    return palette


# obtain a palette with contrast colors from the given image
def get_contrast_palette(image, number):
    count, rgb_colors = get_colors(image, number)
    palette = []

    print(palette)
    return palette


def main():
    modified_image = load_image('download.jpg')
    percentage = get_color_percentages(modified_image, 5)
    palette = get_palette(modified_image, 5)
    complementary_palette = get_complementary_palette(modified_image, 5)
    least_palette = get_least_palette(modified_image, 3)
    most_palette = get_most_palette(modified_image, 3)
    similar_palette = get_similar_palette(modified_image, 5)
    contrast_palette = get_contrast_palette(modified_image, 5)


if __name__ == "__main__":
    main()
