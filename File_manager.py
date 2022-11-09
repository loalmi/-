#import shutil
import os

def path(f):
    a = open('settings.txt', 'r', encoding='utf-8')

def func_name(a):
    f = {'cr_dir':create_dir, 'd_dir':delete_dir,
         'm_dir':move_dir, 'cr_f':create_file,
         'wr_f': write_file, 'v_f':view_file,
         'd_f':delete_file, 'copy_f':copy_file,
         'm_f':move_file, 'rn_f': rename_file}
    if a.split(' ')[0] in f:
        f[a.split(' ')[0]](a.split(' ')[1:])
    else:
        return 'некорректно'


def create_dir(Name):
    if len(Name) == 1:
        name = Name[0]
    rasshireniya = ['.jpg','.png', '.bmp','.gif', '.tif',
                    'txt','doc', 'docx', 'csv', 'xlsx',
                    'xls', 'zip','.pdf'] #Взяла популярные расширения (можно перечислить все)
    a = open('settings.txt', 'r', encoding='utf-8')
    osnova = a.read() #путь к основной папки
    a.close()
    p = os.path.join(osnova, name) #путь к текущей папке
    if not os.path.exists(p) and not p.endswith(rasshireniya):
        os.mkdir(p)
        print(f'Папка {name} успешно создана.')
    elif os.path.exists(p):
        print(f'Папка {name} уже существует.')
    else:
        print('Некорректный ввод.')

def delete_dir(name):
    pass

def move_dir(name):
    pass

def create_file(name):
    pass

def write_file(name):
    t = input('Введите текст :')
    pass

def view_file(name):
    pass

def delete_file(name):
    pass

def copy_file(file1, name1, name2):
    pass

def move_file(file1, name1, name2):
    pass

def rename_file(file1, file2):
    pass

while 1:
    w = input()
    if func_name(w) == 'некорректно':
        print('Функция введена некорректно')
    else:
        func_name(w)
        print(func_name(w))

