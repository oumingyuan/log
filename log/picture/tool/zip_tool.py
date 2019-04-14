# -*- coding: utf-8 -*-


import os
import time
import zipfile

'''
    将文件夹下的文件保存到zip文件中。
    :param filePath: 待备份文件
    :param savePath: 备份路径
    :param note: 备份文件说明
    :return:
    '''


def create_zip(file_path, save_path):
    today = time.strftime('%Y%m%d')
    file_list = []
    if not os.path.exists(today):
        # os.mkdir(today)
        print('mkdir successful')

    target = save_path + '.zip'

    new_zip = zipfile.ZipFile(target, 'w')
    for dir_path, dir_names, file_names in os.walk(file_path):
        for file_name in file_names:
            file_list.append(os.path.join(dir_path, file_name))
    for tar in file_list:
        new_zip.write(tar, tar[len(file_path):])  # tar为写入的文件，tar[len(filePath)]为保存的文件名
    new_zip.close()
    f = open(file=target, mode='rb')

    return f.read()
