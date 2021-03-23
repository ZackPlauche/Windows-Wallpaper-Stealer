import platform
import shutil
from typing import Generator
from pathlib import Path


USER_PATH = list(Path(__file__).resolve().parents)[-3]

ASSETS_PATH = USER_PATH / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

DESKTOP = USER_PATH / 'desktop'


class WindowsWallpaperStealer:

    def __init__(self, destination_dir=DESKTOP / 'Windows Wallpapers'):
        check_if_windows()
        self.destination_dir = destination_dir
    
    def run(self):
        self.make_destination_dir()
        self.steal_wallpapers()

    def make_destination_dir(self):
        self.destination_dir.mkdir(exist_ok=True, parents=True)

    def steal_wallpapers(self):
        windows_wallpaper_assets = get_image_assets()
        copy_and_transform_image_assets(windows_wallpaper_assets, self.destination_dir)


def check_if_windows():
    if platform.system() != 'Windows':
        raise SystemError('This app only works on Windows')


def copy_and_transform_image_assets(image_assets, destination_dir):
    """Copies each image_asset file to a new directory and renames them
    chronologically with a .jpg suffix to transform them into images."""
    for i, image_asset in enumerate(image_assets, 1):
        new_image_name = f'{i}.jpg'
        new_image_path = destination_dir / new_image_name
        shutil.copy(image_asset, new_image_path)


def get_image_assets():
    raw_assets = get_raw_assets()
    image_assets = filter_assets_for_images(raw_assets)
    return image_assets


def get_raw_assets() -> Generator[Path, None, None]:
    return ASSETS_PATH.iterdir()


def filter_assets_for_images(assets) -> list:
    image_assets = [asset for asset in assets if check_if_asset_is_image(asset)]
    return image_assets


def check_if_asset_is_image(asset) -> bool:
    """Checks if asset file is greater than 20000 bytes, because this typically 
    means that the file is an image"""
    return get_file_size(asset) >= 20000


def get_file_size(file):
    file_size = file.lstat().st_size
    return file_size


if __name__ == '__main__':
    WindowsWallpaperStealer().run()
