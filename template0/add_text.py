#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author：pfq time:2020/7/1

import random
import datetime
import re
import cv2 as cv
from PIL import Image
from PIL import ImageDraw
from faker import Faker
from numpy import sin, cos, pi

import global_var as global_var
import template0.split_picture as sp
from template0 import strong_picture
from template0 import correct_rotate

'''
声明全局变量
im : 读取的图像
filename : 保存坐标的文件名
rotate_angle : 图片旋转角度
cx, cy ：图片中心点坐标
index : 生成一定数量的图片需要循环，index是目前循环的次数 
'''
im = Image.open('template0\\pic_template\\template_1.jpg')
draw = ImageDraw.Draw(im)

filename = 'template0\\res\\pic1.txt'
kv_filename = 'template0\\res\\pic1_kv.txt'
rotate_angle = 0
cx, cy = 0, 0
index = 0

fake = Faker(locale = 'zh_CN')  # 初始化中文简体


def rotate(x, y) :
    """
    点(x,y) 绕(cx,cy)点旋转
    """
    angle = - (rotate_angle * pi / 180)  # 角度转换为弧度计算
    x_new = (x - cx) * cos(angle) - (y - cy) * sin(angle) + cx
    y_new = (x - cx) * sin(angle) + (y - cy) * cos(angle) + cy
    return x_new, y_new


def xy_end(m1, n1, m2, n2, m3, n3, m4, n4) :
    """
    返回旋转之后的坐标值
    """
    m11, n11 = rotate(m1, n1)
    m22, n22 = rotate(m2, n2)
    m33, n33 = rotate(m3, n3)
    m44, n44 = rotate(m4, n4)
    return (str(m11) + ',' + str(n11) + ',' + str(m22) + ',' + str(n22) + ',' + str(m33) + ',' + str(n33) + ',' + str(
        m44) + ',' + str(n44) + ' ')


# 金额转换为中文大写
def digital_to_chinese(digital) :
    str_digital = str(digital)
    chinese = {'1' : '壹', '2' : '贰', '3' : '叁', '4' : '肆', '5' : '伍', '6' : '陆', '7' : '柒', '8' : '捌', '9' : '玖',
               '0' : '零'}
    chinese2 = ['拾', '佰', '仟', '万', '厘', '分', '角']
    jiao = ''
    bs = str_digital.split('.')
    yuan = bs[0]
    if len(bs) > 1 :
        jiao = bs[1]
    r_yuan = [i for i in reversed(yuan)]
    count = 0
    for i in range(len(yuan)) :
        if i == 0 :
            r_yuan[i] += '圆'
            continue
        r_yuan[i] += chinese2[count]
        count += 1
        if count == 4 :
            count = 0
            chinese2[3] = '亿'

    s_jiao = [i for i in jiao][:2]  # 去掉小于分之后的

    j_count = -1
    for i in range(len(s_jiao)) :
        s_jiao[i] += chinese2[j_count]
        j_count -= 1
    last = [i for i in reversed(r_yuan)] + s_jiao
    last_str = ''.join(last)
    # print(str_digital)
    # print(last_str)
    for i in range(len(last_str)) :
        digital = last_str[i]
        if digital in chinese :
            last_str = last_str.replace(digital, chinese[digital])
    if '零角零分' in last_str :
        last_str.replace('零角零分', '整')

    last_str = re.sub(r'零[仟佰拾角分]', '零', last_str)
    last_str = re.sub(r'零{2,}', '零', last_str)
    last_str = re.sub(r'零$', '', last_str)
    last_str = re.sub(r'零圆', '圆', last_str)
    return last_str


# 生成日期函数
def print_date() :
    date = fake.date(pattern = '%Y年%m月%d日')
    draw.text((1501, 191), date, fill = (31, 83, 182), font = global_var.ft5)
    # 日期的坐标
    x1, y1 = 1500, 191
    x2, y2 = 1680, 191
    x3, y3 = 1500, 219
    x4, y4 = 1680, 219
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)

    a1, b1 = 1341, 183
    a2, b2 = 1479, 183
    a3, b3 = 1341, 213
    a4, b4 = 1479, 213
    bf_date = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)

    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_date + '开票日期：' + '\n')
        f.write(text + date + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("发票基本信息_开票日期" + '\t' + date + '\n')
        fname.write("发票基本信息_校验码" + '\n')


# 购买方区域文字添加
def purchase() :
    """
    字体宽度为27px，高度为30px
    以此计算字符串范围的四个顶点坐标
    然后调用rotate函数计算旋转之后的顶点坐标
    """
    # 添加公司名称
    name = fake.company()  # 随机生成公司名称
    draw.text((436, 253), name, fill = (8, 67, 161), font = global_var.ft6)
    name_length = len(name)
    x_start, y_start = 436, 253
    x_end, y_end = 436 + (name_length * 26), 253 + 25

    x1, y1 = x_start, y_start
    x2, y2 = x_end, y_start
    x3, y3 = x_start, y_end
    x4, y4 = x_end, y_end
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)

    a1, b1 = 225, 247
    a2, b2 = 405, 247
    a3, b3 = 225, 277
    a4, b4 = 405, 277
    bf_text = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '名称：' + '\n')
        f.write(text + name + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("购买方_名称" + '\t' + name + '\n')

    # 添加纳税人识别号
    id_num = ''.join(str(random.choice(range(10))) for _ in range(15))  # 随机生成15位纳税人识别号
    draw.text((461, 290), id_num, fill = (8, 67, 161), font = global_var.ft7)
    id_x1, id_y1 = 461, 290
    id_x2, id_y2 = 744, 290
    id_x3, id_y3 = 461, 315
    id_x4, id_y4 = 744, 315
    text = xy_end(id_x1, id_y1, id_x2, id_y2, id_x3, id_y3, id_x4, id_y4)

    id_a1, id_b1 = 225, 290
    id_a2, id_b2 = 405, 290
    id_a3, id_b3 = 225, 315
    id_a4, id_b4 = 405, 315
    bf_text = xy_end(id_a1, id_b1, id_a2, id_b2, id_a3, id_b3, id_a4, id_b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '纳税人识别号：' + '\n')
        f.write(text + id_num + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("购买方_纳税人识别号" + '\t' + id_num + '\n')
    # 添加地址电话
    phone1 = ''.join(str(random.choice(range(10))) for _ in range(3))
    phone2 = ''.join(str(random.choice(range(10))) for _ in range(7))
    address = fake.address()[0 : -7]
    add_len = len(address)
    address_phone = address + ' ' + phone1 + '-' + phone2
    draw.text((433, 338), address_phone, fill = (8, 67, 161), font = global_var.ft8)
    add_ph_x1, add_ph_y1 = 433, 338
    add_ph_x2, add_ph_y2 = 433 + 21 * (add_len + 1) + 12 * 10, 338  # 十个号码加一个空格一个斜杠以及地址长度
    add_ph_x3, add_ph_y3 = 433, 338 + 25
    add_ph_x4, add_ph_y4 = 433 + 21 * (add_len + 1) + 12 * 10, 338 + 25
    text = xy_end(add_ph_x1, add_ph_y1, add_ph_x2, add_ph_y2, add_ph_x3, add_ph_y3, add_ph_x4, add_ph_y4)

    add_ph_a1, add_ph_b1 = 225, 334
    add_ph_a2, add_ph_b2 = 405, 334
    add_ph_a3, add_ph_b3 = 225, 360
    add_ph_a4, add_ph_b4 = 405, 360
    bf_text = xy_end(add_ph_a1, add_ph_b1, add_ph_a2, add_ph_b2, add_ph_a3, add_ph_b3, add_ph_a4, add_ph_b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '地址、电话：' + '\n')
        f.write(text + address_phone + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("购买方_地址、电话" + '\t' + address_phone + '\n')

    # 添加开户行及账号
    bank1 = ['招商银行', '汉口银行', 'EBA银行', '交通银行股份', '中国建设银行']
    bank2 = ['龙阳大道支行', '北京东三环支行', '上海分行', '城北支行', '北京海淀支行', '上海支行']
    # 15或18位账号
    acc = [''.join(str(random.choice(range(10))) for _ in range(15)),
           ''.join(str(random.choice(range(10))) for _ in range(18))]
    bank = random.choice(bank1) + random.choice(bank2)
    acc = random.choice(acc)
    bank_len, acc_len = len(bank), len(acc)
    bank_account = bank + ' ' + acc
    draw.text((436, 380), bank_account, fill = (8, 67, 161), font = global_var.ft6)
    bank_x1, bank_y1 = 436, 380
    bank_x2, bank_y2 = 436 + bank_len * 26 + 14 * acc_len, 380
    bank_x3, bank_y3 = 436, 380 + 25
    bank_x4, bank_y4 = 436 + bank_len * 26 + 14 * acc_len, 380 + 25
    text = xy_end(bank_x1, bank_y1, bank_x2, bank_y2, bank_x3, bank_y3, bank_x4, bank_y4)

    bank_a1, bank_b1 = 225, 375
    bank_a2, bank_b2 = 405, 375
    bank_a3, bank_b3 = 225, 401
    bank_a4, bank_b4 = 405, 401
    bf_text = xy_end(bank_a1, bank_b1, bank_a2, bank_b2, bank_a3, bank_b3, bank_a4, bank_b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '开户行及账号：' + '\n')
        f.write(text + bank_account + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("购买方_开户行及账号" + '\t' + bank_account + '\n')


# 添加密码区
def password() :
    """
    密码区每行长度都相同为66，高度为33
    """
    stru = ['+', '-', '*', '\\', '<', '>', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 组成密码的符号和数字
    pwd1 = ''.join(str(random.choice(stru)) for _ in range(27))
    pwd2 = ''.join(str(random.choice(stru)) for _ in range(27))
    pwd3 = ''.join(str(random.choice(stru)) for _ in range(27))
    pwd4 = ''.join(str(random.choice(stru)) for _ in range(27))
    draw.text((1127, 257), pwd1, fill = (8, 67, 161), font = global_var.ft9)
    draw.text((1127, 290), pwd2, fill = (8, 67, 161), font = global_var.ft9)
    draw.text((1127, 323), pwd3, fill = (8, 67, 161), font = global_var.ft9)
    draw.text((1127, 356), pwd4, fill = (8, 67, 161), font = global_var.ft9)
    # # 第一行密码的坐标
    # pwd1_x1, pwd1_y1 = 1127, 257
    # pwd1_x2, pwd1_y2 = 1693, 257
    # pwd1_x3, pwd1_y3 = 1127, 288
    # pwd1_x4, pwd1_y4 = 1693, 288
    # pwd1_text = xy_end(pwd1_x1, pwd1_y1, pwd1_x2, pwd1_y2, pwd1_x3, pwd1_y3, pwd1_x4, pwd1_y4)
    # # 第二行密码的坐标
    # pwd2_x1, pwd2_y1 = 1127, 290
    # pwd2_x2, pwd2_y2 = 1693, 290
    # pwd2_x3, pwd2_y3 = 1127, 321
    # pwd2_x4, pwd2_y4 = 1693, 321
    # pwd2_text = xy_end(pwd2_x1, pwd2_y1, pwd2_x2, pwd2_y2, pwd2_x3, pwd2_y3, pwd2_x4, pwd2_y4)
    # # 第三行密码的坐标
    # pwd3_x1, pwd3_y1 = 1127, 323
    # pwd3_x2, pwd3_y2 = 1693, 323
    # pwd3_x3, pwd3_y3 = 1127, 354
    # pwd3_x4, pwd3_y4 = 1693, 354
    # pwd3_text = xy_end(pwd3_x1, pwd3_y1, pwd3_x2, pwd3_y2, pwd3_x3, pwd3_y3, pwd3_x4, pwd3_y4)
    # # 第四行密码的坐标
    # pwd4_x1, pwd4_y1 = 1127, 356
    # pwd4_x2, pwd4_y2 = 1693, 356
    # pwd4_x3, pwd4_y3 = 1127, 387
    # pwd4_x4, pwd4_y4 = 1693, 387
    # pwd4_text = xy_end(pwd4_x1, pwd4_y1, pwd4_x2, pwd4_y2, pwd4_x3, pwd4_y3, pwd4_x4, pwd4_y4)
    # with open(filename, 'a+', encoding = 'utf-8') as f :
    #     f.write(pwd1_text + pwd1 + '\n')
    #     f.write(pwd2_text + pwd2 + '\n')
    #     f.write(pwd3_text + pwd3 + '\n')
    #     f.write(pwd4_text + pwd4 + '\n')


# 添加货物或应税劳务及后面对应的规格价格等内容
def change_line(y) :
    goods = fake.sentence()[0 : 3]
    draw.text((185, y), goods, fill = (8, 67, 161), font = global_var.ft6)
    goods_x1, goods_y1 = 185, y
    goods_x2, goods_y2 = 185 + 3 * 26, y
    goods_x3, goods_y3 = 185, y + 25
    goods_x4, goods_y4 = 185 + 3 * 26, y + 25
    goods_text = xy_end(goods_x1, goods_y1, goods_x2, goods_y2, goods_x3, goods_y3, goods_x4, goods_y4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(goods_text + goods + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("货物或应税劳务、服务名称" + '\t' + goods + '\n')


def add_goods() :
    """
    货物，型号，单位等每个字符长为26高为29
    其余数字字符宽为13或19
    """
    types = ['g', 'g', 'l', '*', '#', 'h', '', 'kg', '']
    units = ['升', '支', '件', '袋', '只', '瓶', '盒', '块', 'km', 'N', 'kg', 'KG', '米', '根', '平方', '毫升', '千克', '斤', '']
    amounts = [random.randint(1, 10), random.randint(1, 100),
               random.randint(1, 1000), random.randint(1, 2000)]
    unit_prices = [round(random.uniform(0, 10), 2), round(random.uniform(0, 100), 2),
                   round(random.uniform(0, 1000), 2)]
    rate = random.choice(range(1, 20))  # 求对应的税率
    total1 = 0  # 各个金额之和
    total2 = 0  # 各个税额之和
    total = 0

    goods_a1, goods_b1 = 198, 418
    goods_a2, goods_b2 = 525, 418
    goods_a3, goods_b3 = 198, 444
    goods_a4, goods_b4 = 525, 444
    bf_goods_text = xy_end(goods_a1, goods_b1, goods_a2, goods_b2, goods_a3, goods_b3, goods_a4, goods_b4)

    standards_a1, standards_b1 = 612, 418
    standards_a2, standards_b2 = 732, 418
    standards_a3, standards_b3 = 612, 444
    standards_a4, standards_b4 = 732, 444
    bf_standards_text = xy_end(standards_a1, standards_b1, standards_a2, standards_b2, standards_a3, standards_b3,
                               standards_a4, standards_b4)
    units_a1, units_b1 = 797, 418
    units_a2, units_b2 = 851, 418
    units_a3, units_b3 = 797, 444
    units_a4, units_b4 = 851, 444
    bf_units_text = xy_end(units_a1, units_b1, units_a2, units_b2, units_a3, units_b3, units_a4, units_b4)

    amount_a1, amount_b1 = 917, 418
    amount_a2, amount_b2 = 993, 418
    amount_a3, amount_b3 = 917, 444
    amount_a4, amount_b4 = 993, 444
    bf_amount_text = xy_end(amount_a1, amount_b1, amount_a2, amount_b2, amount_a3, amount_b3, amount_a4, amount_b4)

    unit_price_a1, unit_price_b1 = 1081, 418
    unit_price_a2, unit_price_b2 = 1156, 418
    unit_price_a3, unit_price_b3 = 1081, 444
    unit_price_a4, unit_price_b4 = 1156, 444
    bf_unit_price_text = xy_end(unit_price_a1, unit_price_b1, unit_price_a2, unit_price_b2, unit_price_a3,
                                unit_price_b3, unit_price_a4, unit_price_b4)

    total_price_a1, total_price_b1 = 1266, 418
    total_price_a2, total_price_b2 = 1377, 418
    total_price_a3, total_price_b3 = 1266, 444
    total_price_a4, total_price_b4 = 1377, 444
    bf_total_price_text = xy_end(total_price_a1, total_price_b1, total_price_a2, total_price_b2, total_price_a3,
                                 total_price_b3, total_price_a4, total_price_b4)

    rate_a1, rate_b1 = 1452, 418
    rate_a2, rate_b2 = 1512, 418
    rate_a3, rate_b3 = 1452, 444
    rate_a4, rate_b4 = 1512, 444
    bf_rate_text = xy_end(rate_a1, rate_b1, rate_a2, rate_b2, rate_a3, rate_b3, rate_a4, rate_b4)

    tax_a1, tax_b1 = 1588, 418
    tax_a2, tax_b2 = 1699, 418
    tax_a3, tax_b3 = 1588, 444
    tax_a4, tax_b4 = 1699, 444
    bf_tax_text = xy_end(tax_a1, tax_b1, tax_a2, tax_b2, tax_a3, tax_b3, tax_a4, tax_b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :  # 写入坐标信息
        f.write(bf_goods_text + '货物或应税劳务、服务名称' + '\n')
        f.write(bf_standards_text + '规格型号' + '\n')
        f.write(bf_units_text + '单位' + '\n')
        f.write(bf_amount_text + '数量' + '\n')
        f.write(bf_unit_price_text + '单价' + '\n')
        f.write(bf_total_price_text + '金额' + '\n')
        f.write(bf_rate_text + '税率' + '\n')
        f.write(bf_tax_text + '税额' + '\n')

    flag = random.choice(['true', 'false', 'false', 'false'])   # 判断是否要生成换行的货物名称
    for i in range(4) :
        y = 461 + (35 * i)
        goods = fake.sentence()[0 : -1]
        standards = ''
        for a in range(random.randint(1, 3)) :
            standards = standards + fake.word() + random.choice(types)
        unit = random.choice(units)

        if flag == 'true' and i == 0 :
            goods = goods + (fake.sentence()[0 : -1] * 5)
        if len(goods) > 15 :
            goods = goods[0 : 15]  # 避免字符串过长
        goods = '*' + goods
        goods_len = len(goods)

        if flag == 'true' and i == 1 :
            change_line(y)
            continue

        draw.text((185, y), goods, fill = (8, 67, 161), font = global_var.ft6)  # 添加货物
        draw.text((586, y), standards, fill = (8, 67, 161), font = global_var.ft6)  # 添加型号规格
        draw.text((804, y), unit, fill = (8, 67, 161), font = global_var.ft6)  # 添加单位

        # 获取货物，型号，单位旋转后的坐标
        goods_x1, goods_y1 = 185, y
        goods_x2, goods_y2 = 185 + goods_len * 26, y
        if goods_x2 > 578 :
            goods_x2 = 578
        goods_x3, goods_y3 = 185, y + 25
        goods_x4, goods_y4 = 185 + goods_len * 26, y + 25
        if goods_x4 > 578 :
            goods_x4 = 578
        goods_text = xy_end(goods_x1, goods_y1, goods_x2, goods_y2, goods_x3, goods_y3, goods_x4, goods_y4)

        standards_x1, standards_y1 = 586, y
        standards_x2, standards_y2 = 586 + 25 * (len(standards)), y
        standards_x3, standards_y3 = 586, y + 25
        standards_x4, standards_y4 = 586 + 25 * (len(standards)), y + 25
        standards_text = xy_end(standards_x1, standards_y1, standards_x2, standards_y2, standards_x3, standards_y3,
                                standards_x4, standards_y4)

        units_x1, units_y1 = 804, y
        units_x2, units_y2 = 804 + 48, y
        units_x3, units_y3 = 804, y + 25
        units_x4, units_y4 = 804 + 48, y + 25
        units_text = xy_end(units_x1, units_y1, units_x2, units_y2, units_x3, units_y3, units_x4, units_y4)

        # 最终坐标写入到文件中
        with open(filename, 'a+', encoding = 'utf-8') as f :
            f.write(goods_text + goods + '\n')
            f.write(standards_text + standards + '\n')
            f.write(units_text + unit + '\n')
        with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
            fname.write("货物或应税劳务、服务名称" + '\t' + goods + '\n')
            fname.write("规格型号" + '\t' + standards + '\n')
            fname.write("单位" + '\t' + unit + '\n')

        amount = random.choice(amounts)  # 取对应的数量
        unit_price = random.choice(unit_prices)  # 取单价
        total_price = amount * unit_price  # 求对应的金额
        tax_amount = rate * total_price * 0.01  # 求对应的税额
        total1 += total_price
        total2 += tax_amount
        draw.text((909, y), str(amount).rjust(8), fill = (8, 67, 161), font = global_var.ft13)  # 添加数量
        # 计算商品数量的坐标
        amount_x1, amount_y1 = 909 + 12 * (8 - len(str(amount))), y
        amount_x2, amount_y2 = 1013, y
        amount_x3, amount_y3 = 909 + 12 * (8 - len(str(amount))), y + 25
        amount_x4, amount_y4 = 1013, y + 25
        amount_text = xy_end(amount_x1, amount_y1, amount_x2, amount_y2, amount_x3, amount_y3, amount_x4, amount_y4)

        # 计算单价的坐标
        draw.text((1069, y), ("%.2f" % unit_price).rjust(8), fill = (8, 67, 161), font = global_var.ft13)  # 添加单价
        unit_price_x1, unit_price_y1 = 1069 + 13 * (8 - len(str(round(unit_price, 2)))), y
        unit_price_x2, unit_price_y2 = 1172, y
        unit_price_x3, unit_price_y3 = 1069 + 13 * (8 - len(str(round(unit_price, 2)))), y + 25
        unit_price_x4, unit_price_y4 = 1172, y + 25
        unit_price_text = xy_end(unit_price_x1, unit_price_y1, unit_price_x2, unit_price_y2, unit_price_x3,
                                 unit_price_y3, unit_price_x4, unit_price_y4)

        # 计算金额的坐标
        draw.text((1290, y), ("%.2f" % total_price).rjust(11), fill = (8, 67, 161), font = global_var.ft13)  # 添加金额
        total_price_x1, total_price_y1 = 1290 + 13 * (8 - len(str(round(total_price, 2)))), y
        total_price_x2, total_price_y2 = 1435, y
        total_price_x3, total_price_y3 = 1290 + 13 * (8 - len(str(round(total_price, 2)))), y + 25
        total_price_x4, total_price_y4 = 1435, y + 25
        total_price_text = xy_end(total_price_x1, total_price_y1, total_price_x2, total_price_y2, total_price_x3,
                                  total_price_y3, total_price_x4, total_price_y4)

        # 计算税率的坐标
        draw.text((1480, y), str(rate) + '%', fill = (8, 67, 161), font = global_var.ft13)  # 添加税率
        rate_x1, rate_y1 = 1480, y
        rate_x2, rate_y2 = 1521, y
        rate_x3, rate_y3 = 1480, y + 25
        rate_x4, rate_y4 = 1521, y + 25
        rate_text = xy_end(rate_x1, rate_y1, rate_x2, rate_y2, rate_x3, rate_y3, rate_x4, rate_y4)

        # 计算税额的坐标
        draw.text((1600, y), ("%.2f" % tax_amount).rjust(10), fill = (8, 67, 161), font = global_var.ft13)  # 添加税额
        tax_x1, tax_y1 = 1600 + 13 * (10 - len(str(round(tax_amount, 2)))), y
        tax_x2, tax_y2 = 1730, y
        tax_x3, tax_y3 = 1600 + 13 * (10 - len(str(round(tax_amount, 2)))), y + 25
        tax_x4, tax_y4 = 1730, y + 25
        tax_text = xy_end(tax_x1, tax_y1, tax_x2, tax_y2, tax_x3, tax_y3, tax_x4, tax_y4)

        with open(filename, 'a+', encoding = 'utf-8') as f :  # 写入坐标信息
            f.write(amount_text + str(amount) + '\n')
            f.write(unit_price_text + ("%.2f" % unit_price) + '\n')
            f.write(total_price_text + ("%.2f" % total_price) + '\n')
            f.write(rate_text + str(rate) + '%' + '\n')
            f.write(tax_text + ("%.2f" % tax_amount) + '\n')
        with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
            fname.write("数量" + '\t' + str(amount) + '\n')
            fname.write("单价" + '\t' + ("%.2f" % unit_price) + '\n')
            fname.write("金额" + '\t' + ("%.2f" % total_price) + '\n')
            fname.write("税率" + '\t' + str(rate) + '%' + '\n')
            fname.write("税额" + '\t' + ("%.2f" % tax_amount) + '\n')
    # 计算总价
    total = total1 + total2
    big_total = digital_to_chinese(round(total, 2))  # 总金额取两位并转为大写
    # 添加金额前的￥符号
    draw.text((1214, 715), '￥', fill = (8, 67, 161), font = global_var.ft12)
    draw.text((1541, 715), '￥', fill = (8, 67, 161), font = global_var.ft12)
    draw.text((1410, 781), '￥', fill = (8, 67, 161), font = global_var.ft12)

    draw.text((1244, 715), ("%.2f" % total1), fill = (8, 67, 161), font = global_var.ft10)  # 添加金额之和
    draw.text((1571, 715), ("%.2f" % total2), fill = (8, 67, 161), font = global_var.ft10)  # 添加税额之和
    draw.text((1440, 781), ("%.2f" % total), fill = (8, 67, 161), font = global_var.ft10)  # 添加金额税额之和
    draw.text((654, 778), big_total, fill = (8, 67, 161), font = global_var.ft11)  # 添加金额税额之和的中文大写

    total_a1, total_b1 = 275, 725
    total_a2, total_b2 = 453, 725
    total_a3, total_b3 = 275, 751
    total_a4, total_b4 = 453, 751
    bf_total_text = xy_end(total_a1, total_b1, total_a2, total_b2, total_a3, total_b3, total_a4, total_b4)
    # 金额之和坐标
    total1_x1, total1_y1 = 1214, 715
    total1_x2, total1_y2 = 1244 + 19 * len(str("%.2f" % total1)), 715
    total1_x3, total1_y3 = 1214, 740
    total1_x4, total1_y4 = 1244 + 19 * len(str("%.2f" % total1)), 740
    total1_text = xy_end(total1_x1, total1_y1, total1_x2, total1_y2, total1_x3, total1_y3, total1_x4, total1_y4)

    # 税额之和坐标
    total2_x1, total2_y1 = 1541, 715
    total2_x2, total2_y2 = 1571 + 19 * len("%.2f" % total2), 715
    total2_x3, total2_y3 = 1541, 740
    total2_x4, total2_y4 = 1571 + 19 * len("%.2f" % total2), 740
    total2_text = xy_end(total2_x1, total2_y1, total2_x2, total2_y2, total2_x3, total2_y3, total2_x4, total2_y4)

    # 金额+税额之和的坐标
    total_x1, total_y1 = 1410, 781
    total_x2, total_y2 = 1440 + 19 * len("%.2f" % total), 781
    total_x3, total_y3 = 1410, 806
    total_x4, total_y4 = 1440 + 19 * len("%.2f" % total), 806
    total_text = xy_end(total_x1, total_y1, total_x2, total_y2, total_x3, total_y3, total_x4, total_y4)

    small_total_a1, small_total_b1 = 1315, 777
    small_total_a2, small_total_b2 = 1413, 777
    small_total_a3, small_total_b3 = 1315, 803
    small_total_a4, small_total_b4 = 1413, 803
    bf_small_total = xy_end(small_total_a1, small_total_b1, small_total_a2, small_total_b2, small_total_a3,
                            small_total_b3, small_total_a4, small_total_b4)

    # 大写金额税额之和的坐标
    big_x1, big_y1 = 654, 778
    big_x2, big_y2 = 654 + 26 * len(big_total), 778
    big_x3, big_y3 = 654, 803  # 778 + 25
    big_x4, big_y4 = 654 + 26 * len(big_total), 803
    big_text = xy_end(big_x1, big_y1, big_x2, big_y2, big_x3, big_y3, big_x4, big_y4)

    big_a1, big_b1 = 248, 780
    big_a2, big_b2 = 477, 780
    big_a3, big_b3 = 248, 806
    big_a4, big_b4 = 477, 806
    bf_big_text = xy_end(big_a1, big_b1, big_a2, big_b2, big_a3, big_b3, big_a4, big_b4)
    # 写入坐标
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_total_text + '合计' + '\n')
        f.write(total1_text + '￥' + ("%.2f" % total1) + '\n')
        f.write(total2_text + '￥' + ("%.2f" % total2) + '\n')
        f.write(bf_small_total + '（小写）' + '\n')
        f.write(total_text + '￥' + ("%.2f" % total) + '\n')
        f.write(bf_big_text + '价税合计（大写）' + '\n')
        f.write(big_text + big_total + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("合计金额" + '\t' + ("%.2f" % total1) + '\n')
        fname.write("合计税额" + '\t' + ("%.2f" % total2) + '\n')
        fname.write("价税合计（大写）" + '\t' + big_total + '\n')
        fname.write("价税合计（小写）" + '\t' + ("%.2f" % total) + '\n')


# 添加销售方内容
def add_seller() :  # 添加销售方名称
    """
    宽为27高为30
    """
    seller_name = fake.company()
    draw.text((436, 840), seller_name, fill = (8, 67, 161), font = global_var.ft6)
    x1, y1 = 436, 840
    x2, y2 = 436 + 27 * len(seller_name), 840
    x3, y3 = 436, 840 + 25
    x4, y4 = 436 + 27 * len(seller_name), 840 + 25
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    a1, b1 = 228, 838
    a2, b2 = 405, 838
    a3, b3 = 228, 863
    a4, b4 = 405, 863
    bf_text = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '名称：' + '\n')
        f.write(text + seller_name + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("销售方_名称" + '\t' + seller_name + '\n')


def seller_nums() :  # 添加纳税人识别号（销售方）
    """
    宽为20高为30
    """
    id_part = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', chr(random.randint(65, 90))]
    id1 = ''.join(str(random.choice(id_part)) for _ in range(18))
    id2 = ''.join(str(random.choice(id_part)) for _ in range(15))
    seller_num = random.choice([id1, id2])
    draw.text((470, 872), seller_num, fill = (8, 67, 141), font = global_var.ft7)
    x1, y1 = 470, 872
    x2, y2 = 470 + 20 * len(seller_num), 872
    x3, y3 = 470, 897
    x4, y4 = 470 + 20 * len(seller_num), 897
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)

    a1, b1 = 228, 872
    a2, b2 = 405, 872
    a3, b3 = 228, 897
    a4, b4 = 405, 897
    bf_text = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '纳税人识别号：' + '\n')
        f.write(text + seller_num + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("销售方_纳税人识别号" + '\t' + seller_num + '\n')


def add_and_phone() :  # 添加地址、电话（销售方）
    """
    电话宽为14，地址宽为27，高为30
    """
    phone1 = ''.join(str(random.choice(range(10))) for _ in range(3))
    phone2 = ''.join(str(random.choice(range(10))) for _ in range(7))
    address = fake.address()[0 : -7]
    add_len = len(address)
    address_phone = address + ' ' + phone1 + '-' + phone2
    draw.text((420, 915), address_phone, fill = (8, 67, 141), font = global_var.ft6)
    x1, y1 = 420, 915
    x2, y2 = 420 + 26 * (add_len + 1) + 14 * 7, 915
    x3, y3 = 420, 940
    x4, y4 = 420 + 26 * (add_len + 1) + 14 * 7, 940
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)

    a1, b1 = 228, 910
    a2, b2 = 405, 910
    a3, b3 = 228, 935
    a4, b4 = 405, 935
    bf_text = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '地址、电话：' + '\n')
        f.write(text + address_phone + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("销售方_地址、电话" + '\t' + address_phone + '\n')


def add_bankId() :  # 添加开户行及账号
    """
    银行名称字符宽为27，账号宽为14
    """
    bank1 = ['招商银行', '汉口银行', 'EBA银行', '交通银行股份', '中国建设银行']
    bank2 = ['龙阳大道支行', '北京东三环支行', '上海分行', '城北支行', '北京海淀支行', '上海支行']
    bank = random.choice(bank1) + random.choice(bank2)
    bank_len = len(bank)
    # 15或18位账号
    acc = [''.join(str(random.choice(range(10))) for _ in range(15)),
           ''.join(str(random.choice(range(10))) for _ in range(18))]
    account = random.choice(acc)
    acc_len = len(account)
    bank_and_account = bank + ' ' + account
    draw.text((420, 950), bank_and_account, fill = (8, 67, 161), font = global_var.ft6)
    x1, y1 = 420, 950
    x2, y2 = 420 + 26 * (bank_len + 1) + 14 * acc_len, 950
    x3, y3 = 420, 975
    x4, y4 = 420 + 26 * (bank_len + 1) + 14 * acc_len, 975
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)

    a1, b1 = 228, 948
    a2, b2 = 405, 948
    a3, b3 = 228, 973
    a4, b4 = 405, 973
    bf_text = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_text + '开户行及账号：' + '\n')
        f.write(text + bank_and_account + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("销售方_开户行及账号" + '\t' + bank_and_account + '\n')


def add_name() :
    # 添加收款人复核人开票人名字
    # 生成随机的三个名字
    name1 = fake.name()
    name2 = fake.name()
    name3 = fake.name()
    draw.text((305, 995), name1, fill = (8, 67, 161), font = global_var.ft6)
    draw.text((722, 995), name2, fill = (8, 67, 161), font = global_var.ft6)
    draw.text((1099, 995), name3, fill = (8, 67, 161), font = global_var.ft6)

    n1_x1, n1_y1 = 305, 995
    n1_x2, n1_y2 = 305 + 27 * len(name1), 995
    n1_x3, n1_y3 = 305, 1020
    n1_x4, n1_y4 = 305 + 27 * len(name1), 1020
    n1_text = xy_end(n1_x1, n1_y1, n1_x2, n1_y2, n1_x3, n1_y3, n1_x4, n1_y4)

    n1_a1, n1_b1 = 185, 995
    n1_a2, n1_b2 = 297, 995
    n1_a3, n1_b3 = 185, 1025
    n1_a4, n1_b4 = 297, 1025
    bf_n1 = xy_end(n1_a1, n1_b1, n1_a2, n1_b2, n1_a3, n1_b3, n1_a4, n1_b4)

    n2_x1, n2_y1 = 722, 995
    n2_x2, n2_y2 = 722 + 27 * len(name2), 995
    n2_x3, n2_y3 = 722, 1020
    n2_x4, n2_y4 = 722 + 27 * len(name2), 1020
    n2_text = xy_end(n2_x1, n2_y1, n2_x2, n2_y2, n2_x3, n2_y3, n2_x4, n2_y4)

    n2_a1, n2_b1 = 635, 995
    n2_a2, n2_b2 = 713, 995
    n2_a3, n2_b3 = 635, 1025
    n2_a4, n2_b4 = 713, 1025
    bf_n2 = xy_end(n2_a1, n2_b1, n2_a2, n2_b2, n2_a3, n2_b3, n2_a4, n2_b4)

    n3_x1, n3_y1 = 1099, 995
    n3_x2, n3_y2 = 1099 + 27 * len(name2), 995
    n3_x3, n3_y3 = 1099, 1020
    n3_x4, n3_y4 = 1099 + 27 * len(name2), 1020
    n3_text = xy_end(n3_x1, n3_y1, n3_x2, n3_y2, n3_x3, n3_y3, n3_x4, n3_y4)

    n3_a1, n3_b1 = 975, 995
    n3_a2, n3_b2 = 1090, 995
    n3_a3, n3_b3 = 975, 1025
    n3_a4, n3_b4 = 1090, 1025
    bf_n3 = xy_end(n3_a1, n3_b1, n3_a2, n3_b2, n3_a3, n3_b3, n3_a4, n3_b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(bf_n1 + '收款人：' + '\n')
        f.write(n1_text + name1 + '\n')
        f.write(bf_n2 + '复核：' + '\n')
        f.write(n2_text + name2 + '\n')
        f.write(bf_n3 + '开票人：' + '\n')
        f.write(n3_text + name3 + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("发票基本信息_收款人" + '\t' + name1 + '\n')
        fname.write("发票基本信息_复核" + '\t' + name2 + '\n')
        fname.write("发票基本信息_开票人" + '\t' + name3 + '\n')


# 添加发票代码
def add_fapiao_daima() :
    num_str = ''.join(str(random.choice(range(10))) for _ in range(10))  # 随机生成10位数字发票代码
    draw.text((344, 82), num_str, fill = (72, 75, 68), font = global_var.ft1)  # 添加发票代码
    draw.text((1603, 110), num_str, fill = (31, 83, 182), font = global_var.ft3)  # 添加号码后面的小代码
    # 大的发票代码的坐标
    x1, y1 = 344, 82
    x2, y2 = 624, 82
    x3, y3 = 344, 130
    x4, y4 = 624, 130
    x_text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    # 小的发票代码的坐标
    sx1, sy1 = 1600, 110
    sx2, sy2 = 1735, 110
    sx3, sy3 = 1600, 133
    sx4, sy4 = 1735, 133
    sx_text = xy_end(sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4)

    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(x_text + num_str + '\n')
        f.write(sx_text + num_str + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("发票基本信息_发票代码" + '\t' + num_str + '\n')


# 添加发票号码
def add_fapiao_hao() :
    no_str = ''.join(str(random.choice(range(10))) for _ in range(8))
    no_str1 = 'No ' + no_str # 随机生成8位数字发票号码
    draw.text((1370, 86), no_str, fill = (48, 87, 161), font = global_var.ft2)  # 添加发票号码
    draw.text((1585, 146), no_str, fill = (8, 67, 161), font = global_var.ft4)  # 添加小号码
    # 大的号码坐标
    x1, y1 = 1366, 88
    x2, y2 = 1591, 88
    x3, y3 = 1366, 135
    x4, y4 = 1591, 135
    x_text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    # 小的号码坐标
    sx1, sy1 = 1585, 146
    sx2, sy2 = 1707, 146
    sx3, sy3 = 1585, 174
    sx4, sy4 = 1707, 174
    sx_text = xy_end(sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(x_text + no_str1 + '\n')
        f.write(sx_text + no_str + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as fname :
        fname.write("发票基本信息_发票号码" + '\t' + no_str1 + '\n')


# 主函数
def add(time_str) :
    add_fapiao_daima()  # 添加发票代码
    add_fapiao_hao()  # 添加发票号码
    print_date()  # 生成日期函数
    add_name()  # 添加收款人复核人开票人名字
    purchase()  # 购买方区域文字添加
    password()  # 添加密码区
    add_goods()  # 添加货物或应税劳务及后面对应的规格价格等内容
    add_seller()  # 添加销售方内容
    seller_nums()  # 添加纳税人识别号（销售方）
    add_and_phone()  # 添加地址、电话（销售方）
    add_bankId()  # 添加开户行及账号
    # global_var.im.show()

    im.save('template0\\pic_origin\\res' + str(index) + '.jpg')  # 保存添加完的图片

    # 旋转图片
    img = cv.imread('template0\\pic_origin\\res' + str(index) + '.jpg')
    sp.split_to_box(img, time_str)
    rot_mat = cv.getRotationMatrix2D((cx, cy), rotate_angle, 1)
    img_rotated_by_alpha = cv.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]))
    blur_num = int(random.choice(['1', '3', '1', '1']))  # 模糊图片的程度
    dst_img = cv.GaussianBlur(img_rotated_by_alpha, (blur_num, blur_num), 0)

    cv.imwrite('template0\\res\\rotate\\pic' + time_str + '.jpg', dst_img)  # 保存高斯模糊处理+仿射变换后的图片
    print(index)


def before_add(template_num) :
    if template_num == 1 :
        name = "上海增值税专用发票"
    elif template_num == 2 :
        name = "湖北增值税专用发票"
    elif template_num == 3 :
        name = "江苏增值税专用发票"
    else :
        name = "内蒙古增值税专用发票"

    a1, b1 = 695, 49
    a2, b2 = 1205, 49
    a3, b3 = 695, 105
    a4, b4 = 1205, 105
    fapiao = xy_end(a1, b1, a2, b2, a3, b3, a4, b4)
    with open(filename, 'a+', encoding = 'utf-8') as f :
        f.write(fapiao + name + '\n')
    with open(kv_filename, 'a+', encoding = 'utf-8') as f :
        f.write("发票基本信息_发票类型" + '\t' + "专用发票" + '\n')
        f.write("发票基本信息_发票名称" + '\t' + name + '\n')


def main() :
    global index
    import setup
    args = setup.parser_args()
    for index in range(args.amount) :
        global im
        global draw
        global filename
        global kv_filename
        global rotate_angle
        global cx, cy
        template_num = random.randint(1, 4)
        im = Image.open('template0\\pic_template\\template_' + str(template_num) + '.jpg')  # 随机挑选一个模板图
        draw = ImageDraw.Draw(im)
        rotate_angle = 0
        # rotate_angle = random.uniform(-args.angle, args.angle)  # 生成随机的旋转角度（正数为逆时针）
        '''
        模板图片尺寸和处理后的图片尺寸是一致的
        所以中心点是一样的
        '''
        img_tmp = cv.imread('template0\\pic_template\\template_' + str(template_num) + '.jpg')
        h, w, c = img_tmp.shape  # 获取图片的高和宽
        cx, cy = w / 2, h / 2  # 得到中心坐标点

        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d_%H-%M') + '_' + str(index)

        filename = 'template0\\res\\txt\\pic' + time_str + '.txt'
        kv_filename = 'template0\\res\\key_value\\pic' + time_str + '_kv.txt'
        before_add(template_num)
        add(time_str)
        if args.strong_if == 1 :
            strong_picture.adjust(time_str)
        # correct_rotate.main(time_str)
    return 0
