INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs

defs_DATA = metacity.defs

EXTRA_DIST = $(defs_DATA)

common_ldflags = -module -avoid-version

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# metacity binding

if BUILD_METACITY
pkgpyexec_LTLIBRARIES = metacity.la
endif
metacity_la_CFLAGS = $(METACITY_CFLAGS)
metacity_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initmetacity
metacity_la_LIBADD = $(METACITY_LIBS)
metacity_la_SOURCES = metacitymodule.c
nodist_metacity_la_SOURCES = metacity.c
CLEANFILES = metacity.c
EXTRA_DIST += metacity.override  
metacity.c: metacity.defs metacity.override

.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
            --register $(PYGTK_DEFSDIR)/gtk-types.defs \
            --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --py_ssize_t-clean \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c
