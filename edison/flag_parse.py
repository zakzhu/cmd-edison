#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 11:01:19
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-18 19:10:33

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
    parser.add_argument('--quiet', action='store_true', help='')
    def add_flag(is_required=True):
        try:
            if flags['type'] == 'bool':
                parser.add_argument(
                    '--%s' % flag['name'],
                    type=bool,
                    choices=[True, False],
                    required=is_required,
                    help=flag['help']
                )
        except KeyError:
            try:
                parser.add_argument(
                    '--%s' % flag['name'],
                    choices=flag['choices'],
                    required=is_required,
                    help=flag['help']
                )
            except KeyError:
                parser.add_argument(
                    '--%s' % flag['name'],
                    required=is_required,
                    help=flag['help']
                )        


    for flag in flag_dict['flags']:
        if flag.required:
            try:
                if flags['type'] == 'bool':
                    parser.add_argument(
                        '--%s' % flag['name'],
                        type=bool,
                        choices=[True, False],
                        required=True,
                        help=flag['help']
                    )
            except KeyError:
                try:
                    parser.add_argument(
                        '--%s' % flag['name'],
                        choices=flag['choices'],
                        required=True,
                        help=flag['help']
                    )
                except KeyError:
                    parser.add_argument(
                        '--%s' % flag['name'],
                        required=True,
                        help=flag['help']
                    )
        else:



def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
