#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 03:36:22
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-16 10:43:33

import argparse

from edison import command, path, yaml_conf

workdir = path.dirname(__file__)

flag_file = path.name(workdir, "flag.yml")
help_file = path.name(workdir, "help.yml")


def main():
    print(flag_file, help_file)


if __name__ == "__main__":
    main()
