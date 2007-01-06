INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

CLEANFILES =

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = applet.defs

EXTRA_DIST = $(defs_DATA)

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

pygnomedir = $(pkgpythondir)/gnome
pygnomeexecdir = $(pkgpyexecdir)/gnome

pygnome_PYTHON = applet.py # compat dummy module


common_ldflags = -module -avoid-version

pkgpyexec_LTLIBRARIES = gnomeapplet.la
gnomeapplet_la_CFLAGS = $(LIBPANELAPPLET_CFLAGS)
gnomeapplet_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initgnomeapplet
gnomeapplet_la_LIBADD = $(LIBPANELAPPLET_LIBS)
gnomeapplet_la_SOURCES = appletmodule.c
nodist_gnomeapplet_la_SOURCES = applet.c
CLEANFILES += applet.c
EXTRA_DIST += applet.override
applet.c: applet.defs applet.override


.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --load-types $(GNOME_PYTHON_ARGTYPES_DIR)/bonobo-arg-types.py \
	    --py_ssize_t-clean \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(GNOMEPYTHON_DEFSDIR)/bonobo-types.defs \
	    --register $(GNOMEPYTHON_DEFSDIR)/bonoboui-types.defs \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

install-exec-hook: # Remove old deprecated modules
	-$(LIBTOOL) --mode=uninstall rm -f $(pygnomeexecdir)/applet.la
