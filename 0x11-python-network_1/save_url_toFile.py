#!/usr/bin/env python3
import shutil
import urllib.request

custom_file_path = './createdFile.html'
url = 'https://portfolio-delta-one-32.vercel.app/'
with urllib.request.urlopen(url) as response:
    with open (custom_file_path, 'wb') as tmp_file:
        shutil.copyfileobj(response, tmp_file)

print('content saved at : {}'.format(custom_file_path))
