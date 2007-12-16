CLEANFILES=
INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = print.defs printui.defs art.defs

EXTRA_DIST = $(defs_DATA) print-arg-types.py

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

common_ldflags = -module -avoid-version

pygnomedir = $(pkgpythondir)/gnomeprint
pygnome_PYTHON = __init__.py

pygnomeexecdir = $(pkgpyexecdir)/gnomeprint
pygnomeexec_LTLIBRARIES =

# libgnomeprint binding
pygnomeexec_LTLIBRARIES += _print.la
_print_la_CFLAGS = $(LIBGNOMEPRINT_CFLAGS) $(PYGNOMEPRINT_DEFS)
_print_la_LDFLAGS = $(common_ldflags) -export-symbols-regex init_print
_print_la_LIBADD = $(LIBGNOMEPRINT_LIBS)
_print_la_SOURCES = printmodule.c art-gtype.h art-gtype.c
nodist__print_la_SOURCES = print.c
CLEANFILES += print.c
EXTRA_DIST += print.override
print.c: print.defs print.override

# libgnomeprintui binding
if BUILD_GNOMEPRINTUI
pygnomeexec_LTLIBRARIES += ui.la
endif
ui_la_CFLAGS = $(LIBGNOMEPRINTUI_CFLAGS)
ui_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initui
ui_la_LIBADD = $(LIBGNOMEPRINTUI_LIBS)
ui_la_SOURCES = printuimodule.c
nodist_ui_la_SOURCES = printui.c
CLEANFILES += printui.c
EXTRA_DIST += printui.override  
printui.c: printui.defs printui.override


# generic rule
.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    $(PYGNOMEPRINT_DEFS) \
	    --load-types print-arg-types.py \
	    --register $(PYGTK_DEFSDIR)/pango-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register print.defs \
	    --register $(GNOMEPYTHON_DEFSDIR)/canvas.defs \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c


EXTRA_DIST += wscript

