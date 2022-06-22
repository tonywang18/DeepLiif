from PIL import Image
import os
import numpy as np
import skimage.io  as io
#path路径是要拼接对的图片路径
path="D:\数据集\IHC训练集\mix_pic"
#path1路径是要拼接对的图片路径
path1="D:\数据集\images1"
#此py文件将单张图片处理为6张相同图片水平拼接的输入图片（512*512）
pic_names=os.listdir(path)
for pic_name in pic_names:
    # a=cv2.imread(path+pic_name)
    # a1=cv2.imread(path+pic_name)
    a=np.array(Image.open(os.path.join(path,pic_name)))

    a1= np.array(Image.open(os.path.join(path, pic_name)))
    a2=np.hstack((a,a1))

    for i in range(4):
        a2=np.hstack((a2,a))
    io.imsave(os.path.join(path1,pic_name),a2)
