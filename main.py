#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 03:36:22
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-20 09:58:27


from edison import command, flag, path, yaml_conf

# parser.exit(status=rc)

workdir = path.dirname(__file__)
playbook_dir = path.name(workdir, "playbook")
flag_yaml = path.name(workdir, "flag.yml")
flag_dict = yaml_conf.get_data(flag_yaml)
parser = flag.parse(flag_dict)
args = parser.parse_args()
if args.verbose >= 2:
    pass
elif args.verbose >= 1:
    pass
else:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
