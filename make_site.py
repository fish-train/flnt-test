# coding : utf-8

import os
import subprocess

# Удаление лог-файлов
def delete_log(foldername):
    file_list = os.listdir(foldername)										# Получить список файлов в папке
    for f in file_list:
        fullname = os.path.join(foldername, f)								# Получить путь к файлам
        if os.path.isfile(fullname):										# Проверить файл или нет
            if fullname.endswith('log'):									# Если файл заканчивается на 'log':
                os.remove(fullname)											# Удалить файл
                if not os.path.exists(fullname):							# Если файл не существует:
                    print("Файл", f,"удален")								# Показать имя удаленного файла

# Сборка сайта
def make_site():
	cmd = "foliant make site & cd flnt-test.mkdocs & python -m http.server"		# Собрать сайт , перейти в папку сайта, запустить веб-сервер
	subprocess.Popen(cmd, shell = True)									    # Выполнить команду CMD

make_site()																	# Собрать сайт

dirname = 'D:/flnt-test'													# Указать рабочую папку
delete_log(dirname)															# Удалить лог-файл предыдущей сборки

# Попробовать:
# Проверять, запущен ли веб-сервер. Если да - перезапускать.