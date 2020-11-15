#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-13 15:18:28
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-16 01:40:50

import shlex
import subprocess


def run(cmd, path, silent=False):
    args = shlex.split(cmd)
    command = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
        cwd=path,
        check=False,
        encoding="utf-8",
        universal_newlines=True,
    )
    if silent:
        if command.returncode != 0:
            print(command.stdout)
    else:
        print(command.stdout)
        print("rc:", command.returncode)


def test():
    cmd = "ansible-playbook test.yml"
    path = "/tmp"
    run(cmd, path, silent=True)


if __name__ == "__main__":
    test()
