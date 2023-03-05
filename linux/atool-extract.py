#!/usr/bin/env python

from sys import argv
from subprocess import run
from pathlib import Path


def main():
    file, dir = get_path()
    if file.endswith(('.7z', '.zip', '.rar')):
        extraction_control(p7zip(file, dir))
    elif file.endswith(('.tar', '.tar.gz', '.tar.xz')):
        extraction_control(tar(file, dir))
    elif file.endswith('.zst'):
        extraction_control(zstd(file, dir))


def get_path():
    if len(argv) == 2 and Path(argv[1]).is_file():
        path_file = argv[1]
        path_dir = path_file[:path_file.rindex('/')]
    elif len(argv) > 2 and Path(argv[1]).is_file and Path(argv[2]).is_dir():
        path_file = argv[1]
        path_dir = argv[2]
    else:
        print('\n** Некорректные вводные параметры **\n')
        raise SystemExit
    return path_file, path_dir


def extraction_control(unpacker):
    print('Идет распаковка...')
    try:
        run(unpacker, shell=True, check=True)
    except:
        print('\n** Ошибка распаковки **\n')
    else:
        print('Распаковка выполнена успешно')


def p7zip(file, dir):
    return f'7z x {file} -o{dir} -y'


def tar(file, dir):
    return f'tar xf {file} -C {dir}'


def zstd(file, dir):
    name = file[file.rindex('/'):].replace('.zst', '')
    return f'unzstd -qf {file} -o {dir + name}'


if __name__ == '__main__':
    main()
