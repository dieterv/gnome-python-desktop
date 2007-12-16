
SUBDIRS =  docs

if BUILD_GNOMEPRINT
  SUBDIRS += gnomeprint
endif

if BUILD_APPLET
  SUBDIRS += gnomeapplet
endif

if BUILD_GTKSOURCEVIEW
  SUBDIRS += gtksourceview
endif

if BUILD_WNCK
  SUBDIRS += wnck
endif

if BUILD_TOTEM_PLPARSER
  SUBDIRS += totem
endif

if BUILD_GTOP
  SUBDIRS += gtop
endif

if BUILD_NAUTILUSBURN
  SUBDIRS += nautilusburn
endif

if BUILD_MEDIAPROFILES
  SUBDIRS += mediaprofiles
endif

if BUILD_METACITY
  SUBDIRS += metacity
endif

if BUILD_RSVG
  SUBDIRS += rsvg
endif

if BUILD_GNOMEKEYRING
  SUBDIRS += gnomekeyring
endif

if BUILD_GNOMEDESKTOP
  SUBDIRS += gnomedesktop
endif

if BUILD_EVOLUTION
  SUBDIRS += evolution
endif

SUBDIRS +=  tests

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = gnome-python-desktop-2.0.pc

## Install the bugbuddy module
pkgpyexecdir = $(pyexecdir)/gtk-2.0
if BUILD_BUGBUDDY
  pkgpyexec_PYTHON = bugbuddy.py
endif


EXTRA_DIST = \
  MAINTAINERS \
  COPYING.GPL COPYING.LGPL \
  gnome-python-desktop-2.0.pc.in \
  ltihooks.py \
  examples/gtksourceview/test-widget.py \
  examples/applet/applet.py \
  examples/applet/GNOME_PythonAppletSample.server \
  examples/applet/README \
  examples/gnomeprint/test-print.py \
  examples/gnomeprint/example_01.py \
  examples/gnomeprint/example_02.py \
  examples/gnomeprint/example_03.py \
  examples/gnomeprint/example_04.py \
  examples/gnomeprint/example_05.py \
  examples/gnomeprint/example_06.py \
  examples/gnomeprint/example_08.py \
  examples/gnomeprint/example_09.py \
  examples/gnomeprint/example_10.glade \
  examples/gnomeprint/example_10.py \
  examples/gnomeprint/example_11.py \
  examples/gnomeprint/README \
  examples/gnomeprint/sample-image.png \
  examples/mediaprofiles/profiles.py \
  examples/nautilusburn/blank_disc.py \
  examples/nautilusburn/drive_selection.py \
  examples/nautilusburn/write_iso.py \
  examples/keyring.py \
  examples/keyring-async.py \
  examples/rsvg/rsvg-cairo.py \
  examples/wnck_example.py


dist-hook: dist-hook-local
	cp `which waf` $(distdir)

.PHONY : dist-hook-local
