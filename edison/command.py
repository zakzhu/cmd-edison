#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Zak Zhu
# @Date:   2020-11-13 15:18:28
# @Last Modified by:   Zak Zhu
# @Last Modified time: 2020-11-23 10:41:04

import shlex
import subprocess


def run(cmd, workdir, quiet=False):
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
    rc_msg = f"RETURN CODE: {rc}"
    out_msg = f"\n>> {cmd}\n" f"{command.stdout}\n" f"{rc_msg}\n"

    if quiet:
        if rc != 0:
            print(out_msg)
    else:
        print(out_msg)
    return rc


def main():
    cmd = "ansible-playbook test.yml"
    path = "/tmp"
    # run(cmd, path, quiet=True)
    run(cmd, path, quiet=False)


if __name__ == "__main__":
    main()
