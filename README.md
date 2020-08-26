# ocr
###### 目录结构
```
template0
├── pic_origin  # 添加文字后的原始图
├── pic_template  # 添加文字的模板图片
├── __pycache__
└── res # 图片增强结果
    ├── bright  # 亮度增强图片
    ├── color # 色度增强图片
    ├── contrast  # 对比度增强图片
    ├── part_bright # 局部增强图片
    ├── rotate  # 图片随机旋转
    ├── sharp # 锐度增强图片
    ├── splits  # 图片分割结果
    │   ├── spl0  # 表示pic_origin中的pic0的分割结果
    │   ├── spl1
    │   ├── spl2
    │   ├── spl3
    │   ├── spl4
    │   ├── spl5
    │   ├── spl6
    │   ├── spl7
    │   ├── spl8
    │   └── spl9
    └── txt # 图片标注信息文件

```
*setup.py是运行文件，global_var.py是字体等设置文件，fonts是字体库，template1和template2具有相同的结构。*  
*通过python setup.py生成图片，默认取library0中的模板图片，生成10张旋转角度范围在（-7.0,7.0）的图片及其切割结果和标注文件。*  
**通过加参数来设置生成图片的数量**

| library | amount | angle | strong_if | num | strong_type |
| ------ | ------ | ------ | ------ | ------ | ------ |
| 图片库号 | 图片数量 | 旋转角度范围 | 是否增强图片 | 每张图片增强的数量 | 增强类型 |
| 0,1,2默认为0 | 默认为10 | 默认为7.0 | 0,1默认为0不增强 | 默认为5 | 默认为none，所有类型都增强 |  

**需要增强某种类型或生成更多某种类型图片可以设置如下参数**  


| bright_limit | color_limit | contrast_limit | sharp_limit | part_bright_coe |
| ------ | ------ | ------ | ------ | ------ | 
| 亮度范围 | 色度范围 | 对比度范围 | 锐度范围 | 局部亮度 | 
| 默认为0.5（1.0±0.5） | 默认为1.0 | 默认为0.5 | 默认2.0±2.0 | 默认为50（0,50）该区域像素减小的值 | 
