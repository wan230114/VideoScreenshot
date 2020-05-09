# 来源参考：
# Python首先视频帧截图,并保存图片_python_kuronekonano的博客-CSDN博客
# https://blog.csdn.net/kuronekonano/article/details/90766475

import cv2


def VideoCut(filename, spend):
    # 使用opencv按一定间隔截取视频帧，并保存为图片

    vc = cv2.VideoCapture(filename)  # 读取视频文件
    c = 0
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
        yield vc.get(7)  # 总帧数
    else:
        rval = False
    timeF = spend  # 视频帧计数间隔频率
    while rval:  # 循环读取视频帧
        # print(rval, frame)
        # print(c, timeF, c % timeF)
        if (c % timeF == 0):  # 每隔timeF帧进行存储操作
            # print("write...")
            # cv2.imwrite('../testout/all/%03d.jpg' % c, frame)  # 存储为图像
            yield c, frame
            # print("success!")
        c = c + 1
        rval, frame = vc.read()
    cv2.waitKey(1)
    vc.release()


if __name__ == "__main__":
    for x in VideoCut('../test/ppt_video.mp4', 1):
        # print(x)
        pass
