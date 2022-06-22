import numpy as np
import imageio
import cv2
import os
import PIL.Image as image
# result_path=r"C:\Users\22691\Desktop\deepliif_threechannel\\"
path=r"D:\数据集\需要拆解出细胞核通道的图片\\"
list=os.listdir(path)
for pic_name in list:
    im=image.open(path+pic_name)
    a=np.array(im)
    b=a.copy()
    c=a.copy()

    three_channel=np.stack([a,b,c],axis=-1)
    three=three_channel.reshape(512,512,3)

    imageio.imsave(r"D:\数据集\deepliif_threechannel\{}".format(pic_name),three)