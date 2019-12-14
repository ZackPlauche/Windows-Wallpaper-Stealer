# Windows Wallpaper Stealer
## TL:DR Description
Download this and run it to have the epic Windows Wallpapers found on your Windows computer's lockscreen in a folder on your Desktop.
## Introduction
\****App and description is intended for Windows users only****

You know those epic wallpapers you see on your Windows computer's lock screen, but have no idea where they're stored on your computer?

Well, those files are hidden in a directory (folder) that's not super obvious to find or access.

Specifically: `C:\Users\username\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets`

The issue is that they're not saved as .png, .jpg, or any filetype useful for konwing that they're photos, and their names are just a huge mix of random letters and numbers, making them hard to find.

Here's an example name I just pulled from my own assets folder:
> 2cad6ab7697cb65703b03d91bec75d97376d32ba16c27beadf4ecd2e83d31dc3

Not very pretty is it?
 
## This is a straight-forward app
I built this simple program to automate the process of doing the following:

1. Create a new directory (named "Windows Wallpapers") in the desktop folder to store the wallpapers in.
2. Copy the hidden image assets (of an unreadable file type) to another folder if their file size is more than 20000 bits.
3. Add .jpg to the end of each asset file to convert it into a JPEG image format.
4. Rename the newly converted images in numerical order (because their original names are long and not useful).

It also adds two folders (Desktop & Mobile) in the Windows Wallpapers folder to store the images you like.  

### Checklist Progress
- [x] 1. Create a new directory (named "Windows Wallpapers") in the desktop folder to store the wallpapers in.
- [x] 2. Copy the hidden image assets (of an unreadable file type) to another folder if their file size is more than 20000 bits.
- [x] 3. Add .jpg to the end of each asset file to convert it into a JPEG image format.
- [x] 4. Rename the newly converted images in numerical order (because their original names are long and not useful).
