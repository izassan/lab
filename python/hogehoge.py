import os

if os.name == 'nt':
    current_dir = os.getenv('USERPROFILE')
else:
    current_dir = os.getenv('HOME')

print(f'{current_dir}')
