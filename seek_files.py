from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_entries = scandir('my_directory/')
    for entry in dir_entries:
    if entry.is_file():
	info = entry.stat()
	print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
