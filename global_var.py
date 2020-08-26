#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：pfq time:2020/7/14

from PIL import ImageFont


ft1 = ImageFont.truetype("fonts/fapiao_daima.ttf", 55)  # 发票代码字体
ft2 = ImageFont.truetype("fonts/fapiao_haoma.ttf", 50)  # 发票号码字体
ft3 = ImageFont.truetype("fonts/fapiao_daima.ttf", 25)
ft4 = ImageFont.truetype("fonts/fapiao_daima.ttf", 30)
ft5 = ImageFont.truetype("fonts/kaipiao_riqi.ttf", 23)  # 开票日期字体

ft6 = ImageFont.truetype("fonts/mingcheng.ttf", 25)  # 名称字体
ft7 = ImageFont.truetype("fonts/shibiehao.ttf", 32)  # 纳税人识别号字体
ft8 = ImageFont.truetype("fonts/mingcheng.ttf", 22)  # 地址电话字体
ft9 = ImageFont.truetype("fonts/shibiehao.ttf", 35)  # 密码区字体
ft10 = ImageFont.truetype("fonts/shibiehao.ttf", 32)  # 总金额，总税额字体
ft11 = ImageFont.truetype("fonts/simsun.ttc", 25)
ft12 = ImageFont.truetype("fonts/jin_e.ttf", 30)  # 金额￥字体
ft13 = ImageFont.truetype("fonts/fapiao_daima.ttf", 25)  # 单价等字体

# 姓
first_name = '赵钱孙李周吴郑王冯陈卫蒋沈韩杨朱秦尤许何吕张孔曹严华金魏陶姜戚谢邹喻苏潘葛范彭郎鲁韦马苗花方俞任袁柳鲍史唐薛雷贺倪' \
             '汤殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平黄和穆萧尹姚邵汪祁毛禹狄米贝明臧计成戴宋庞熊纪舒屈项祝董粱杜阮季强贾路' \
             '娄危江童颜郭梅盛林钟徐邱骆高夏蔡田胡凌霍万柯卢莫房解应宗丁宣邓郁单杭洪包左石崔吉龚程邢裴陆荣翁荀甄家封储靳焦牧山蔡' \
             '田胡霍万柯卢莫房干谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘逄姬冉桂牛燕尚温庄晏瞿习容向古居步耿文东曾关红'
# 名字第二字
second_name = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣' \
              '叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭' \
              '冰爽琬茗羽希宁欣飘育馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽伟刚勇毅楠俊峰强军平保东文辉力明永健世广志义兴' \
              '良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群' \
              '豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德' \
              '行时泰盛雄琛钧冠策腾榕风航弘'
# 名字第三字
last_name = '强 丹 海 明 良 逸 臣 月 知 时 节 好 雨 春 生 鸟 静 新 白 然 浩 隐 右 京 平 杰 天 军 保 兴 航 玉 红 卿 梦 苗 贞 ' \
            '晓 珊 倩 浅 颜 言 之 一 伊 易 衣 宜 懿 杭 豪 娴 瑾 颖 露 瑶 怡 婵 雁 蓓 纨 仪 荷 丹 清 飞 彬 富 顺 信 子 杰 涛 ' \
            '昌 成 康 星 伦 翔 旭 鹏 泽 晨 辰 士 以 建 家 致 树 炎 冰 爽 琬 茗 羽 希 宁 欣 飘 育                           '

