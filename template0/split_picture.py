#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020/7/23 0023
import os
import shutil
import cv2 as cv


def split_to_box(img, time_str):
    """
    使用opencv进行图像分割，分割对象是添加到背景图片上的内容
    每个内容占用一个方框，以此框进行切割
    :param time_str:
    :param img: 要切割的图片，在main函数中定义   index: 要切割的图片的序号
    """
    dir_name = "template0\\res\\splits\\spl" + time_str
    if os.path.isdir(dir_name) :
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    # 先以切割发票代码进行举例
    # 要被切割的开始的像素的宽度值
    be_w = 344
    # 要被切割的结束的像素的宽度值
    end_w = 624
    # 要被切割的开始的像素的高度值
    be_h = 82
    # 要被切割的结束的像素的高度值
    end_h = 130
    dst_img = img[be_h: end_h, be_w: end_w]
    save_name = dir_name + '\\daima.jpg'
    # cv.imshow("dstImg", dst_img)
    cv.imwrite(save_name, dst_img)

    dst_img = img[110: 133, 1600: 1730]
    cv.imwrite(dir_name + '\\xiao_daima.jpg', dst_img)

    dst_img = img[88: 135, 1366: 1591]
    cv.imwrite(dir_name + '\\haoma.jpg', dst_img)

    dst_img = img[146: 174, 1585: 1707]
    cv.imwrite(dir_name + '\\xiao_haoma.jpg', dst_img)

    dst_img = img[191: 219, 1500: 1680]
    cv.imwrite(dir_name + '\\riqi.jpg', dst_img)

    dst_img = img[253: 282, 436: 750]
    cv.imwrite(dir_name + '\\goumaifang_name.jpg', dst_img)

    dst_img = img[290: 320, 461: 744]
    cv.imwrite(dir_name + '\\shibiehao.jpg', dst_img)

    dst_img = img[338: 362, 433: 978]
    cv.imwrite(dir_name + '\\goumaifang_dizhi.jpg', dst_img)

    dst_img = img[380: 409, 436: 912]
    cv.imwrite(dir_name + '\\goumaifang_yinhang.jpg', dst_img)

    dst_img = img[257: 290, 1127: 1693]
    cv.imwrite(dir_name + '\\mima1.jpg', dst_img)

    dst_img = img[290: 323, 1127: 1693]
    cv.imwrite(dir_name + '\\mima2.jpg', dst_img)

    dst_img = img[323: 356, 1127: 1693]
    cv.imwrite(dir_name + '\\mima3.jpg', dst_img)

    dst_img = img[356: 389, 1127: 1693]
    cv.imwrite(dir_name + '\\mima4.jpg', dst_img)

    dst_img = img[461: 488, 185: 575]
    cv.imwrite(dir_name + '\\huowu1.jpg', dst_img)

    dst_img = img[496: 523, 185: 575]
    cv.imwrite(dir_name + '\\huowu2.jpg', dst_img)

    dst_img = img[531: 558, 185: 575]
    cv.imwrite(dir_name + '\\huowu3.jpg', dst_img)

    dst_img = img[566: 593, 185: 575]
    cv.imwrite(dir_name + '\\huowu4.jpg', dst_img)

    dst_img = img[461: 488, 586: 790]
    cv.imwrite(dir_name + '\\guige1.jpg', dst_img)

    dst_img = img[496: 523, 586: 790]
    cv.imwrite(dir_name + '\\guige2.jpg', dst_img)

    dst_img = img[531: 558, 586: 790]
    cv.imwrite(dir_name + '\\guige3.jpg', dst_img)

    dst_img = img[566: 593, 586: 790]
    cv.imwrite(dir_name + '\\guige4.jpg', dst_img)

    dst_img = img[461: 488, 804: 830]
    cv.imwrite(dir_name + '\\danwei1.jpg', dst_img)

    dst_img = img[496: 523, 804: 852]
    cv.imwrite(dir_name + '\\danwei2.jpg', dst_img)

    dst_img = img[531: 558, 804: 852]
    cv.imwrite(dir_name + '\\danwei3.jpg', dst_img)

    dst_img = img[566: 593, 804: 852]
    cv.imwrite(dir_name + '\\danwei4.jpg', dst_img)

    dst_img = img[461: 488, 950: 1013]
    cv.imwrite(dir_name + '\\shuliang1.jpg', dst_img)

    dst_img = img[496: 523, 950: 1013]
    cv.imwrite(dir_name + '\\shuliang2.jpg', dst_img)

    dst_img = img[531: 558, 950: 1013]
    cv.imwrite(dir_name + '\\shuliang3.jpg', dst_img)

    dst_img = img[566: 593, 950: 1013]
    cv.imwrite(dir_name + '\\shuliang4.jpg', dst_img)

    dst_img = img[461: 488, 1091: 1172]
    cv.imwrite(dir_name + '\\danjia1.jpg', dst_img)

    dst_img = img[496: 523, 1091: 1172]
    cv.imwrite(dir_name + '\\danjia2.jpg', dst_img)

    dst_img = img[531: 558, 1091: 1172]
    cv.imwrite(dir_name + '\\danjia3.jpg', dst_img)

    dst_img = img[566: 593, 1091: 1172]
    cv.imwrite(dir_name + '\\danjia4.jpg', dst_img)

    dst_img = img[461: 488, 1292: 1435]
    cv.imwrite(dir_name + '\\jin_e1.jpg', dst_img)

    dst_img = img[496: 523, 1292: 1435]
    cv.imwrite(dir_name + '\\jin_e2.jpg', dst_img)

    dst_img = img[531: 558, 1292: 1435]
    cv.imwrite(dir_name + '\\jin_e3.jpg', dst_img)

    dst_img = img[566: 593, 1292: 1435]
    cv.imwrite(dir_name + '\\jin_e4.jpg', dst_img)

    dst_img = img[461: 488, 1480: 1521]
    cv.imwrite(dir_name + '\\shuilv1.jpg', dst_img)

    dst_img = img[496: 523, 1480: 1521]
    cv.imwrite(dir_name + '\\shuilv2.jpg', dst_img)

    dst_img = img[531: 558, 1480: 1521]
    cv.imwrite(dir_name + '\\shuilv3.jpg', dst_img)

    dst_img = img[566: 593, 1480: 1521]
    cv.imwrite(dir_name + '\\shuilv4.jpg', dst_img)

    dst_img = img[461: 488, 1624: 1730]
    cv.imwrite(dir_name + '\\shuie1.jpg', dst_img)

    dst_img = img[496: 523, 1624: 1730]
    cv.imwrite(dir_name + '\\shuie2.jpg', dst_img)

    dst_img = img[531: 558, 1624: 1730]
    cv.imwrite(dir_name + '\\shuie3.jpg', dst_img)

    dst_img = img[566: 593, 1624: 1730]
    cv.imwrite(dir_name + '\\shuie4.jpg', dst_img)

    dst_img = img[715: 745, 1214: 1429]
    cv.imwrite(dir_name + '\\jin_ezhihe.jpg', dst_img)

    dst_img = img[715: 745, 1541: 1753]
    cv.imwrite(dir_name + '\\shuie_zhihe.jpg', dst_img)

    dst_img = img[778: 803, 654: 1115]
    cv.imwrite(dir_name + '\\zonghe_daxie.jpg', dst_img)

    dst_img = img[781: 811, 1410: 1650]
    cv.imwrite(dir_name + '\\zonghe_xiaoxie.jpg', dst_img)

    dst_img = img[840: 870, 436: 750]
    cv.imwrite(dir_name + '\\xiaoshoufang_name.jpg', dst_img)

    dst_img = img[872: 902, 470: 830]
    cv.imwrite(dir_name + '\\xiaoshoufang_shibiehao.jpg', dst_img)

    dst_img = img[915: 945, 420: 965]
    cv.imwrite(dir_name + '\\xiaoshoufang_dizhi.jpg', dst_img)

    dst_img = img[950: 980, 420: 891]
    cv.imwrite(dir_name + '\\xiaoshoufang_yinhang.jpg', dst_img)

    dst_img = img[995: 1025, 305: 386]
    cv.imwrite(dir_name + '\\shoukuanren.jpg', dst_img)

    dst_img = img[995: 1025, 722: 803]
    cv.imwrite(dir_name + '\\fuhe.jpg', dst_img)

    dst_img = img[995: 1025, 1099: 1180]
    cv.imwrite(dir_name + '\\kaipiaoren.jpg', dst_img)
