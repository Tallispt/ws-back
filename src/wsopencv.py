import cv2 as cv
from utils.image_utils import resize_img, manipulate_img, detect_contours, cut_warp_image, cut_spots
from utils.base64_utils import readb64, encode64
from data import data as base
img = cv.imread("src/imgs/IMG_1858.jpg")

def detect_sensor_by_image(image):
    img = resize_img(image)
    canny = manipulate_img(img)
    drawn, contour = detect_contours(img, canny)
    output = cut_warp_image(image, contour)
    base64 = encode64(output)
    return base64, [canny, drawn, output]

def detect_sensor_by_base64(base64):
    image = readb64(base64)
    return detect_sensor_by_image(image)

base64, image_array = detect_sensor_by_base64(base)
# base64, image_array = detect_sensor_by_image(img)
# for i in image_array:
#     cv.namedWindow("output window", cv.WINDOW_KEEPRATIO)
#     cv.imshow("output window", i)
#     cv.waitKey(0)

spots = cut_spots(image_array[2])

# preto e branco, blur e circle detection
for i in spots:
    canny = manipulate_img(i, (21,21), 0.9)
    cv.namedWindow("output window", cv.WINDOW_KEEPRATIO)
    cv.imshow("output window", canny)
    cv.waitKey(0)

# Aplicar mascara no circulo utilizando ponto central e 0,7 do raio

# Fazer média dos pontos e extrair um array final ordenado com replicadas, RGB, CMYK, HSV, Euclidian distance