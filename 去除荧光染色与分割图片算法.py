import os
#此py文件去除不需要的生成图片，如荧光染色图片等
path=r"D:\数据集\images2\test_latest\images"
pics=os.listdir(path)
for pic in pics:
    pp=pic.split(".")[0]
    if(len(pp.split("_"))>3):
        if int(pp.split("_")[3])!=2:
           os.remove(os.path.join(path,pic))
    elif (len(pp.split("_"))<=3):
        os.remove(os.path.join(path, pic))