#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-18 10:38:40

import argparse

# >>> parser.add_argument('--foo')
# _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)

# class argparse.ArgumentParser(description=None)

# ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

# ArgumentParser.add_argument(name or flags...[, action][, nargs][, type][, choices][, required][, help][, metavar])

# ArgumentParser.add_argument_group(title=None)

# ArgumentParser.add_mutually_exclusive_group(required=False)


parser = argparse.ArgumentParser()

parser.add_argument()

parser.exit(status=rc)


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
