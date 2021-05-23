import platform
import shutil
from pathlib import WindowsPath
from typing import Generator


ASSETS_PATH = WindowsPath.home() / 'AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'

DESKTOP = WindowsPath.home() / 'desktop'


def steal_windows_wallpapers(destination_dir: WindowsPath = DESKTOP / 'Windows Wallpapers'):
    check_if_windows()
    destination_dir.mkdir(exist_ok=True, parents=True)
    windows_wallpaper_assets = get_image_assets()
    copy_and_transform_image_assets(windows_wallpaper_assets, destination_dir)


def check_if_windows():
    if platform.system() != 'Windows':
        raise SystemError('This app only works on Windows.')


def copy_and_transform_image_assets(image_assets, destination_dir):
    """
    Copies each image_asset file to a new directory and renames them
    chronologically with a .jpg suffix to transform them into images.
    """

    for i, image_asset in enumerate(image_assets, 1):
        new_image_name = f'{i}.jpg'
        new_image_path = destination_dir / new_image_name
        shutil.copy(image_asset, new_image_path)


def get_image_assets():
    raw_assets = get_raw_assets()
    image_assets = filter_assets_for_images(raw_assets)
    return image_assets


def get_raw_assets() -> Generator[WindowsPath, None, None]:
    return ASSETS_PATH.iterdir()


def filter_assets_for_images(assets) -> list:
    return [asset for asset in assets if is_image(asset)]


def is_image(asset: WindowsPath) -> bool:
    # Asset files > 20000 bytes are typically images.
    return get_file_size(asset) >= 20000


def get_file_size(file: WindowsPath) -> int:
    file_size_in_bytes = file.lstat().st_size
    return file_size_in_bytes


if __name__ == '__main__':
    steal_windows_wallpapers()
