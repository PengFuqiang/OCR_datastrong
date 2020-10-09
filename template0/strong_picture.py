#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\7\\28 0028

from PIL import Image
from PIL import ImageEnhance
import cv2
import random
import setup

args = setup.parser_args()


def bright(pic_name) :
    for j in range(args.num) :
        image = Image.open('template0\\res\\rotate\\pic' + pic_name + '.jpg')
        txt = open('template0\\res\\txt\\pic' + pic_name + '.txt', 'r', encoding='utf-8')
        txtdata = txt.read()
        # 亮度增强
        enh_bri = ImageEnhance.Brightness(image)
        cc1 = random.uniform(1.0 - args.bright_limit, 1.0 + args.bright_limit)  # 亮暗系数
        brightness = cc1
        image_brightened = enh_bri.enhance(brightness)
        image_brightened.save('template0\\res\\bright\\pic' + pic_name + '_' + str(j) + '_bri.jpg')
        txt_bright = open('template0\\res\\strong_txt\\pic' + pic_name + '_' + str(j) + '_bri.txt', 'w', encoding='utf-8')
        txt_bright.write(txtdata)


def color(pic_name) :
    for j in range(args.num) :
        image = Image.open('template0\\res\\rotate\\pic' + pic_name + '.jpg')
        txt = open('template0\\res\\txt\\pic' + pic_name + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        # 色度增强
        enh_col = ImageEnhance.Color(image)
        cc2 = random.uniform(1.0 - args.color_limit, 1.0 + args.color_limit)  # 色度系数
        color_cc = cc2
        image_colored = enh_col.enhance(color_cc)
        image_colored.save('template0\\res\\color\\pic' + pic_name + '_' + str(j) + '_col.jpg')
        txt_bright = open('template0\\res\\strong_txt\\pic' + pic_name + '_' + str(j) + '_col.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)


def contrast(pic_name) :
    for j in range(args.num) :
        image = Image.open('template0\\res\\rotate\\pic' + pic_name + '.jpg')
        txt = open('template0\\res\\txt\\pic' + pic_name + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        # 对比度增强
        enh_con = ImageEnhance.Contrast(image)
        cc3 = random.uniform(1.0 - args.contrast_limit, 1.0 + args.contrast_limit)  # 对比度系数
        contrast_cc = cc3
        image_contrasted = enh_con.enhance(contrast_cc)
        image_contrasted.save('template0\\res\\contrast\\pic' + pic_name + '_' + str(j) + '_con.jpg')
        txt_bright = open('template0\\res\\strong_txt\\pic' + pic_name + '_' + str(j) + '_con.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)


def sharp(pic_name) :
    for j in range(args.num) :
        image = Image.open('template0\\res\\rotate\\pic' + pic_name + '.jpg')
        txt = open('template0\\res\\txt\\pic' + pic_name + '.txt', 'r', encoding = 'utf-8')
        txtdata = txt.read()
        # 锐度增强
        enh_sha = ImageEnhance.Sharpness(image)
        cc4 = random.uniform(2.0 - args.sharp_limit, 2.0 + args.sharp_limit)  # 锐度系数
        sharpness = cc4
        image_sharped = enh_sha.enhance(sharpness)
        image_sharped.save('template0\\res\\sharp\\pic' + pic_name + '_' + str(j) + '_sha.jpg')
        txt_bright = open('template0\\res\\strong_txt\\pic' + pic_name + '_' + str(j) + '_sha.txt', 'w',
                          encoding = 'utf-8')
        txt_bright.write(txtdata)


def part_bright(pic_name) :
    for j in range(args.num) :
        img = cv2.imread('template0\\res\\rotate\\pic' + pic_name + '.jpg')
        #   指定区域变暗
        rows, cols, c = img.shape  # rows = height, cols = width
        dark = random.randint(-args.part_bright_coe, args.part_bright_coe)
        with open('template0\\res\\txt\\pic' + str(i) + '.txt', 'r') as f :
            lines = f.readlines()
            tp = []
            for line in lines[8 : 12] :
                temp1 = line.strip('\n')
                temp2 = temp1.split(',')
                tp.extend(temp2)
            # print(tp[0])
            x1 = min(int(float(tp[0])), int(float(tp[-9])))
            y1 = min(int(float(tp[1])), int(float(tp[3]))) - 30
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
        cv2.imwrite('template0\\res\\part_bright\\pic' + pic_name + '_' + str(j) + '_part.jpg', img)


def adjust(time_str) :
    pic_name = time_str
    s_type = args.strong_type
    if s_type == 'bright' :
        bright(pic_name)
    elif s_type == 'color' :
        color(pic_name)
    elif s_type == 'contrast' :
        contrast(pic_name)
    elif s_type == 'sharp' :
        sharp(pic_name)
    elif s_type == 'part_bright' :
        part_bright(pic_name)
    else :
        bright(pic_name)
        color(pic_name)
        contrast(pic_name)
        sharp(pic_name)
        # part_bright()

    # 视角转换
    # img = cv2.imread('res\\pic' + str(index) + '.jpg')
    # rows, cols, c = img.shape  # rows = height, cols = width
    # print(c)
    # pts1 = np.float32([[30, 30], [cols - 30, 30], [30, rows - 30], [cols - 30, rows - 30]])
    # pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
    # M = cv2.getPerspectiveTransform(pts1, pts2)
    # dst = cv2.warpPerspective(img, M, (cols, rows))
    # cv2.imwrite('res\\pic' + str(index) + '_wrp.jpg', dst)
    #
    # # 透视变换
    # pts1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
    # pts2 = np.float32([[200, 200], [cols - 200, 200], [0, rows], [cols, rows]])
    # M = cv2.getPerspectiveTransform(pts1, pts2)
    # dst = cv2.warpPerspective(img, M, (cols, rows))
    # cv2.imwrite('res\\pic' + str(index) + '_' + str(amount) + '_toushi.jpg', dst)
    #
    # #  图像凹形
    # output = np.zeros(img.shape)
    # for m in range(rows) :
    #     for n in range(cols) :
    #         offset_x = int(128.0 * math.sin(2 * math.pi * m \\ (2 * cols)))
    #         offset_y = 0
    #         if n + offset_x < cols :
    #             output[m, n] = img[m, (n + offset_x) % cols]
    #         else :
    #             output[m, n] = 255
    #
    # cv2.imwrite('res\\pic' + str(index) + '_' + str(amount) + '_wave.jpg', output)
