INCLUDES = $(PYTHON_INCLUDES) $(PYGTK_CFLAGS)

defsdir = $(datadir)/pygtk/2.0/defs

defs_DATA = gnomekeyring.defs

EXTRA_DIST = $(defs_DATA) gnomekeyring-argtypes.py

common_ldflags = -module -avoid-version

pkgpythondir = $(pyexecdir)/gtk-2.0
pkgpyexecdir = $(pyexecdir)/gtk-2.0

# gnomekeyring binding

if BUILD_GNOMEKEYRING
pkgpyexec_LTLIBRARIES = gnomekeyring.la
endif
gnomekeyring_la_CFLAGS = $(GNOMEKEYRING_CFLAGS)
gnomekeyring_la_LDFLAGS = $(common_ldflags) -export-symbols-regex initgnomekeyring
gnomekeyring_la_LIBADD = $(GNOMEKEYRING_LIBS)
gnomekeyring_la_SOURCES = gnomekeyringmodule.c
nodist_gnomekeyring_la_SOURCES = gnomekeyring.c
CLEANFILES = gnomekeyring.c
EXTRA_DIST += gnomekeyring.override  
gnomekeyring.c: gnomekeyring.defs gnomekeyring.override gnomekeyring-argtypes.py

.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --load-types gnomekeyring-argtypes.py \
	    --py_ssize_t-clean \
            --register $(PYGTK_DEFSDIR)/gtk-types.defs \
            --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --override $*.override \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

EXTRA_DIST += wscript
