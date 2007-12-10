INCLUDES = $(PYTHON_INCLUDES)

pkgpythondir = $(pyexecdir)/gtk-2.0/evolution
pkgpyexecdir = $(pyexecdir)/gtk-2.0/evolution

pkgpyexec_LTLIBRARIES = ebook.la

if WANT_ECAL
pkgpyexec_LTLIBRARIES += ecal.la
endif

pkgpyexec_DATA = __init__.py

ecal_la_LDFLAGS = -module -avoid-version -export-symbols-regex initecal
ecal_la_CFLAGS = $(INCLUDES) $(ECAL_CFLAGS)
ecal_la_LIBADD = $(ECAL_LIBS)
ecal_la_SOURCES = \
	ecalmodule.c \
	override_common.c \
	evo-ecal-environment.c \
	evo-calendar.c \
	override_common.h \
	evo-ecal-environment.h \
	evo-calendar.h

ebook_la_LDFLAGS = -module -avoid-version -export-symbols-regex initebook
ebook_la_CFLAGS = $(INCLUDES) $(EBOOK_CFLAGS)
ebook_la_LIBADD = $(EBOOK_LIBS)
ebook_la_SOURCES = \
	ebookmodule.c \
	override_common.c \
	evo-ebook-environment.c \
	evo-contact.c \
	evo-addressbook.c \
	ebook-enums.c \
	override_common.h \
	evo-ebook-environment.h \
	evo-contact.h \
	evo-addressbook.h \
	ebook-enums.h


nodist_ecal_la_SOURCES = ecal.c
nodist_ebook_la_SOURCES = ebook.c

defsdir = $(pkgdatadir)/defs
defs_DATA = ebook.defs

if WANT_ECAL
	defs_DATA += ecal.defs
endif


CLEANFILES = ebook.c ecal.c
EXTRA_DIST = \
	ebook.defs \
	ecal.defs \
	ebook.override \
	ecal.override \
	gen-defs.sh \
	__init__.py

ebook.c: ebook.defs ebook.override
ecal.c: ecal.defs ecal.override
.defs.c:
	(cd $(srcdir) \
	 && $(PYGTK_CODEGEN) \
	    --override $*.override \
	    --register $(PYGTK_DEFSDIR)/gtk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-types.defs \
	    --register $(PYGTK_DEFSDIR)/gdk-base-types.defs \
	    --prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

