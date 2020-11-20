#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-20 14:18:33

import argparse


def parse(flag_dict):
    parser = argparse.ArgumentParser(description=flag_dict["description"])
    vers = "%(progs)s {}".format(flag_dict["version"])
    parser.add_argument("--version", action="version", version="%s" % vers)
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

    for flag in flag_dict["flags"]:
        flag = list(flag.values())[0]
        if flag["required"]:
            add_flag(flag)
        else:
            add_flag(flag, False)

    return parser


def main():
    import yaml_conf

    file = "/root/Programs/python/v3/cmd-edison/flag.yml"
    flag_dict = yaml_conf.get_data(file)
    # print(flag_dict["flags"])
    # for flag in flag_dict["flags"]:
    #     print(list(flag.values())[0]["name"])
    #     # for i in v:
    #     # print(i)
    #     # print(flag.values()[0]["name"])
    parser = parse(flag_dict)
    parser.print_help()
    args = parser.parse_args()
    args_dict = vars(args)
    for i in ["check", "quiet", "verbose"]:
        args_dict.pop(i)

    print(args_dict)

    undefined_args = []
    for i in args_dict:
        # print(args_dict[i])
        if args_dict[i] is None:
            undefined_args.append(i)
    for i in undefined_args:
        args_dict.pop(i)
    print(args_dict)


if __name__ == "__main__":
    main()
