INCLUDES = $(PYTHON_INCLUDES)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = nautilus_burn.defs
EXTRA_DIST = $(defs_DATA)

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# nautilusburn binding
pkgpyexec_LTLIBRARIES = nautilusburn.la
nautilusburn_la_CFLAGS = $(NAUTILUSBURN_CFLAGS)
nautilusburn_la_LDFLAGS = -module -avoid-version -export-symbols-regex initnautilusburn
nautilusburn_la_LIBADD = $(NAUTILUSBURN_LIBS)
nautilusburn_la_SOURCES = nb_module.c		\
	nb_track.c nb_track.h

nodist_nautilusburn_la_SOURCES = nautilus_burn.c
CLEANFILES = nautilus_burn.c
EXTRA_DIST += nautilus_burn.override  
nautilus_burn.c: nautilus_burn.defs nautilus_burn.override

.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --py_ssize_t-clean \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --prefix $* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

EXTRA_DIST += wscript

