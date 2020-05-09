"""
Python3通过OpenCV对比图片相似度_Python_u014259820的博客-CSDN博客
https://blog.csdn.net/u014259820/article/details/82889752
"""

from skimage.measure import compare_ssim
import cv2


class CompareImage():

    def compare_image(self, path_image1, path_image2):

        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)
        return self.compare_gray(imageA, imageB)

    def compare_gray(self, imageA, imageB):
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        # print("SSIM: {}".format(score))
        return score


if __name__ == "__main__":
    compare_image = CompareImage()
    compare_image.compare_image("../test/1-1.jpg", "../test/1-2.jpg")
    compare_image.compare_image("../test/2-1.jpg", "../test/2-2.jpg")
    compare_image.compare_image("../test/1-1.jpg", "../test/2-1.jpg")
    compare_image.compare_image("../test/ppt1.PNG", "../test/ppt2.PNG")
    compare_image.compare_image("../test/ppt2.PNG", "../test/ppt3.PNG")
    compare_image.compare_image("../test/ppt3.PNG", "../test/ppt4.PNG")
