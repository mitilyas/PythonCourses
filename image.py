from PIL import Image
import numpy as np


def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.array(img)
    return data


def save_l_image(npdata, outfilename):
    img = Image.fromarray(npdata)
    img = img.convert('L')
    img.save(outfilename)


def save_image(npdata, outfilename):
    img = Image.fromarray(npdata.astype(np.uint8))
    img.save(outfilename)


filename = input("Введите путь к файлу: ")
arr = load_image(filename)
l_image = input("Введите путь, по которому сохранится полутоновое изображение: ")
b = np.array([0.299, 0.587, 0.114])
arr = (arr*b)
save_image(np.sum(arr, axis=2), l_image)
# Преобразование в Lena_thresholded.png
arr = load_image(l_image)
arr[arr < 50] = 0
img = Image.fromarray(arr)
print("Полученная гистограмма яркости изображения")
print(img.histogram())
t_image = input("Введите путь, по которому сохранится пороговое изображение: ")
save_image(arr, t_image)
