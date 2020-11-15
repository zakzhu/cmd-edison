#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-13 15:18:28
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-16 01:34:17

# SUBPROCESS MODULE USAGE:
# subprocess.run(
#     args, *, stdin=None, input=None, stdout=None,
#     stderr=None, shell=False, cwd=None,
#     timeout=None, check=False, encoding=None, errors=None,
#     env=None, universal_newlines=None)

# subprocess.Popen(
#     args, bufsize=-1, executable=None, stdin=None,
#     stdout=None, stderr=None, preexec_fn=None, close_fds=True,
#     shell=False, cwd=None, env=None, universal_newlines=None,
#     startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False,
#     pass_fds=(), *, encoding=None, errors=None, text=None)

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
