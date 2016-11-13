import sys

def change_background(self, filename):
    if sys.platform.startswith('win32'):
        change_windows_background(filename)

    elif sys.platform.startswith('linux'):
        change_linux_background(filename)

def change_linux_background(self, filename):
    from gi.repository import Gio

    gsettings = Gio.Settings.new('org.gnome.desktop.background')
    gsettings.set_string('picture-uri', "file://" + filename)
    gsettings.apply()

def change_windows_background(self, filename):
    import ctypes

    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 
                                               0, 
                                               filename, 3)
    