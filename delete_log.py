# coding : utf-8

import os
import sys
import psutil
import getpass
import shutil
import random

def delete_log(foldername):
    file_list = os.listdir(foldername)
    for f in file_list:
        fullname = os.path.join(foldername, f)
        if os.path.isfile(fullname):
            if fullname.endswith('log'):
                os.remove(fullname)
                if not os.path.exists(fullname):
                    print("Файл", f,"удален")

dirname = 'D:/flnt-test'
delete_log(dirname)