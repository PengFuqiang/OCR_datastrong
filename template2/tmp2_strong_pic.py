#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\8\\1 0001

from PIL import Image
from PIL import ImageEnhance
import cv2
import random
import setup


def strong(time_str) :
    bright(time_str)
    color(time_str)
    contrast(time_str)
    sharp(time_str)
    part_bright(time_str)


def bright(time_str) :
    args = setup.parser_args()
    for j in range(args.num) :
        image = Image.open('template2\\tmp2_res\\rotate\\pic' + time_str + '.jpg')
        txt = open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        # 亮度增强
        enh_bri = ImageEnhance.Brightness(image)
        cc1 = random.uniform(1.0 - args.bright_limit, 1.0 + args.bright_limit)  # 亮暗系数
        brightness = cc1
        image_brightened = enh_bri.enhance(brightness)
        image_brightened.save('template2\\tmp2_res\\bright\\pic' + time_str + '_' + str(j) + '_bri.jpg')
        txt_bright = open('template2\\tmp2_res\\strong_txt\\pic' + time_str + '_' + str(j) + '_bri.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)

def color(time_str) :
    args = setup.parser_args()
    for j in range(args.num) :
        image = Image.open('template2\\tmp2_res\\rotate\\pic' + time_str + '.jpg')
        txt = open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        # 色度增强
        enh_col = ImageEnhance.Color(image)
        cc2 = random.uniform(1.0 - args.color_limit, 1.0 + args.color_limit)  # 色度系数
        color_cc = cc2
        image_colored = enh_col.enhance(color_cc)
        image_colored.save('template2\\tmp2_res\\color\\pic' + time_str + '_' + str(j) + '_col.jpg')
        txt_bright = open('template2\\tmp2_res\\strong_txt\\pic' + time_str + '_' + str(j) + '_col.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)

def contrast(time_str) :
    args = setup.parser_args()
    for j in range(args.num) :
        image = Image.open('template2\\tmp2_res\\rotate\\pic' + time_str + '.jpg')
        # 对比度增强
        txt = open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        enh_con = ImageEnhance.Contrast(image)
        cc3 = random.uniform(1.0 - args.contrast_limit, 1.0 + args.contrast_limit)  # 对比度系数
        contrast_cc = cc3
        image_contrasted = enh_con.enhance(contrast_cc)
        image_contrasted.save('template2\\tmp2_res\\contrast\\pic' + time_str + '_' + str(j) + '_con.jpg')
        txt_bright = open('template2\\tmp2_res\\strong_txt\\pic' + time_str + '_' + str(j) + '_con.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)

def sharp(time_str) :
    args = setup.parser_args()
    for j in range(args.num) :
        image = Image.open('template2\\tmp2_res\\rotate\\pic' + time_str + '.jpg')
        # 锐度增强
        txt = open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        enh_sha = ImageEnhance.Sharpness(image)
        cc4 = random.uniform(2.0 - args.sharp_limit, 2.0 + args.sharp_limit)  # 锐度系数
        sharpness = cc4
        image_sharped = enh_sha.enhance(sharpness)
        image_sharped.save('template2\\tmp2_res\\sharp\\pic' + time_str + '_' + str(j) + '_sha.jpg')
        txt_bright = open('template2\\tmp2_res\\strong_txt\\pic' + time_str + '_' + str(j) + '_sha.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)

def part_bright(time_str) :
    args = setup.parser_args()
    for j in range(args.num) :
        img = cv2.imread('template2\\tmp2_res\\rotate\\pic' + time_str + '.jpg')
        txt = open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        #   指定区域变暗
        rows, cols, c = img.shape  # rows = height, cols = width
        dark1 = random.randint(-args.part_bright_coe, -args.part_bright_coe + 20)
        dark2 = random.randint(args.part_bright_coe - 20, args.part_bright_coe)
        dark = random.choice([dark1, dark2])
        print(dark)
        # with open('template2\\tmp2_res\\txt\\pic' + time_str + '.txt', 'r') as f :
        #     lines = f.readlines()
        #     tp = []
        #     for line in lines[8 : 12] :
        #         temp1 = line.strip('\n')
        #         temp2 = temp1.split(',')
        #         tp.extend(temp2)
        #     # print(tp[0])
        #     x1 = min(int(float(tp[0])), int(float(tp[-9])))
        #     y1 = min(int(float(tp[1])), int(float(tp[3])))
        #     x2 = max(int(float(tp[2])), int(float(tp[-3])))
        #     y2 = max(int(float(tp[-4])), int(float(tp[-2])))
        x1, y1 = random.randint(30, 900), random.randint(161, 672)
        x2, y2 = x1 + 200, y1 + 100
        for x in range(y1, y2) :
            for y in range(x1, x2) :
                for z in range(c) :
                    if (img[x, y, z] + dark) > 255 :
                        img[x, y, z] = 255
                    elif (img[x, y, z] + dark) < 0 :
                        img[x, y, z] = 0
                    else :
                        img[x, y, z] += dark
        cv2.imwrite('template2\\tmp2_res\\part_bright\\pic' + time_str + '_' + str(j) + '_part.jpg', img)
        txt_part = open('template2\\tmp2_res\\strong_txt\\pic' + time_str + '_' + str(j) + '_sha.txt', 'w',
                          encoding = 'utf-8')
        txt_part.write(txtdata)

def adjust(time_str) :
    args = setup.parser_args()
    s_type = args.strong_type
    if s_type == 'bright' :
        bright(time_str)
    elif s_type == 'color' :
        color(time_str)
    elif s_type == 'contrast' :
        contrast(time_str)
    elif s_type == 'shape' :
        sharp(time_str)
    elif s_type == 'part_bright' :
        part_bright(time_str)
    else :
        strong(time_str)
