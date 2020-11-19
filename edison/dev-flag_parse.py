#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-19 14:17:59

import argparse

from . import yaml_conf

# ArgumentParser.add_argument(
# name or flags...
# [, type]
# [, choices]
# [, required]
# [, help]

# parser.exit(status=rc)

flag_dict = yaml_conf.get_data("../flag.yml")
flags = flag_dict["flags"]


def parser():
    parser = argparse.ArgumentParser(description=flag_dict["description"])
    vers = "%(progs)s {}".format(flag_dict["version"])
    parser.add_argument("--version", action="version", version="%s" % vers)
    parser.add_argument("--quiet", action="store_true", help="")
    for flag in flags:

        def add_flag(is_required=True):
            try:
                if flag["type"] == "bool":
                    parser.add_argument(
                        "--%s" % flag["name"],
                        type=bool,
                        choices=[True, False],
                        required=is_required,
                        help=flag["help"],
                    )
            except KeyError:
                try:
                    parser.add_argument(
                        "--%s" % flag["name"],
                        choices=flag["choices"],
                        required=is_required,
                        help=flag["help"],
                    )
                except KeyError:
                    parser.add_argument(
                        "--%s" % flag["name"],
                        required=is_required,
                        help=flag["help"],
                    )

        if flag.required:
            add_flag()
        else:
            add_flag(False)


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
