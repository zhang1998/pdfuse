from PIL import Image
from pylab import *
# 读取图像到数组中
im = array(Image.open('empire.jpg').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
