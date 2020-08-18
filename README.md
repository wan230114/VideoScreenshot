# VideoScreenshot
打开视频文件进行按照不同画面自动截图，适用于众多PPT讲解视频截取PPT图片

## 准备

提前安装Python库
```bash
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
pip install Pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## 使用方法

```
usage: vshot.py [-h] [-o OUTDIR] [-S SIMILARITY] [-s SPEND] [-m METHOD]
                VideoFilePath

用于自动从视频截取不同图片

positional arguments:
  VideoFilePath         输入文件, filepath

optional arguments:
  -h, --help            show this help message and exit
  -o OUTDIR, --outdir OUTDIR
                        输出文件夹路径, dirpath
  -S SIMILARITY, --Similarity SIMILARITY
                        相似度参数, 默认低于0.98进行截取, float
  -s SPEND, --spend SPEND
                        间隔帧数, int
  -m METHOD, --method METHOD
                        使用算法, 0,1,2对应均值、差值、感知哈希算法, 
                        3,4对应三直方图算法和单通道的直方图,
                        5为ssim(注:该算法效率最低)
```

```python
python vshot.py ./test/ppt_video.mp4 -o ./Testout/ -s 10 -S 0.97
```

## 其他工具

[DupImageFinder](./other_tools/DupImageFinder/) 用于对于截取的众多图片，进行二次去重。(先点击reg注册)
