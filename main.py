#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 03:36:22
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-20 14:44:45


from edison import command, flag, path, yaml_conf

# parser.exit(status=rc)

workdir = path.dirname(__file__)
playbook_dir = path.name(workdir, "playbook")
flag_yaml = path.name(workdir, "flag.yml")
flag_dict = yaml_conf.get_data(flag_yaml)

parser = flag.parse(flag_dict)
args = parser.parse_args()
args_dict = vars(args)


def get_extra_vars():
    extra_vars = args_dict.copy()
    for i in ["check", "quiet", "verbose"]:
        extra_vars.pop(i)

    undefined_vars = []
    for i in extra_vars:
        if extra_vars[i] is None:
            undefined_vars.append(i)

    for i in undefined_vars:
        extra_vars.pop(i)
    return extra_vars


extra_vars = get_extra_vars()

if args.verbose >= 2:
    if args.check:
        cmd = 'ansible-playbook -vv -C -e "%s" site.yml' % extra_vars
    else:
        cmd = 'ansible-playbook -vv -e "%s" site.yml' % extra_vars
elif args.verbose >= 1:
    if args.check:
        cmd = 'ansible-playbook -v -C -e "%s" site.yml' % extra_vars
    else:
        cmd = 'ansible-playbook -v -e "%s" site.yml' % extra_vars
else:
    if args.check:
        cmd = 'ansible-playbook -C -e "%s" site.yml' % extra_vars
    else:
        cmd = 'ansible-playbook -e "%s" site.yml' % extra_vars


def main():
    pass


if __name__ == "__main__":
    main()
