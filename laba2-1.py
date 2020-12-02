from PIL import Image
import numpy as np
import os.path
from matplotlib import pyplot as plt
from numpy import array


def maximal(color):
    maxi = (np.amax(arr, axis=(0, 1)))[color]
    return maxi


def average(color):
    summa = np.average(arr, axis=(0, 1))[color]
    return summa


def convert(array1):
    b = np.array([0.299, 0.587, 0.114])
    array2 = array1 * b
    return array2


def minimal(color):
    mini = (np.amin(arr, axis=(0, 1)))[color]

    return mini


def limit_convert():
    arr_copy2[arr_copy2 < 100] = 0


def histogram():
    b = []
    b = arr_copy2.ravel()

    n, bin, patches = plt.hist(b, bins=20, color='red')
    plt.title('Распределения яркости изображения', size=20)
    plt.xlabel('Уровень яркости', size=16)
    plt.ylabel('Пиксель', size=16)
    plt.show()


# D:\dk\python\Lena.png
# path1 = input()

path1 = "D:\dk\python\Lena.png"
if (not os.path.isfile(path1)) and not (path1 == "[0-9][a-z].png"):
    print("Введите корректный путь")

arr = np.asarray(Image.open(path1))
arr_copy = arr.copy()


new_arr = convert(arr_copy)
new_arr = np.uint8(new_arr)
res = minimal(0), maximal(0), average(0)
res1 = minimal(1), maximal(1), average(1)
res2 = minimal(2), maximal(2), average(2)
print("Миимальное, максимальное, среднее для канала R", res, "\nМиимальное, максимальное, среднее для канала G", res1,
      "\nМиимальное, максимальное, среднее для канала B", res2)

# Запись массива в изображение:
img = Image.fromarray((new_arr))
img.save("D:\dk\python\Lena_grayscaled.png")

arr_copy2 = new_arr.copy()

limit_convert()

img2 = Image.fromarray(arr_copy2)
img2.save("D:\dk\python\Lena_thresholded.png")

histogram()
