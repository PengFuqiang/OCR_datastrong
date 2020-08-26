#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\7\\30 0030
import os
import shutil
import cv2 as cv


def split_to_box(img, index) :
    """
    使用opencv进行图像分割，分割对象是添加到背景图片上的内容
    每个内容占用一个方框，以此框进行切割
    :param index:
    :param img: 要切割的图片，在main函数中定义   index: 要切割的图片的序号
    """
    dir_name = "template2\\tmp2_res\\splits\\spl" + str(index)
    if os.path.isdir(dir_name) :
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    # 先以切割发票代码进行举例
    # 要被切割的开始的像素的宽度值
    be_w = 250
    # 要被切割的结束的像素的宽度值
    end_w = 555
    # 要被切割的开始的像素的高度值
    be_h = 84
    # 要被切割的结束的像素的高度值
    end_h = 132
    dst_img = img[be_h : end_h, be_w : end_w]
    save_name = dir_name + '\\daima.jpg'
    # cv.imshow("dstImg", dst_img)
    cv.imwrite(save_name, dst_img)

    dst_img = img[114 : 136, 1594 : 1763]
    cv.imwrite(dir_name + '\\xiao_daima.jpg', dst_img)

    dst_img = img[82 : 129, 1326 : 1551]
    cv.imwrite(dir_name + '\\haoma.jpg', dst_img)

    dst_img = img[148 : 175, 1574 : 1736]
    cv.imwrite(dir_name + '\\xiao_haoma.jpg', dst_img)

    dst_img = img[196 : 226, 1480 : 1714]
    cv.imwrite(dir_name + '\\riqi.jpg', dst_img)

    dst_img = img[254 : 284, 365 : 711]
    cv.imwrite(dir_name + '\\goumaifang_name.jpg', dst_img)

    dst_img = img[298 : 328, 386 : 756]
    cv.imwrite(dir_name + '\\shibiehao.jpg', dst_img)

    dst_img = img[350 : 374, 354 : 900]
    cv.imwrite(dir_name + '\\goumaifang_dizhi.jpg', dst_img)

    dst_img = img[388 : 428, 354 : 840]
    cv.imwrite(dir_name + '\\goumaifang_yinhang.jpg', dst_img)

    dst_img = img[268 : 301, 1100 : 1700]
    cv.imwrite(dir_name + '\\mima1.jpg', dst_img)

    dst_img = img[301 : 334, 1100 : 1700]
    cv.imwrite(dir_name + '\\mima2.jpg', dst_img)

    dst_img = img[334 : 367, 1100 : 1700]
    cv.imwrite(dir_name + '\\mima3.jpg', dst_img)

    dst_img = img[367 : 400, 1100 : 1700]
    cv.imwrite(dir_name + '\\mima4.jpg', dst_img)

    dst_img = img[476 : 505, 92 : 440]
    cv.imwrite(dir_name + '\\huowu1.jpg', dst_img)

    dst_img = img[506 : 535, 92 : 440]
    cv.imwrite(dir_name + '\\huowu2.jpg', dst_img)

    dst_img = img[536 : 565, 92 : 440]
    cv.imwrite(dir_name + '\\huowu3.jpg', dst_img)

    dst_img = img[566 : 596, 92 : 440]
    cv.imwrite(dir_name + '\\huowu4.jpg', dst_img)

    dst_img = img[476 : 505, 536 : 606]
    cv.imwrite(dir_name + '\\guige1.jpg', dst_img)

    dst_img = img[506 : 535, 536 : 606]
    cv.imwrite(dir_name + '\\guige2.jpg', dst_img)

    dst_img = img[536 : 565, 536 : 606]
    cv.imwrite(dir_name + '\\guige3.jpg', dst_img)

    dst_img = img[566 : 596, 536 : 606]
    cv.imwrite(dir_name + '\\guige4.jpg', dst_img)

    dst_img = img[476 : 505, 740 : 766]
    cv.imwrite(dir_name + '\\danwei1.jpg', dst_img)

    dst_img = img[506 : 535, 740 : 766]
    cv.imwrite(dir_name + '\\danwei2.jpg', dst_img)

    dst_img = img[536 : 565, 740 : 766]
    cv.imwrite(dir_name + '\\danwei3.jpg', dst_img)

    dst_img = img[566 : 596, 740 : 766]
    cv.imwrite(dir_name + '\\danwei4.jpg', dst_img)

    dst_img = img[476 : 505, 850 : 970]
    cv.imwrite(dir_name + '\\shuliang1.jpg', dst_img)

    dst_img = img[506 : 535, 850 : 970]
    cv.imwrite(dir_name + '\\shuliang2.jpg', dst_img)

    dst_img = img[536 : 565, 850 : 970]
    cv.imwrite(dir_name + '\\shuliang3.jpg', dst_img)

    dst_img = img[566 : 596, 850 : 970]
    cv.imwrite(dir_name + '\\shuliang4.jpg', dst_img)

    dst_img = img[476 : 505, 1024 : 1142]
    cv.imwrite(dir_name + '\\danjia1.jpg', dst_img)

    dst_img = img[506 : 535, 1024 : 1142]
    cv.imwrite(dir_name + '\\danjia2.jpg', dst_img)

    dst_img = img[536 : 565, 1024 : 1142]
    cv.imwrite(dir_name + '\\danjia3.jpg', dst_img)

    dst_img = img[566 : 596, 1024 : 1142]
    cv.imwrite(dir_name + '\\danjia4.jpg', dst_img)

    dst_img = img[476 : 505, 1218 : 1400]
    cv.imwrite(dir_name + '\\jin_e1.jpg', dst_img)

    dst_img = img[506 : 535, 1218 : 1400]
    cv.imwrite(dir_name + '\\jin_e2.jpg', dst_img)

    dst_img = img[536 : 565, 1218 : 1400]
    cv.imwrite(dir_name + '\\jin_e3.jpg', dst_img)

    dst_img = img[566 : 596, 1218 : 1400]
    cv.imwrite(dir_name + '\\jin_e4.jpg', dst_img)

    dst_img = img[476 : 505, 1425 : 1485]
    cv.imwrite(dir_name + '\\shuilv1.jpg', dst_img)

    dst_img = img[506 : 535, 1425 : 1485]
    cv.imwrite(dir_name + '\\shuilv2.jpg', dst_img)

    dst_img = img[536 : 565, 1425 : 1485]
    cv.imwrite(dir_name + '\\shuilv3.jpg', dst_img)

    dst_img = img[566 : 596, 1425 : 1485]
    cv.imwrite(dir_name + '\\shuilv4.jpg', dst_img)

    dst_img = img[476 : 505, 1580 : 1740]
    cv.imwrite(dir_name + '\\shuie1.jpg', dst_img)

    dst_img = img[506 : 535, 1580 : 1740]
    cv.imwrite(dir_name + '\\shuie2.jpg', dst_img)

    dst_img = img[536 : 565, 1580 : 1740]
    cv.imwrite(dir_name + '\\shuie3.jpg', dst_img)

    dst_img = img[566 : 596, 1580 : 1740]
    cv.imwrite(dir_name + '\\shuie4.jpg', dst_img)

    dst_img = img[748 : 778, 1172 : 1390]
    cv.imwrite(dir_name + '\\jin_ezhihe.jpg', dst_img)

    dst_img = img[748 : 778, 1518 : 1730]
    cv.imwrite(dir_name + '\\shuie_zhihe.jpg', dst_img)

    dst_img = img[812 : 842, 590 : 1050]
    cv.imwrite(dir_name + '\\zonghe_daxie.jpg', dst_img)

    dst_img = img[812 : 842, 1434 : 1674]
    cv.imwrite(dir_name + '\\zonghe_xiaoxie.jpg', dst_img)

    dst_img = img[875 : 905, 350 : 782]
    cv.imwrite(dir_name + '\\xiaoshoufang_name.jpg', dst_img)

    dst_img = img[912 : 942, 392 : 752]
    cv.imwrite(dir_name + '\\xiaoshoufang_shibiehao.jpg', dst_img)

    dst_img = img[960 : 990, 350 : 895]
    cv.imwrite(dir_name + '\\xiaoshoufang_dizhi.jpg', dst_img)

    dst_img = img[998 : 1028, 350 : 821]
    cv.imwrite(dir_name + '\\xiaoshoufang_yinhang.jpg', dst_img)

    dst_img = img[1044 : 1074, 220 : 301]
    cv.imwrite(dir_name + '\\shoukuanren.jpg', dst_img)

    dst_img = img[1044 : 1074, 660 : 741]
    cv.imwrite(dir_name + '\\fuhe.jpg', dst_img)

    dst_img = img[1044 : 1074, 1055 : 1136]
    cv.imwrite(dir_name + '\\kaipiaoren.jpg', dst_img)
