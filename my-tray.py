#!/usr/bin/env python3

# simple-gtk-trayer
# @depends: gir1.2-appindicator3

import os
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("My Tray", "starred", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()

  command_one = gtk.MenuItem("My Notes")
  command_one.connect("activate", noteQuick)
  menu.append(command_one)

  command_2 = gtk.MenuItem("My Todo List")
  command_2.connect("activate", noteTodo)
  menu.append(command_2)

  exittray = gtk.MenuItem("Exit")
  exittray.connect("activate", quit)
  menu.append(exittray)

  menu.show_all()
  return menu

def noteQuick(_):
  # print(os.environ["NOTES_QUICK"])
  os.system("xterm -e vim $NOTES_QUICK")

def noteTodo(_):
  os.system("xterm -e vim $NOTES_TODO")

def quit(_):
  gtk.main_quit()

if __name__ == "__main__":
  main()
