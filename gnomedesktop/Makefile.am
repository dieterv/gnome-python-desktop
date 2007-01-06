INCLUDES = $(PYTHON_INCLUDES)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = _gnomedesktop.defs

EXTRA_DIST = $(defs_DATA)

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0


_gnomedesktopdir = $(pkgpyexecdir)/gnomedesktop
_gnomedesktop_LTLIBRARIES = _gnomedesktop.la
_gnomedesktop_la_LDFLAGS = -module -avoid-version -export-symbols-regex init_gnomedesktop
_gnomedesktop_la_LIBADD = $(GNOMEDESKTOP_LIBS)
_gnomedesktop_la_CFLAGS = $(GNOMEDESKTOP_CFLAGS)
_gnomedesktop_la_SOURCES = \
	_gnomedesktopmodule.c 

nodist__gnomedesktop_la_SOURCES = _gnomedesktop.c

_gnomedesktop_PYTHON = \
	__init__.py

CLEANFILES = _gnomedesktop.c
EXTRA_DIST += _gnomedesktop.override

_gnomedesktop.c: _gnomedesktop.defs _gnomedesktop.override
.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --py_ssize_t-clean \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c
