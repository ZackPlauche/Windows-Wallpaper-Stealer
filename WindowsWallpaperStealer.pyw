#! python3

'''
You know those nice wallpapers you see your Windows Lockscreen,
but you're unable to find them in your folders?

If if you do find them, you feel you have to go through a manual process
to change the name of each one just to find which ones are actual images?

Well, my program automates that process and organizes it into a
nice, clean folder :)
'''

# -*- coding in: utf-8 -*-
import os
import shutil  # Shell Utilities module, allows for file transfer

# Get User's name (regardless of computer)
user = os.getcwd().split(os.path.sep)[2]

# Main Paths
desktop = f'C:\\Users\\{user}\\Desktop'
assets_path = f'C:\\Users\\{user}\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'

# New Paths
windows_wallpapers = f'{desktop}\\Windows Wallpapers'
desktop_wallpapers = f'{windows_wallpapers}\\Desktop Wallpapers'
mobile_wallpapers = f'{windows_wallpapers}\\Mobile Wallpapers'

# Directory Tree
directory_tree = {windows_wallpapers: [desktop_wallpapers, mobile_wallpapers]}

# Create New Directory Folders
for parent in directory_tree:
    os.makedirs(windows_wallpapers, exist_ok=True)
    for child in directory_tree[parent]:
        os.makedirs(child, exist_ok=True)

# Safely copy assets from Assets folder, remove any that aren't images, and transform them into .jpgs
assets = os.listdir(assets_path)
asset_counter = 1
for asset in assets:
    file_size = os.path.getsize(f'{assets_path}\\{asset}')
    if file_size < 10000:
        pass
    else:
        shutil.copy(f'{assets_path}\\{asset}', f'{windows_wallpapers}\\{asset_counter}.jpg')
        print(f'File {asset_counter}: {file_size}')
        asset_counter += 1
