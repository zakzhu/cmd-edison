#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-23 11:13:15

import argparse


def parse(flag_dict):
    parser = argparse.ArgumentParser(
        description=flag_dict["description"],
        allow_abbrev=False,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {flag_dict['version']}",
    )
    parser.add_argument(
        "-C",
        "--check",
        action="store_true",
        help="dry run mode",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="suppress non-error messages",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="verbose mode (-vv for more),",
    )

    def add_flag(flag, is_required=True):
        try:
            if flag["type"] == "bool":
                parser.add_argument(
                    f"--{flag['name']}",
                    action="store_true",
                    required=is_required,
                    help=flag["help"],
                )
        except KeyError:
            try:
                parser.add_argument(
                    f"--{flag['name']}",
                    choices=flag["choices"],
                    required=is_required,
                    help=flag["help"],
                )
            except KeyError:
                parser.add_argument(
                    f"--{flag['name']}",
                    required=is_required,
                    help=flag["help"],
                )

    for flag in flag_dict["flags"]:
        flag = list(flag.values())[0]
        if flag["required"]:
            add_flag(flag)
        else:
            add_flag(flag, False)

    return parser
