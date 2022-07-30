import os
import time
class BatchRename():

    #根据自己的名字，修改 dst = os.path.join(os.path.abspath(self.path), 'cyz'+format(str(i), '0>7s') +'.jpg')中的 “cyz”
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = r'C:\Users\Cheny\Desktop\footimage\baidu'  #表示需要命名处理的文件夹

    def rename(self):
        filelist = os.listdir(self.path)   #获取文件路径
        total_num = len(filelist)  #获取文件长度（个数）
        startnum = 1  #表示文件的命名是从1开始的
        nowtime=int(time.strftime("%m%d",time.localtime())) #获取当前日期并转化为整形
        print(nowtime)
        i=nowtime*10000+startnum    #将时间乘10000以获得4位0用于文件命名。
        for item in filelist:
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), 'cyz'+format(str(i), '0>7s') +'.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.png'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),  'cyz'+format(str(i), '0>7s') + '.png')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.jpeg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),  'cyz'+format(str(i), '0>7s') + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
            if item.endswith('.webp'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),  'cyz'+format(str(i), '0>7s') + '.jpg')#处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()