import os.path

def rename(img_folder):
    for img_name in os.listdir(img_folder):  # os.listdir()： 列出路径下所有的文件
        #os.path.join() 拼接文件路径
        src = os.path.join(img_folder, img_name)   #src：要修改的目录名
        dst = os.path.join(img_folder, img_name.split("_")[0] + '.png') #dst： 修改后的目录名      注意此处str(num)将num转化为字符串,继而拼接

        os.rename(src, dst) #用dst替代src\



def main():
    img_folder0 = r'D:\数据集\images2\test_latest\images' #图片的文件夹路径    直接放你的文件夹路径即可

    rename(img_folder0)

if __name__ == '__main__':
    main()