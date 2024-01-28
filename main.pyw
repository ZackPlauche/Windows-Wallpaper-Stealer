"""
Copy files from the Windows Spotlight assets folder, convert the full size ones 
to JPG, and open the folder.
"""
import os
import shutil
from pathlib import Path

from PIL import Image


if __name__ == '__main__':
    ASSETS_DIR_PATH = Path.home() / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

    TARGET_DIR = Path.home() / 'Pictures/Spotlight'
    TARGET_DIR.mkdir(exist_ok=True, parents=True)

    for file in ASSETS_DIR_PATH.iterdir():
        copy_file = TARGET_DIR / file.with_suffix('.jpg').name
        shutil.copy(file, copy_file)

        # Only copy files that are 1920x1080
        with Image.open(file) as img:
            if img.width != 1920:
                copy_file.unlink()
            else:
                print(f'Copied {copy_file.name}')


    # Open the folder in Windows Explorer
    os.startfile(TARGET_DIR)