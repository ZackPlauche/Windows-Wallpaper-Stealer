import platform
import shutil
from pathlib import Path

if platform.system() != 'Windows':
    raise SystemError('This app only works on Windows')

USER_PATH = list(Path(__file__).resolve().parents)[-3]
DESKTOP = USER_PATH / 'desktop'
ASSETS_PATH = USER_PATH / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
DESTINATION_DIR = DESKTOP / 'Windows Wallpapers'
DESTINATION_DIR.mkdir(exist_ok=True, parents=True)

image_assets = [asset for asset in ASSETS_PATH.iterdir() if asset.lstat().st_size >= 20000]
for asset in image_assets:
    asset_index = str(image_assets.index(asset) + 1)
    shutil.copy(asset, DESTINATION_DIR / f'{asset_index}.jpg')
