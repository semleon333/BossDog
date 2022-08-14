from django.conf import settings
import os
import re


def media_namer(instance, filename) -> str:
    """Создает уникальное название загружаемого файла"""
    filetuple = tuple(filename.split("."))
    try:
        new_file_header: str = re.sub('[^\wа-яА-Я]', '_', instance.name)
    except:
        new_file_header: str = re.sub('[^\wа-яА-Я]', '_', filetuple[0])+"empty"
    if len(filetuple) > 1: 
        new_file_name: str = f'{new_file_header}.{filetuple[-1]}'
    else:
        new_file_name: str = f'{new_file_header}'
    counter = 0
    while True:
        if os.path.exists(f'{settings.MEDIA_ROOT}/{new_file_name}') is False:
            return new_file_name
        else:
            counter += 1
            new_file_name = f'copy{counter}_{new_file_name}'

