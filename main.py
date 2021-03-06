#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-16 03:36:22
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-23 09:50:58


from edison import command, flag, path, yaml_conf


def get_extra_vars(args_dict):
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


def playbook_cmd(args, extra_vars):
    if args.verbose >= 2:
        if args.check:
            cmd = f'ansible-playbook -vv -C -e "{extra_vars}" site.yml'
        else:
            cmd = f'ansible-playbook -vv -e "{extra_vars}" site.yml'
    elif args.verbose >= 1:
        if args.check:
            cmd = f'ansible-playbook -v -C -e "{extra_vars}" site.yml'
        else:
            cmd = f'ansible-playbook -v -e "{extra_vars}" site.yml'
    else:
        if args.check:
            cmd = f'ansible-playbook -C -e "{extra_vars}" site.yml'
        else:
            cmd = f'ansible-playbook -e "{extra_vars}" site.yml'
    return cmd


def playbook_run(args, cmd, playbook_dir, parser):
    if args.quiet:
        rc = command.run(cmd, playbook_dir, quiet=True)
        parser.exit(status=rc)
    else:
        rc = command.run(cmd, playbook_dir)
        parser.exit(status=rc)


def main():
    playbook_dir = path.name(__file__, "playbook")
    flag_yaml = path.name(__file__, "flag.yml")
    flag_dict = yaml_conf.get_data(flag_yaml)

    parser = flag.parse(flag_dict)
    args = parser.parse_args()
    args_dict = vars(args)

    extra_vars = get_extra_vars(args_dict)

    ansible_cmd = playbook_cmd(args, extra_vars)

    playbook_run(args, ansible_cmd, playbook_dir, parser)


if __name__ == "__main__":
    main()
