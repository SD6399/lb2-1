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


def convert(arrr):
    b = np.array([0.299, 0.587, 0.114])
    arrrr = arrr * b
    return arrrr

def minimal(color):
    mini = (np.amin(arr, axis=(0, 1)))[color]

    return mini

def limit_convert():

    arr_copy2[arr_copy2<100]=0


def histogr():
    b=[]
    b=arr_copy2.ravel()

    n, bin, patches = plt.hist(b, bins=20)
    plt.show()

# D:\dk\python\Lena.png
# path1 = input()
path1 = "D:\dk\python\Lena.png"
if (not os.path.isfile(path1)) and not ((path1 == "[0-9][a-z].jpg") or (path1 == "[0-9][a-z].jpg")):
    print("Введите корректный путь")

# print("111")
arr = np.asarray(Image.open(path1))

arr_copy = arr.copy()


# print(arr)




q = convert(arr_copy)
q = np.uint8(q)
res = minimal(0), maximal(0), average(0)
res1 = minimal(1), maximal(1), average(1)
res2 = minimal(2), maximal(2), average(2)
print("Миимальное, максимальное, среднее для канала R", res, "\nМиимальное, максимальное, среднее для канала G", res1,
      "\nМиимальное, максимальное, среднее для канала B", res2)

# Запись массива в изображение:
img = Image.fromarray((q))
img.save("D:\dk\python\Lena_grayscaled.png")


arr_copy2 = q.copy()

limit_convert()

img2 = Image.fromarray(arr_copy2)
img2.save("D:\dk\python\Lena_thresholded.png")

histogr()
