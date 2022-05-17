from django.conf import settings
import os
import re


# TODO
#   Сделать утиль для форматирования полей моделей (исключая Many to many)

def media_namer(instance, filename) -> str:
	"""Создает уникальное название загружаемого файла"""
	try:
		try:
			new_file_header: str = re.sub('[^\wа-яА-Я]', '_', instance.name)
		except:
			# new_file_header: str = re.sub('[^\wа-яА-Я]', '_', filename.split(".")[0])
			new_file_header: str = re.sub('[^\wа-яА-Я]', '_', instance.fk.name)
		new_file_name: str = f'{new_file_header}.{filename.split(".")[-1]}'
		counter = 0
		while True:
			if os.path.exists(f'{settings.MEDIA_ROOT}/{new_file_name}') is False:
				return new_file_name
			else:
				counter += 1
				new_file_name = f'copy{counter}_{new_file_name}'
	except Exception as ex:
		raise ex
