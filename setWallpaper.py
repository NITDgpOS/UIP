from gi.repository import Gio

def change_background(self, filename):
    gsettings = Gio.Settings.new('org.gnome.desktop.background')
    gsettings.set_string('picture-uri', "file://" + filename)
    gsettings.apply()
