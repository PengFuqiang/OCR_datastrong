#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: pfq time: 2020/7/31 0031

import argparse

import template0.add_text
import template1.tmp1_add_text
import template2.tmp2_add_text


def parser_args() :
    parser = argparse.ArgumentParser(description = 'Create pictures parameter')

    parser.add_argument('-library', type = int, default = 0,
                        help = 'the num of template picture library, between 0 and 2')

    parser.add_argument('-amount', type = int, default = 10, help = 'how many pictures will be created')

    parser.add_argument('-angle', type = float, default = 7.0, help = 'rotate angle of pic')

    parser.add_argument('-bright_limit', type = float, default = 0.3, help = 'the bright coe, limited 0 and 2')

    parser.add_argument('-color_limit', type = float, default = 0.5, help = 'the color coe, between 0 and 2')

    parser.add_argument('-contrast_limit', type = float, default = 0.3, help = 'the contrast coe, between 0 and 2')

    parser.add_argument('-sharp_limit', type = float, default = 2.0, help = 'the sharp coe, between 0 and 4')

    parser.add_argument('-part_bright_coe', type = int, default = 50, help = 'the num of px to bright,between 0 and 50')

    parser.add_argument('-num', type = int, default = 1, help = 'the num of strong pictures')

    parser.add_argument('-strong_if', type = int, default = 0, help = '1 is strong pic, 0 is don\'t strong pic')

    parser.add_argument('-strong_type', default = 'none',
                        help = 'the type includes bright, color, contrast, sharp and part_bright')

    p_args = parser.parse_args()
    return p_args


if __name__ == '__main__' :
    args = parser_args()
    if args.library == 0 :
        template0.add_text.main()
    elif args.library == 1 :
        template1.tmp1_add_text.main()
    else :
        template2.tmp2_add_text.main()
