#!/usr/bin/env python
# coding=utf-8

u"""
指定したディレクトリ以下のバイナリーファイルにマニフェスト情報を埋め込む。

マニフェストファイルの作成方法は以下の通り。
mt.exe -out:py27.manifest -inputresource:C:\Python27\python.exe
"""

from __future__ import absolute_import, division, print_function

import argparse
import os
import subprocess
import sys


MT = u"C:\\Program Files (x86)\\Windows Kits\\8.1\\bin\\x64\\mt.exe"
MANIFEST = u"./py27.manifest"


def fix_manifest(dirpath, manifest, tool):
    for root, dirs, files in os.walk(dirpath):
        for name in files:
            if name.endswith((".pyd", ".dll")):
                resource_id = 2
            elif name.endswith(".exe"):
                resource_id = 1
            else:
                continue

            target_filename = (os.path.join(root, name))

            cmd = [
                MT,
                '-manifest',
                MANIFEST,
                '-outputresource:{0};{1}'.format(target_filename, resource_id),
            ]

            print(" ".join(cmd))

            _p = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
            )
            (stdout, stderr) = _p.communicate()


def main():
    help = u"search and fix binaries' manifest information."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument(
        '-i', '--input',
        dest='dirpath',
        type=str, default=".",
        metavar='DIR',
        help=u'input directory. (default: ./)'
    )
    parser.add_argument(
        '--manifest',
        dest='manifest',
        type=str, default=MANIFEST,
        metavar='FILENAME',
        help=u'manifest filename. (default: {0})'.format(MANIFEST)
    )
    parser.add_argument(
        '--tool',
        dest='tool',
        type=str, default=MT,
        metavar='FILENAME',
        help=u'mt tool filename. (default: {0})'.format(MT)
    )
    args = parser.parse_args()

    fix_manifest(args.dirpath, args.manifest, args.tool)

    return 0


if __name__ == '__main__':
    sys.exit(main())

# EOF
