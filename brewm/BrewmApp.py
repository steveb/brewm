#!/usr/bin/python
#
#	THIS FILE IS PART OF THE BREWM PROJECT AND LICENSED UNDER THE GPL. SEE
#	THE 'COPYING' FILE FOR DETAILS
#
#	Brewm's main class. It creates the majority of the main window GUI
#	and gets everything up and running.
#
#-------------------------------------------------------------------------------

import sys
import gtk
  
class BrewmApp:
    def on_window_destroy(self, widget, data=None):
        gtk.main_quit()
    
    def __init__(self):
        builder = gtk.Builder()
        builder.add_from_file("Brewm.glade") 
        
        self.window = builder.get_object("window")
        builder.connect_signals(self)
    
if __name__ == "__main__":
    app = BrewmApp()
    app.window.show()
    gtk.main()
