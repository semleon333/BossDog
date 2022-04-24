from django.conf import settings
import os
import re


def media_namer(instance, filename):
	"""Создает уникальное название загружаемого файла"""
	try:
		new_file_header = re.sub('[^\wа-яА-Я]', '_', instance.name)
		new_file_name = f'{new_file_header}.{filename.split(".")[-1]}'
		counter = 0
		while True:
			if os.path.exists(f'{settings.MEDIA_ROOT}/{new_file_name}') is False:
				return new_file_name
			else:
				counter += 1
				new_file_name = f'copy{counter}_{new_file_name}'
	except Exception as ex:
		raise ex
