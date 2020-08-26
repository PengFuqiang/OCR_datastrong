#!\\usr\\bin\\env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020\\7\\30 0030
import random

import cv2 as cv
from PIL import Image
from PIL import ImageDraw
from faker import Faker
from numpy import sin, cos, pi

import template2.tmp2_split_pic as sp
import global_var as gl
import template2.tmp2_strong_pic as strong

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
        m44) + ',' + str(n44) + ',')


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
        last_str.replace('零角零分', '圆整')
    elif '零分' in last_str :
        last_str.replace('零分', '')
    # elif '零角' in last_str and '分' not in last_str :
    #     last_str.replace('零角', '圆整')
    # print(last_str)
    return last_str


# 生成日期函数
def print_date() :
    date = fake.date(pattern = '%Y年%m月%d日')
    draw.text((1480, 196), date, fill = (25, 82, 234), font = gl.ft5)
    # 日期的坐标
    x1, y1 = 1480, 196
    x2, y2 = 1714, 196
    x3, y3 = 1480, 226
    x4, y4 = 1714, 226
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + date + '\n')
    with open(kv_filename, 'a+') as fname :
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
    draw.text((365, 254), name, fill = (25, 82, 234), font = gl.ft6)
    name_length = len(name)
    x_start, y_start = 365, 254
    x_end, y_end = 365 + (name_length * 27), 254 + 30

    x1, y1 = x_start, y_start
    x2, y2 = x_end, y_start
    x3, y3 = x_start, y_end
    x4, y4 = x_end, y_end
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + name + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("购买方_名称" + '\t' + name + '\n')

    # 添加纳税人识别号
    id_num = ''.join(str(random.choice(range(10))) for _ in range(15))  # 随机生成15位纳税人识别号
    draw.text((386, 298), id_num, fill = (25, 82, 234), font = gl.ft7)
    id_x1, id_y1 = 386, 298
    id_x2, id_y2 = 756, 298
    id_x3, id_y3 = 386, 328
    id_x4, id_y4 = 756, 328
    text = xy_end(id_x1, id_y1, id_x2, id_y2, id_x3, id_y3, id_x4, id_y4)
    with open(filename, 'a+') as f :
        f.write(text + id_num + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("购买方_纳税人识别号" + '\t' + id_num + '\n')
    # 添加地址电话
    phone1 = ''.join(str(random.choice(range(10))) for _ in range(3))
    phone2 = ''.join(str(random.choice(range(10))) for _ in range(7))
    address = fake.address()[0 : -7]
    add_len = len(address)
    address_phone = address + ' ' + phone1 + '-' + phone2
    draw.text((354, 350), address_phone, fill = (25, 82, 234), font = gl.ft8)
    add_ph_x1, add_ph_y1 = 354, 350
    add_ph_x2, add_ph_y2 = 354 + 21 * (add_len + 1) + 12 * 10, 350  # 十个号码加一个空格一个斜杠以及地址长度
    add_ph_x3, add_ph_y3 = 354, 350 + 24
    add_ph_x4, add_ph_y4 = 354 + 21 * (add_len + 1) + 12 * 10, 350 + 24
    text = xy_end(add_ph_x1, add_ph_y1, add_ph_x2, add_ph_y2, add_ph_x3, add_ph_y3, add_ph_x4, add_ph_y4)
    with open(filename, 'a+') as f :
        f.write(text + address_phone + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("购买方_地址、电话" + '\t' + address_phone + '\n')

    # 添加开户行及账号
    bank1 = ['招商银行', '汉口银行', 'EBA银行']
    bank2 = ['龙阳大道支行', '北京东三环支行', '上海分行', '城北支行']
    # 15或18位账号
    acc = [''.join(str(random.choice(range(10))) for _ in range(15)),
           ''.join(str(random.choice(range(10))) for _ in range(18))]
    bank = random.choice(bank1) + random.choice(bank2)
    acc = random.choice(acc)
    bank_len, acc_len = len(bank), len(acc)
    bank_account = bank + ' ' + acc
    draw.text((354, 388), bank_account, fill = (25, 82, 234), font = gl.ft6)
    bank_x1, bank_y1 = 354, 388
    bank_x2, bank_y2 = 354 + bank_len * 26 + 14 * acc_len, 388
    bank_x3, bank_y3 = 354, 388 + 30
    bank_x4, bank_y4 = 354 + bank_len * 26 + 14 * acc_len, 388 + 30
    text = xy_end(bank_x1, bank_y1, bank_x2, bank_y2, bank_x3, bank_y3, bank_x4, bank_y4)
    with open(filename, 'a+') as f :
        f.write(text + bank_account + '\n')
    with open(kv_filename, 'a+') as fname :
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
    draw.text((1100, 268), pwd1, fill = (25, 82, 234), font = gl.ft9)
    draw.text((1100, 301), pwd2, fill = (25, 82, 234), font = gl.ft9)
    draw.text((1100, 334), pwd3, fill = (25, 82, 234), font = gl.ft9)
    draw.text((1100, 367), pwd4, fill = (25, 82, 234), font = gl.ft9)
    # 第一行密码的坐标
    pwd1_x1, pwd1_y1 = 1100, 268
    pwd1_x2, pwd1_y2 = 1700, 268
    pwd1_x3, pwd1_y3 = 1100, 301
    pwd1_x4, pwd1_y4 = 1700, 301
    pwd1_text = xy_end(pwd1_x1, pwd1_y1, pwd1_x2, pwd1_y2, pwd1_x3, pwd1_y3, pwd1_x4, pwd1_y4)
    # 第二行密码的坐标
    pwd2_x1, pwd2_y1 = 1100, 301
    pwd2_x2, pwd2_y2 = 1700, 301
    pwd2_x3, pwd2_y3 = 1100, 334
    pwd2_x4, pwd2_y4 = 1700, 334
    pwd2_text = xy_end(pwd2_x1, pwd2_y1, pwd2_x2, pwd2_y2, pwd2_x3, pwd2_y3, pwd2_x4, pwd2_y4)
    # 第三行密码的坐标
    pwd3_x1, pwd3_y1 = 1100, 334
    pwd3_x2, pwd3_y2 = 1700, 334
    pwd3_x3, pwd3_y3 = 1100, 367
    pwd3_x4, pwd3_y4 = 1700, 367
    pwd3_text = xy_end(pwd3_x1, pwd3_y1, pwd3_x2, pwd3_y2, pwd3_x3, pwd3_y3, pwd3_x4, pwd3_y4)
    # 第四行密码的坐标
    pwd4_x1, pwd4_y1 = 1100, 367
    pwd4_x2, pwd4_y2 = 1700, 367
    pwd4_x3, pwd4_y3 = 1100, 400
    pwd4_x4, pwd4_y4 = 1700, 400
    pwd4_text = xy_end(pwd4_x1, pwd4_y1, pwd4_x2, pwd4_y2, pwd4_x3, pwd4_y3, pwd4_x4, pwd4_y4)
    with open(filename, 'a+') as f :
        f.write(pwd1_text + pwd1 + '\n')
        f.write(pwd2_text + pwd2 + '\n')
        f.write(pwd3_text + pwd3 + '\n')
        f.write(pwd4_text + pwd4 + '\n')


# 添加货物或应税劳务及后面对应的规格价格等内容
def add_goods() :
    """
    货物，型号，单位等每个字符长为26高为29
    其余数字字符宽为13或19
    """
    types = ['g', '\\', '*', '+', 'g', 'l', '-', '#', '!', '~', 'h']
    # units = ['升', '次', '支', '件', '袋', '只', '瓶', '盒', '块', '']
    amounts = [random.randint(1, 10), random.randint(1, 100),
               random.randint(1, 1000), random.randint(1, 2000)]
    unit_prices = [round(random.uniform(0, 10), 2), round(random.uniform(0, 100), 2),
                   round(random.uniform(0, 1000), 2)]
    rate = random.choice(range(1, 20))  # 求对应的税率
    total1 = 0  # 各个金额之和
    total2 = 0  # 各个税额之和
    total = 0

    for i in range(4) :
        y = 476 + (30 * i)
        goods = fake.sentence()
        standards = fake.word() + random.choice(types)  # 长度为3
        units = random.choice(fake.word())  # 长度为1
        if len(goods) > 14 :
            goods = goods[0 : 14]  # 避免字符串过长
        else :
            goods = goods[0 : -1]  # 去掉最后的标点符号
        goods_len = len(goods)
        draw.text((92, y), goods, fill = (25, 82, 234), font = gl.ft6)  # 添加货物
        draw.text((536, y), standards, fill = (25, 82, 234), font = gl.ft6)  # 添加型号规格
        draw.text((740, y), units, fill = (25, 82, 234), font = gl.ft6)  # 添加单位

        # 获取货物，型号，单位旋转后的坐标
        goods_x1, goods_y1 = 92, y
        goods_x2, goods_y2 = 92 + goods_len * 26, y
        goods_x3, goods_y3 = 92, y + 29
        goods_x4, goods_y4 = 92 + goods_len * 26, y + 29
        goods_text = xy_end(goods_x1, goods_y1, goods_x2, goods_y2, goods_x3, goods_y3, goods_x4, goods_y4)

        standards_x1, standards_y1 = 536, y
        standards_x2, standards_y2 = 536 + 70, y  # 规格字符宽为70
        standards_x3, standards_y3 = 536, y + 29
        standards_x4, standards_y4 = 536 + 70, y + 29
        standards_text = xy_end(standards_x1, standards_y1, standards_x2, standards_y2, standards_x3, standards_y3,
                                standards_x4, standards_y4)

        units_x1, units_y1 = 740, y
        units_x2, units_y2 = 740 + 26, y
        units_x3, units_y3 = 740, y + 29
        units_x4, units_y4 = 740 + 26, y + 29
        units_text = xy_end(units_x1, units_y1, units_x2, units_y2, units_x3, units_y3, units_x4, units_y4)
        # 最终坐标写入到文件中
        with open(filename, 'a+') as f :
            f.write(goods_text + goods + '\n')
            f.write(standards_text + standards + '\n')
            f.write(units_text + units + '\n')
        with open(kv_filename, 'a+') as fname :
            fname.write("货物或应税劳务、服务名称" + '\t' + goods + '\n')
            fname.write("规格型号" + '\t' + standards + '\n')
            fname.write("单位" + '\t' + units + '\n')

        amount = random.choice(amounts)  # 取对应的数量
        unit_price = random.choice(unit_prices)  # 取单价
        total_price = amount * unit_price  # 求对应的金额
        tax_amount = rate * total_price * 0.01  # 求对应的税额
        total1 += total_price
        total2 += tax_amount
        draw.text((850, y), str(amount).rjust(8), fill = (25, 82, 234), font = gl.ft13)  # 添加数量
        # 计算商品数量的坐标
        amount_x1, amount_y1 = 850 + 12 * (8 - len(str(amount))), y
        amount_x2, amount_y2 = 970, y
        amount_x3, amount_y3 = 850 + 12 * (8 - len(str(amount))), y + 29
        amount_x4, amount_y4 = 970, y + 29
        amount_text = xy_end(amount_x1, amount_y1, amount_x2, amount_y2, amount_x3, amount_y3, amount_x4, amount_y4)
        # 计算单价的坐标
        draw.text((1024, y), ("%.2f" % unit_price).rjust(8), fill = (25, 82, 234), font = gl.ft13)  # 添加单价
        unit_price_x1, unit_price_y1 = 1024 + 13 * (8 - len(str(round(unit_price, 2)))), y
        unit_price_x2, unit_price_y2 = 1142, y
        unit_price_x3, unit_price_y3 = 1024 + 13 * (8 - len(str(round(unit_price, 2)))), y + 29
        unit_price_x4, unit_price_y4 = 1142, y + 29
        unit_price_text = xy_end(unit_price_x1, unit_price_y1, unit_price_x2, unit_price_y2, unit_price_x3,
                                 unit_price_y3, unit_price_x4, unit_price_y4)
        # 计算金额的坐标
        draw.text((1218, y), ("%.2f" % total_price).rjust(11), fill = (25, 82, 234), font = gl.ft13)  # 添加金额
        total_price_x1, total_price_y1 = 1218 + 13 * (8 - len(str(round(total_price, 2)))), y
        total_price_x2, total_price_y2 = 1400, y
        total_price_x3, total_price_y3 = 1218 + 13 * (8 - len(str(round(total_price, 2)))), y + 29
        total_price_x4, total_price_y4 = 1400, y + 29
        total_price_text = xy_end(total_price_x1, total_price_y1, total_price_x2, total_price_y2, total_price_x3,
                                  total_price_y3, total_price_x4, total_price_y4)

        # 计算税率的坐标
        draw.text((1425, y), str(rate) + '%', fill = (25, 82, 234), font = gl.ft13)  # 添加税率
        rate_x1, rate_y1 = 1425, y
        rate_x2, rate_y2 = 1485, y
        rate_x3, rate_y3 = 1425, y + 29
        rate_x4, rate_y4 = 1485, y + 29
        rate_text = xy_end(rate_x1, rate_y1, rate_x2, rate_y2, rate_x3, rate_y3, rate_x4, rate_y4)
        # 计算税额的坐标
        draw.text((1580, y), ("%.2f" % tax_amount).rjust(10), fill = (25, 82, 234), font = gl.ft13)  # 添加税额
        tax_x1, tax_y1 = 1580 + 13 * (10 - len(str(round(tax_amount, 2)))), y
        tax_x2, tax_y2 = 1740, y
        tax_x3, tax_y3 = 1580 + 13 * (10 - len(str(round(tax_amount, 2)))), y + 29
        tax_x4, tax_y4 = 1740, y + 29
        tax_text = xy_end(tax_x1, tax_y1, tax_x2, tax_y2, tax_x3, tax_y3, tax_x4, tax_y4)
        with open(filename, 'a+') as f :  # 写入坐标信息
            f.write(amount_text + str(amount) + '\n')
            f.write(unit_price_text + str(unit_price) + '\n')
            f.write(total_price_text + ("%.2f" % total_price) + '\n')
            f.write(rate_text + str(rate) + '%' + '\n')
            f.write(tax_text + ("%.2f" % tax_amount) + '\n')
        with open(kv_filename, 'a+') as fname :
            fname.write("数量" + '\t' + str(amount) + '\n')
            fname.write("单价" + '\t' + str(unit_price) + '\n')
            fname.write("金额" + '\t' + ("%.2f" % total_price) + '\n')
            fname.write("税率" + '\t' + str(rate) + '%' + '\n')
            fname.write("税额" + '\t' + ("%.2f" % tax_amount) + '\n')
    # 计算总价
    total = total1 + total2
    big_total = digital_to_chinese(round(total, 2))  # 总金额取两位并转为大写
    # 添加金额前的￥符号
    draw.text((1172, 748), '￥', fill = (25, 82, 234), font = gl.ft12)
    draw.text((1518, 748), '￥', fill = (25, 82, 234), font = gl.ft12)
    draw.text((1404, 812), '￥', fill = (25, 82, 234), font = gl.ft12)

    draw.text((1202, 748), ("%.2f" % total1), fill = (70, 93, 223), font = gl.ft10)  # 添加金额之和
    draw.text((1548, 748), ("%.2f" % total2), fill = (70, 93, 223), font = gl.ft10)  # 添加税额之和
    draw.text((1434, 812), ("%.2f" % total), fill = (70, 93, 223), font = gl.ft10)  # 添加金额税额之和
    draw.text((590, 812), big_total, fill = (70, 93, 223), font = gl.ft11)  # 添加金额税额之和的中文大写
    # 金额之和坐标
    total1_x1, total1_y1 = 1202, 748
    total1_x2, total1_y2 = 1202 + 19 * len(str("%.2f" % total1)), 748
    total1_x3, total1_y3 = 1202, 778
    total1_x4, total1_y4 = 1202 + 19 * len(str("%.2f" % total1)), 778
    total1_text = xy_end(total1_x1, total1_y1, total1_x2, total1_y2, total1_x3, total1_y3, total1_x4, total1_y4)

    # 税额之和坐标
    total2_x1, total2_y1 = 1548, 748
    total2_x2, total2_y2 = 1548 + 19 * len("%.2f" % total2), 748
    total2_x3, total2_y3 = 1548, 778
    total2_x4, total2_y4 = 1548 + 19 * len("%.2f" % total2), 778
    total2_text = xy_end(total2_x1, total2_y1, total2_x2, total2_y2, total2_x3, total2_y3, total2_x4, total2_y4)

    # 金额+税额之和的坐标
    total_x1, total_y1 = 1434, 812
    total_x2, total_y2 = 1434 + 19 * len("%.2f" % total), 812
    total_x3, total_y3 = 1434, 842
    total_x4, total_y4 = 1434 + 19 * len("%.2f" % total), 842
    total_text = xy_end(total_x1, total_y1, total_x2, total_y2, total_x3, total_y3, total_x4, total_y4)

    # 大写金额税额之和的坐标
    big_x1, big_y1 = 590, 812
    big_x2, big_y2 = 590 + 26 * len(big_total), 812
    big_x3, big_y3 = 590, 842
    big_x4, big_y4 = 590 + 26 * len(big_total), 842
    big_text = xy_end(big_x1, big_y1, big_x2, big_y2, big_x3, big_y3, big_x4, big_y4)
    # 写入坐标
    with open(filename, 'a+') as f :
        f.write(total1_text + '￥' + ("%.2f" % total1) + '\n')
        f.write(total2_text + '￥' + ("%.2f" % total2) + '\n')
        f.write(total_text + '￥' + ("%.2f" % total) + '\n')
        f.write(big_text + big_total + '\n')
    with open(kv_filename, 'a+') as fname :
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
    draw.text((350, 875), seller_name, fill = (25, 82, 234), font = gl.ft6)
    x1, y1 = 350, 875
    x2, y2 = 350 + 27 * len(seller_name), 875
    x3, y3 = 350, 875 + 30
    x4, y4 = 350 + 27 * len(seller_name), 875 + 30
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + seller_name + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("销售方_名称" + '\t' + seller_name + '\n')


def seller_nums() :  # 添加纳税人识别号（销售方）
    """
    宽为20高为30
    """
    id_part = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', chr(random.randint(65, 90))]
    id1 = ''.join(str(random.choice(id_part)) for _ in range(18))
    id2 = ''.join(str(random.choice(id_part)) for _ in range(15))
    seller_num = random.choice([id1, id2])
    draw.text((392, 912), seller_num, fill = (70, 93, 223), font = gl.ft7)
    x1, y1 = 392, 912
    x2, y2 = 392 + 20 * len(seller_num), 912
    x3, y3 = 392, 942
    x4, y4 = 392 + 20 * len(seller_num), 942
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + seller_num + '\n')
    with open(kv_filename, 'a+') as fname :
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
    draw.text((350, 960), address_phone, fill = (25, 82, 234), font = gl.ft8)
    x1, y1 = 350, 960
    x2, y2 = 350 + 27 * (add_len + 1) + 14 * 7, 960
    x3, y3 = 350, 990
    x4, y4 = 350 + 27 * (add_len + 1) + 14 * 7, 990
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + address_phone + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("销售方_地址、电话" + '\t' + address_phone + '\n')


def add_bankId() :  # 添加开户行及账号
    """
    银行名称字符宽为27，账号宽为14
    """
    bank1 = ['招商银行', '汉口银行', 'EBA银行']
    bank2 = ['龙阳大道支行', '北京东三环支行', '上海分行', '城北支行']
    bank = random.choice(bank1) + random.choice(bank2)
    bank_len = len(bank)
    # 15或18位账号
    acc = [''.join(str(random.choice(range(10))) for _ in range(15)),
           ''.join(str(random.choice(range(10))) for _ in range(18))]
    account = random.choice(acc)
    acc_len = len(account)
    bank_and_account = bank + ' ' + account
    draw.text((350, 998), bank_and_account, fill = (25, 82, 234), font = gl.ft6)
    x1, y1 = 350, 998
    x2, y2 = 350 + 27 * (bank_len + 1) + 14 * acc_len, 998
    x3, y3 = 350, 1028
    x4, y4 = 350 + 27 * (bank_len + 1) + 14 * acc_len, 1028
    text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    with open(filename, 'a+') as f :
        f.write(text + bank_and_account + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("销售方_开户行及账号" + '\t' + bank_and_account + '\n')
        fname.write("备注")


def add_name() :
    # 添加收款人复核人开票人名字
    # 生成随机的三个名字
    name1 = fake.name()
    name2 = fake.name()
    name3 = fake.name()
    draw.text((220, 1044), name1, fill = (25, 82, 234), font = gl.ft6)
    draw.text((660, 1044), name2, fill = (25, 82, 234), font = gl.ft6)
    draw.text((1055, 1044), name3, fill = (25, 82, 234), font = gl.ft6)

    n1_x1, n1_y1 = 220, 1044
    n1_x2, n1_y2 = 220 + 27 * len(name1), 1044
    n1_x3, n1_y3 = 220, 1074
    n1_x4, n1_y4 = 220 + 27 * len(name1), 1074
    n1_text = xy_end(n1_x1, n1_y1, n1_x2, n1_y2, n1_x3, n1_y3, n1_x4, n1_y4)

    n2_x1, n2_y1 = 660, 1044
    n2_x2, n2_y2 = 660 + 27 * len(name2), 1044
    n2_x3, n2_y3 = 660, 1074
    n2_x4, n2_y4 = 660 + 27 * len(name2), 1074
    n2_text = xy_end(n2_x1, n2_y1, n2_x2, n2_y2, n2_x3, n2_y3, n2_x4, n2_y4)

    n3_x1, n3_y1 = 1055, 1044
    n3_x2, n3_y2 = 1055 + 27 * len(name2), 1044
    n3_x3, n3_y3 = 1055, 1074
    n3_x4, n3_y4 = 1055 + 27 * len(name2), 1074
    n3_text = xy_end(n3_x1, n3_y1, n3_x2, n3_y2, n3_x3, n3_y3, n3_x4, n3_y4)
    with open(filename, 'a+') as f :
        f.write(n1_text + name1 + '\n')
        f.write(n2_text + name2 + '\n')
        f.write(n3_text + name3 + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("发票基本信息_收款人" + '\t' + name1 + '\n')
        fname.write("发票基本信息_复核" + '\t' + name2 + '\n')
        fname.write("发票基本信息_开票人" + '\t' + name3 + '\n')


# 添加发票代码
def add_fapiao_daima() :
    num_str = ''.join(str(random.choice(range(10))) for _ in range(10))  # 随机生成10位数字发票代码
    draw.text((250, 84), num_str, fill = (72, 75, 68), font = gl.ft1)  # 添加发票代码
    draw.text((1594, 114), num_str, fill = (25, 82, 234), font = gl.ft3)  # 添加号码后面的小代码
    # 大的发票代码的坐标
    x1, y1 = 250, 84
    x2, y2 = 555, 84
    x3, y3 = 250, 132
    x4, y4 = 555, 132
    x_text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    # 小的发票代码的坐标
    sx1, sy1 = 1594, 114
    sx2, sy2 = 1736, 114
    sx3, sy3 = 1594, 136
    sx4, sy4 = 1736, 136
    sx_text = xy_end(sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4)

    with open(filename, 'a+') as f :
        f.write(x_text + num_str + '\n')
        f.write(sx_text + num_str + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("发票基本信息_发票代码" + '\t' + num_str + '\n')


# 添加发票号码
def add_fapiao_hao() :
    no_str = ''.join(str(random.choice(range(10))) for _ in range(8))  # 随机生成8位数字发票号码
    draw.text((1326, 82), no_str, fill = (25, 82, 234), font = gl.ft2)  # 添加发票号码
    draw.text((1574, 148), no_str, fill = (25, 82, 234), font = gl.ft4)  # 添加小号码
    # 大的号码坐标
    x1, y1 = 1326, 82
    x2, y2 = 1551, 82
    x3, y3 = 1326, 129
    x4, y4 = 1551, 129
    x_text = xy_end(x1, y1, x2, y2, x3, y3, x4, y4)
    # 小的号码坐标
    sx1, sy1 = 1574, 148
    sx2, sy2 = 1736, 148
    sx3, sy3 = 1574, 175
    sx4, sy4 = 1736, 175
    sx_text = xy_end(sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4)
    with open(filename, 'a+') as f :
        f.write(x_text + no_str + '\n')
        f.write(sx_text + no_str + '\n')
    with open(kv_filename, 'a+') as fname :
        fname.write("发票基本信息_发票号码" + '\t' + no_str + '\n')


# 主函数
def add() :
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
    # 对图片进行增强

    im.save('template2\\tmp2_pic_origin\\res' + str(index) + '.jpg')  # 保存添加完的图片

    # 图片仿射变换
    img = cv.imread('template2\\tmp2_pic_origin\\res' + str(index) + '.jpg')
    sp.split_to_box(img, index)
    rot_mat = cv.getRotationMatrix2D((cx, cy), rotate_angle, 1)
    img_rotated_by_alpha = cv.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]))
    blur_num = int(random.choice(['1', '3', '3', '5', '5']))  # 模糊的程度
    dst_img = cv.GaussianBlur(img_rotated_by_alpha, (blur_num, blur_num), 0)
    # dir_name = 'test\\res\\res' + str(index)
    # os.mkdir(dir_name)

    cv.imwrite('template2\\tmp2_res\\rotate\\pic' + str(index) + '.jpg', dst_img)  # 保存高斯模糊处理+仿射变换后的图片
    print(index)


def before_add(template_num) :
    if template_num == 1 :
        name = "深圳增值税专用发票"
    else :
        name = "广东增值税专用发票"
    with open(kv_filename, 'a+') as f :
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
        template_num = random.randint(1, 2)
        im = Image.open('template2\\tmp2_pic_template\\pic' + str(template_num) + '.jpg')  # 随机挑选一个模板图
        draw = ImageDraw.Draw(im)
        rotate_angle = 0
        # rotate_angle = random.randint(-7, 7)  # 生成随机的旋转角度（正数为逆时针）
        '''
        模板图片尺寸和处理后的图片尺寸是一致的
        所以中心点是一样的
        '''
        img_tmp = cv.imread('template2\\tmp2_pic_template\\pic' + str(template_num) + '.jpg')
        h, w, c = img_tmp.shape  # 获取图片的高和宽
        cx, cy = w / 2, h / 2  # 得到中心坐标点
        filename = 'template2\\tmp2_res\\txt\\pic' + str(index) + '.txt'
        kv_filename = 'template2\\tmp2_res\\key_value\\pic' + str(index) + '_kv.txt'
        before_add(template_num)
        add()
    if args.strong_if == 1 :
        strong.adjust()
    return 0
