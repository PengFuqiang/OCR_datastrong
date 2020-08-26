#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\7\\29 0029

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
    dir_name = "template1\\tmp1_res\\splits\\spl" + str(index)
    if os.path.isdir(dir_name) :
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    # 先以切割发票代码进行举例
    # 要被切割的开始的像素的宽度值
    be_w = 275
    # 要被切割的结束的像素的宽度值
    end_w = 560
    # 要被切割的开始的像素的高度值
    be_h = 82
    # 要被切割的结束的像素的高度值
    end_h = 134
    dst_img = img[be_h : end_h, be_w : end_w]
    save_name = dir_name + '\\daima.jpg'
    # cv.imshow("dstImg", dst_img)
    cv.imwrite(save_name, dst_img)

    dst_img = img[102 : 125, 1585 : 1720]
    cv.imwrite(dir_name + '\\xiao_daima.jpg', dst_img)

    dst_img = img[82 : 129, 1326 : 1551]
    cv.imwrite(dir_name + '\\haoma.jpg', dst_img)

    dst_img = img[138 : 166, 1563 : 1685]
    cv.imwrite(dir_name + '\\xiao_haoma.jpg', dst_img)

    dst_img = img[187 : 215, 1477 : 1684]
    cv.imwrite(dir_name + '\\riqi.jpg', dst_img)

    dst_img = img[250 : 280, 373 : 750]
    cv.imwrite(dir_name + '\\goumaifang_name.jpg', dst_img)

    dst_img = img[291 : 321, 405 : 688]
    cv.imwrite(dir_name + '\\shibiehao.jpg', dst_img)

    dst_img = img[335 : 359, 373 : 918]
    cv.imwrite(dir_name + '\\goumaifang_dizhi.jpg', dst_img)

    dst_img = img[372 : 402, 373 : 912]
    cv.imwrite(dir_name + '\\goumaifang_yinhang.jpg', dst_img)

    dst_img = img[260 : 294, 1093 : 1659]
    cv.imwrite(dir_name + '\\mima1.jpg', dst_img)

    dst_img = img[293 : 327, 1093 : 1659]
    cv.imwrite(dir_name + '\\mima2.jpg', dst_img)

    dst_img = img[326 : 359, 1093 : 1659]
    cv.imwrite(dir_name + '\\mima3.jpg', dst_img)

    dst_img = img[359 : 392, 1093 : 1659]
    cv.imwrite(dir_name + '\\mima4.jpg', dst_img)

    dst_img = img[465 : 495, 112 : 460]
    cv.imwrite(dir_name + '\\huowu1.jpg', dst_img)

    dst_img = img[495 : 525, 112 : 460]
    cv.imwrite(dir_name + '\\huowu2.jpg', dst_img)

    dst_img = img[525 : 555, 112 : 460]
    cv.imwrite(dir_name + '\\huowu3.jpg', dst_img)

    dst_img = img[555 : 585, 112 : 460]
    cv.imwrite(dir_name + '\\huowu4.jpg', dst_img)

    dst_img = img[465 : 495, 519 : 589]
    cv.imwrite(dir_name + '\\guige1.jpg', dst_img)

    dst_img = img[465 : 495, 519 : 589]
    cv.imwrite(dir_name + '\\guige2.jpg', dst_img)

    dst_img = img[465 : 495, 519 : 589]
    cv.imwrite(dir_name + '\\guige3.jpg', dst_img)

    dst_img = img[465 : 495, 519 : 589]
    cv.imwrite(dir_name + '\\guige4.jpg', dst_img)

    dst_img = img[465 : 495, 760 : 786]
    cv.imwrite(dir_name + '\\danwei1.jpg', dst_img)

    dst_img = img[495 : 525, 760 : 786]
    cv.imwrite(dir_name + '\\danwei2.jpg', dst_img)

    dst_img = img[525 : 555, 760 : 786]
    cv.imwrite(dir_name + '\\danwei3.jpg', dst_img)

    dst_img = img[525 : 555, 760 : 786]
    cv.imwrite(dir_name + '\\danwei4.jpg', dst_img)

    dst_img = img[465 : 495, 865 : 970]
    cv.imwrite(dir_name + '\\shuliang1.jpg', dst_img)

    dst_img = img[495 : 525, 865 : 970]
    cv.imwrite(dir_name + '\\shuliang2.jpg', dst_img)

    dst_img = img[525 : 555, 865 : 970]
    cv.imwrite(dir_name + '\\shuliang3.jpg', dst_img)

    dst_img = img[555 : 585, 865 : 970]
    cv.imwrite(dir_name + '\\shuliang4.jpg', dst_img)

    dst_img = img[465 : 495, 1030 : 1142]
    cv.imwrite(dir_name + '\\danjia1.jpg', dst_img)

    dst_img = img[495 : 525, 1030 : 1142]
    cv.imwrite(dir_name + '\\danjia2.jpg', dst_img)

    dst_img = img[525 : 555, 1030 : 1142]
    cv.imwrite(dir_name + '\\danjia3.jpg', dst_img)

    dst_img = img[555 : 585, 1030 : 1142]
    cv.imwrite(dir_name + '\\danjia4.jpg', dst_img)

    dst_img = img[465 : 495, 1230 : 1385]
    cv.imwrite(dir_name + '\\jin_e1.jpg', dst_img)

    dst_img = img[495 : 525, 1230 : 1385]
    cv.imwrite(dir_name + '\\jin_e2.jpg', dst_img)

    dst_img = img[525 : 555, 1230 : 1385]
    cv.imwrite(dir_name + '\\jin_e3.jpg', dst_img)

    dst_img = img[555 : 585, 1230 : 1385]
    cv.imwrite(dir_name + '\\jin_e4.jpg', dst_img)

    dst_img = img[465 : 495, 1435 : 1476]
    cv.imwrite(dir_name + '\\shuilv1.jpg', dst_img)

    dst_img = img[495 : 525, 1435 : 1476]
    cv.imwrite(dir_name + '\\shuilv2.jpg', dst_img)

    dst_img = img[525 : 555, 1435 : 1476]
    cv.imwrite(dir_name + '\\shuilv3.jpg', dst_img)

    dst_img = img[555 : 585, 1435 : 1476]
    cv.imwrite(dir_name + '\\shuilv4.jpg', dst_img)

    dst_img = img[465 : 495, 1587 : 1717]
    cv.imwrite(dir_name + '\\shuie1.jpg', dst_img)

    dst_img = img[495 : 525, 1587 : 1717]
    cv.imwrite(dir_name + '\\shuie2.jpg', dst_img)

    dst_img = img[525 : 555, 1587 : 1717]
    cv.imwrite(dir_name + '\\shuie3.jpg', dst_img)

    dst_img = img[555 : 585, 1587 : 1717]
    cv.imwrite(dir_name + '\\shuie4.jpg', dst_img)

    dst_img = img[741 : 771, 1179 : 1400]
    cv.imwrite(dir_name + '\\jin_ezhihe.jpg', dst_img)

    dst_img = img[741 : 771, 1511 : 1721]
    cv.imwrite(dir_name + '\\shuie_zhihe.jpg', dst_img)

    dst_img = img[798 : 828, 598 : 1098]
    cv.imwrite(dir_name + '\\zonghe_daxie.jpg', dst_img)

    dst_img = img[796 : 829, 1400 : 1678]
    cv.imwrite(dir_name + '\\zonghe_xiaoxie.jpg', dst_img)

    dst_img = img[860 : 890, 373 : 750]
    cv.imwrite(dir_name + '\\xiaoshoufang_name.jpg', dst_img)

    dst_img = img[898 : 928, 406 : 766]
    cv.imwrite(dir_name + '\\xiaoshoufang_shibiehao.jpg', dst_img)

    dst_img = img[940 : 970, 373 : 980]
    cv.imwrite(dir_name + '\\xiaoshoufang_dizhi.jpg', dst_img)

    dst_img = img[978 : 1008, 373 : 992]
    cv.imwrite(dir_name + '\\xiaoshoufang_yinhang.jpg', dst_img)

    dst_img = img[1026 : 1056, 246 : 327]
    cv.imwrite(dir_name + '\\shoukuanren.jpg', dst_img)

    dst_img = img[1026 : 1056, 670 : 751]
    cv.imwrite(dir_name + '\\fuhe.jpg', dst_img)

    dst_img = img[1026 : 1056, 1060 : 1141]
    cv.imwrite(dir_name + '\\kaipiaoren.jpg', dst_img)



