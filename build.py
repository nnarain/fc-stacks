#/usr/bin/env python3

import os
import shlex
import pathlib
import subprocess

DOCKER = 'docker'
KIBOT_IMAGE = 'setsoft/kicad_auto:ki8'

PRJ_ROOT = '/project'
BUILD_DIR = os.path.join(PRJ_ROOT, 'build')

def build_project(project_name):
    cur_dir = os.getcwd()
    try:
        kibot_cmd = f'kibot -c {PRJ_ROOT}/{project_name}/{project_name}.kibot.yaml -e {PRJ_ROOT}/{project_name}/{project_name}.kicad_sch -b {PRJ_ROOT}/{project_name}/{project_name}.kicad_pcb -d {BUILD_DIR}/{project_name}'
        shell_cmd = shlex.split(f'docker run --rm -it -v {cur_dir}:{PRJ_ROOT} {KIBOT_IMAGE} {kibot_cmd}', posix=False)

        print(f'Running {shell_cmd}')
        subprocess.run(shell_cmd)
    except Exception as e:
        print(f'{e}')

if __name__ == '__main__':
    build_project('blestack02')
