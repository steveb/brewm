#!/usr/bin/python
#
#	THIS FILE IS PART OF THE BREWM PROJECT AND LICENSED UNDER THE GPL. SEE
#	THE 'COPYING' FILE FOR DETAILS
#
#	Brewm's main class. It creates the majority of the main window GUI
#	and gets everything up and running.
#
#-------------------------------------------------------------------------------

import pygtk
pygtk.require("2.0")
import gtk.glade, gobject
import sys
import os, os.path
