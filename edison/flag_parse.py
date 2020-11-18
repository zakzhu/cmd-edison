#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-18 17:55:15

import argparse

# class argparse.ArgumentParser(description=None)

# ArgumentParser.add_argument(
# name or flags...
# [, type]
# [, choices]
# [, required]
# [, help]

# parser.exit(status=rc)



def parser(flag_dict):
    parser = argparse.ArgumentParser(description=flag_dict['description'])
    vers = '%(progs)s {}'.format(flag_dict['version'])
    parser.add_argument('--version', action='version', version='%s' % vers)
    for flag in flag_dict['flags']:
        if flag.required:
            

        else:
    # add boolean type arguments
    parser.add_argument(
        "--%s" % ,
        help=help_msg,
    )
    # add string type arguments 


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
