#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 01:54:15
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-23 10:56:06

import yaml


def get_data(file):
    with open(file, mode="r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data
