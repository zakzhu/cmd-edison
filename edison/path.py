#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 08:59:03
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-23 10:56:00

import os


def dirname(current_file):
    return os.path.dirname(os.path.abspath(current_file))


def name(current_file, basename):
    return os.path.join(dirname(current_file), basename)
