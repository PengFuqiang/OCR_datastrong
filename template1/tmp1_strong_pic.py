#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\7\\29 0028

from PIL import Image
from PIL import ImageEnhance
import cv2
import random
import setup


def strong() :
    bright()
    color()
    contrast()
    sharp()
    # part_bright()


def bright() :
    args = setup.parser_args()
    for i in range(args.amount) :
        for j in range(args.num) :
            image = Image.open('template1\\tmp1_res\\rotate\\pic' + str(i) + '.jpg')
            # 亮度增强
            enh_bri = ImageEnhance.Brightness(image)
            cc1 = random.uniform(1.0 - args.bright_limit, 1.0 + args.bright_limit)  # 亮暗系数
            brightness = cc1
            image_brightened = enh_bri.enhance(brightness)
            image_brightened.save('template1\\tmp1_res\\bright\\pic' + str(i) + '_' + str(j) + '_bri.jpg')


def color() :
    args = setup.parser_args()
    for i in range(args.amount) :
        for j in range(args.num) :
            image = Image.open('template1\\tmp1_res\\rotate\\pic' + str(i) + '.jpg')
            # 色度增强
            enh_col = ImageEnhance.Color(image)
            cc2 = random.uniform(1.0 - args.color_limit, 1.0 + args.color_limit)  # 色度系数
            color_cc = cc2
            image_colored = enh_col.enhance(color_cc)
            image_colored.save('template1\\tmp1_res\\color\\pic' + str(i) + '_' + str(j) + '_col.jpg')


def contrast() :
    args = setup.parser_args()
    for i in range(args.amount) :
        for j in range(args.num) :
            image = Image.open('template1\\tmp1_res\\rotate\\pic' + str(i) + '.jpg')
            # 对比度增强
            enh_con = ImageEnhance.Contrast(image)
            cc3 = random.uniform(1.0 - args.contrast_limit, 1.0 + args.contrast_limit)  # 对比度系数
            contrast_cc = cc3
            image_contrasted = enh_con.enhance(contrast_cc)
            image_contrasted.save('template1\\tmp1_res\\contrast\\pic' + str(i) + '_' + str(j) + '_con.jpg')


def sharp() :
    args = setup.parser_args()
    for i in range(args.amount) :
        for j in range(args.num) :
            image = Image.open('template1\\tmp1_res\\rotate\\pic' + str(i) + '.jpg')
            # 锐度增强
            enh_sha = ImageEnhance.Sharpness(image)
            cc4 = random.uniform(2.0 - args.sharp_limit, 2.0 + args.sharp_limit)  # 锐度系数
            sharpness = cc4
            image_sharped = enh_sha.enhance(sharpness)
            image_sharped.save('template1\\tmp1_res\\sharp\\pic' + str(i) + '_' + str(j) + '_sha.jpg')


def part_bright() :
    args = setup.parser_args()
    for i in range(args.amount) :
        for j in range(args.num) :
            img = cv2.imread('template1\\tmp1_res\\rotate\\pic' + str(i) + '.jpg')
            #   指定区域变暗
            rows, cols, c = img.shape  # rows = height, cols = width
            dark = random.randint(-args.part_bright_coe, args.part_bright_coe)
            with open('template1\\tmp1_res\\txt\\pic' + str(i) + '.txt', 'r') as f :
                lines = f.readlines()
                tp = []
                for line in lines[8 : 12] :
                    temp1 = line.strip('\n')
                    temp2 = temp1.split(',')
                    tp.extend(temp2)
                # print(tp[0])
                x1 = min(int(float(tp[0])), int(float(tp[-9])))
                y1 = min(int(float(tp[1])), int(float(tp[3]))) - 50
                x2 = max(int(float(tp[2])), int(float(tp[-3])))
                y2 = max(int(float(tp[-4])), int(float(tp[-2])))
            for x in range(y1, y2) :
                for y in range(x1, x2) :
                    for z in range(c) :
                        if (img[x, y, z] + dark) > 255 :
                            img[x, y, z] = 255
                        elif (img[x, y, z] + dark) < 0 :
                            img[x, y, z] = 0
                        else :
                            img[x, y, z] += dark
            cv2.imwrite('template1\\tmp1_res\\part_bright\\pic' + str(i) + '_' + str(j) + '_part.jpg', img)


def adjust() :
    args = setup.parser_args()
    s_type = args.strong_type
    if s_type == 'bright' :
        bright()
    elif s_type == 'color' :
        color()
    elif s_type == 'contrast' :
        contrast()
    elif s_type == 'sharp' :
        sharp()
    elif s_type == 'part_bright' :
        part_bright()
    else :
        strong()
