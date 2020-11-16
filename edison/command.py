#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-13 15:18:28
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-16 10:30:59

import shlex
import subprocess


def run(cmd, workdir, silent=False):
    args = shlex.split(cmd)
    command = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        cwd=workdir,
        check=False,
        encoding="utf-8",
        universal_newlines=True,
    )
    rc = command.returncode
    rc_msg = "RETURN CODE: {}".format(rc)
    if silent:
        if rc != 0:
            print(rc_msg)
    else:
        print(command.stdout)
        print(rc_msg)
    return rc


def main():
    cmd = "ansible-playbook test.yml"
    path = "/tmp"
    # run(cmd, path, silent=True)
    run(cmd, path, silent=False)


if __name__ == "__main__":
    main()
