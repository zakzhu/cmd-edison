#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-18 16:05:48

import argparse

# >>> parser.add_argument('--foo')
# _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)

# class argparse.ArgumentParser(description=None)

# ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

# ArgumentParser.add_argument(
# name or flags...
# [, type]
# [, choices]
# [, required]
# [, help]
# [, metavar])

# parser.exit(status=rc)


def parser(required_flag, optional_flag, help_msg, description, ver):
    parser = argparse.ArgumentParser(description=description)
    vers = '%(progs)s {}'.format(ver)
    parser.add_argument('--version', action='version', version='%s' % vers)
    parser.add_argument(
        "--%s" % ,
        help=help_msg,
    )


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
