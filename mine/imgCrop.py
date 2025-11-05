from PIL import Image, ImageEnhance
import cv2 as cv
import random as rng
import numpy as np
import os


root = "img"


def dirTree(root, tree):
    tree.append(root)
    for i in os.listdir(root):
        brench = os.path.join(root, i)
        if os.path.isdir(brench):
            dirTree(brench, tree)
    return tree


def main():
    tree = []
    tree = dirTree(root, tree)
    images = [".jpg", ".jpeg", ".png"]
    prefix = "new"

    makeNewDir(tree, prefix)

    for direct in tree:
        for f in os.listdir(direct):
            path = os.path.join(direct, f)
            if os.path.isfile(path):
                name, ext = os.path.splitext(path)
                if ext in images:
                    img_crop = image_crop(path)
                    saveImage(img_crop, path, prefix)


def makeNewDir(tree, prefix):
    if not os.path.exists(prefix):
        os.mkdir(prefix)

    for f in tree:
        path = os.path.join(prefix, f)
        if not os.path.exists(path):
            os.mkdir(path)


def image_crop(image_path, prefix):
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    threshold = 100
    canny_output = cv.Canny(img, threshold, threshold * 2)
    drawing = np.zeros(
        (canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8
    )

    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(
            drawing,
            (int(boundRect[i][0]), int(boundRect[i][1])),
            (
                int(boundRect[i][0] + boundRect[i][2]),
                int(boundRect[i][1] + boundRect[i][3]),
            ),
            color,
            2,
        )

    # cv.imshow('c', drawing)
    # cv.waitKey(10)

    xMin, yMin = 10000, 10000
    xMax, yMax = 0, 0

    for i in boundRect:
        if xMin > i[0]:
            xMin = i[0]
        if xMax < i[0] + i[2]:
            xMax = i[0] + i[2]
        if yMin > i[1]:
            yMin = i[1]
        if yMax < i[1] + i[3]:
            yMax = i[1] + i[3]

    padX = 10
    padY = 10
    im = Image.open(image_path)
    w = im.width
    h = im.height

    pL = xMin - padX if xMin >= padX else xMin
    pR = xMax + padX if xMax + padX <= w else xMax
    pUp = yMin - padY if yMin > padY else yMin
    pLow = yMax + padY if yMax + padY <= h else yMax

    (left, upper, right, lower) = (pL, pUp, pR, pLow)
    im_crop = im.crop((left, upper, right, lower))
    return im_crop
    # im_crop.show()


def saveImage(image, image_path, prefix):
    new_path = os.path.join(prefix, image_path)
    image.save(new_path)


main()
