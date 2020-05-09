import argparse
from pkg.comp_img import *
from pkg.comp_ski import CompareImage
from pkg.read_video import VideoCut
import os

compare_image = CompareImage()


def fargv():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('用于自动从视频截取不同图片'),
        epilog=(''))
    parser.add_argument('VideoFilePath', type=str,
                        help=('输入文件, filepath'))
    parser.add_argument('-o', '--outdir', type=str, default='./',
                        help=('输出文件夹路径, dirpath'))
    parser.add_argument('-S', '--Similarity', type=float, default=0.92,
                        help=('相似度参数, float'))
    parser.add_argument('-s', '--spend', type=int, default=30,
                        help=('间隔帧数, int'))
    parser.add_argument('-m', '--method', type=int, default=1,
                        help=('使用算法, 0/1'))
    # parser.add_argument('--keep', action='store_true', default=False,
    #                     help='是否怎样怎样')
    # 参数组，只能选择其中一个
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('-m1', help=('模式1'))
    # group.add_argument('-m2', help=('模式2'))
    # group.add_argument('-m3', help=('模式3'))
    args = parser.parse_args()
    print(args)
    return args.__dict__


def runAllImageSimilaryFun(img1, img2):
    # 均值、差值、感知哈希算法三种算法值越小，则越相似,相同图片值为0
    # 三直方图算法和单通道的直方图 0-1之间，值越大，越相似。 相同图片为1

    # t1,t2   14;19;10;  0.70;0.75
    # t1,t3   39 33 18   0.58 0.49
    # s1,s2  7 23 11     0.83 0.86  挺相似的图片
    # c1,c2  11 29 17    0.30 0.31
    hash1 = aHash(img1)
    hash2 = aHash(img2)
    n1 = cmpHash(hash1, hash2)
    # print('均值哈希算法相似度aHash：', n1)

    hash1 = dHash(img1)
    hash2 = dHash(img2)
    n2 = cmpHash(hash1, hash2)
    # print('差值哈希算法相似度dHash：', n2)

    hash1 = pHash(img1)
    hash2 = pHash(img2)
    n3 = cmpHash(hash1, hash2)
    # print('感知哈希算法相似度pHash：', n3)

    n4 = classify_hist_with_split(img1, img2)
    # print('三直方图算法相似度：', n4)

    n5 = calculate(img1, img2)
    # print("单通道的直方图", n5)
    # print("%d %d %d %.2f %.2f " % (n1, n2, n3, round(n4[0], 2), n5[0]))
    print("%.2f %.2f %.2f %.2f %.2f " % (
        1 - float(n1 / 64),
        1 - float(n2 / 64),
        1 - float(n3 / 64),
        n4,
        n5))


def comp(img1, img2, method=0):
    # 均值、差值、感知哈希算法三种算法值越小，则越相似,相同图片值为0
    # 三直方图算法和单通道的直方图 0-1之间，值越大，越相似。 相同图片为1
    if method == 0:
        n5 = compare_image.compare_gray(img1, img2)
        return n5
    else:
        n5 = classify_hist_with_split(img1, img2)
        if n5 < 1:
            return n5[0]
        else:
            return n5


def mydo(VideoFilePath, outdir, Similarity, spend, method=0):
    os.makedirs(outdir, exist_ok=True)
    ITERS = VideoCut(VideoFilePath, spend)
    num_frames_all = next(ITERS)
    print('视频总帧数:', num_frames_all)
    num_frames_all_N = len(str(int(num_frames_all)))
    mod = outdir + '/%%0%dd.jpg' % num_frames_all_N

    # 开始
    num_frames, frame = next(ITERS)
    cv2.imwrite(mod % num_frames, frame)  # 截取第一张
    for num_frames_new, frame_new in ITERS:
        result = comp(frame, frame_new, method=1)
        print('[%.3f%%]' % (num_frames_new/num_frames_all*100),
              num_frames, num_frames_new,
              mod % num_frames_new, result, result < Similarity)
        if result < Similarity:
            runAllImageSimilaryFun(frame, frame_new)
            cv2.imwrite(mod % num_frames_new, frame_new)  # 截取不同
            num_frames, frame = num_frames_new, frame_new



def main():
    # sys.argv = '1 -l listfile -i file -n 1,2'.split()
    # sys.argv = ['', '-h']
    args = fargv()
    # print(*list(args.keys()), sep=", ")
    # print(*list(args.values()), sep=", ")
    mydo(**args)


if __name__ == '__main__':
    main()
    # mydo('./test/ppt_video.mp4', './testout', 0.99985, 15)
    # mydo('./test/ppt_video.mp4', './testout', 0.92, 1, 1)
