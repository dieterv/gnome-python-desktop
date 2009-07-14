import sys
# load module beneath
sys.path.append ('..')

import gtk, gobject
import braseromedia

s = braseromedia.DriveSelection()

def foo ():
	global s;
	print s.get_active().get_display_name()


s.show()

b = gtk.VBox(False, 0)
b.show()

w = gtk.Window (gtk.WINDOW_TOPLEVEL)
w.add (b)
w.show()

b.add (s)
gobject.idle_add (foo)
gtk.main ()
