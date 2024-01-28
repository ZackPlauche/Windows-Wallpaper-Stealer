import os
import shutil
from pathlib import Path


ASSETS_DIR_PATH = Path.home() / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

TARGET_DIR = Path.home() / 'Pictures/Spotlight'
TARGET_DIR.mkdir(exist_ok=True, parents=True)

for file in ASSETS_DIR_PATH.iterdir():
    shutil.copy(file, TARGET_DIR / file.with_suffix('.jpg').name)

# Open the folder in Windows Explorer
os.startfile(TARGET_DIR)