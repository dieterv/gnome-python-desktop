INCLUDES = $(PYTHON_INCLUDES)

defsdir = $(datadir)/pygtk/2.0/defs
defs_DATA = brasero_burn.defs
EXTRA_DIST = $(defs_DATA)

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# braseroburn binding
pkgpyexec_LTLIBRARIES = braseroburn.la
braseroburn_la_CFLAGS = $(BRASEROBURN_CFLAGS)
braseroburn_la_LDFLAGS = -module -avoid-version -export-symbols-regex initbraseroburn
braseroburn_la_LIBADD = $(BRASEROBURN_LIBS)
braseroburn_la_SOURCES = brasero_burn_module.c

nodist_braseroburn_la_SOURCES = brasero_burn.c
CLEANFILES = brasero_burn.c
EXTRA_DIST += brasero_burn.override  
brasero_burn.c: brasero_burn.defs brasero_burn.override

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

