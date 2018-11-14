
# -*- coding: utf-8 -*-
from PIL import Image
import PIL
from numpy.ma import array, zeros
import matplotlib.pyplot
from scipy.misc import imresize
import  graphcut
# 读取一幅图像，并从图像的两个矩形区域估算出类概率,然后创建一个图:

im = array(Image.open('empire.jpg'))
im = imresize(im,0.07,interp='bilinear')
size = im.shape[:2]
# 添加两个矩形训练区域
labels = zeros(size)
labels[3:18,3:18] = -1
labels[-18:-3,-18:-3] = 1
# 创建图
g = graphcut.build_bayes_graph(im,labels,kappa=1)
# 对图进行分割
res = graphcut.cut_graph(g,size)

figure()
graphcut.show_labeling(im,labels)
figure()
imshow(res)
gray()
axis('off')
show()