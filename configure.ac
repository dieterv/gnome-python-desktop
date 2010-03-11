-*- mode: autoconf -*-
AC_PREREQ(2.52)

dnl the gnome-python version number
m4_define(gnome_python_desktop_major_version, 2)
m4_define(gnome_python_desktop_minor_version, 29)
m4_define(gnome_python_desktop_micro_version, 92)
m4_define(gnome_python_desktop_version, gnome_python_desktop_major_version.gnome_python_desktop_minor_version.gnome_python_desktop_micro_version)

dnl required versions of other packages
m4_define(pygtk_required_major_version, 2)
m4_define(pygtk_required_minor_version, 10)
m4_define(pygtk_required_micro_version, 3)
m4_define(pygtk_required_version, pygtk_required_major_version.pygtk_required_minor_version.pygtk_required_micro_version)
m4_define(glib_required_version,              2.6.0)
m4_define(gtk_required_version,               2.4.0)
m4_define(gnome_python_required_version,      2.10.0)
m4_define(libpanelapplet_required_version,    2.13.4)
m4_define(libgnomeprint_required_version,     2.2.0)
m4_define(libgnomeprintui_required_version,   2.2.0)
m4_define(gtksourceview_required_version,     1.1.90)
m4_define(wnck_required_version,              2.19.3)
m4_define(libgtop_required_version,           2.13.0)
m4_define(libnautilus_burn_required_version,  2.15.3)
m4_define(libbrasero_media_required_version,  2.29)
m4_define(mediaprofiles_required_version,     2.10.0)
m4_define(gconf_required_version,             2.10.0)
m4_define(metacity_required_version,          2.21.5)
m4_define(rsvg_required_version,              2.13.93)
m4_define(gnomekeyring_required_version,      0.5.0)
m4_define(gnomedesktop_required_version,      2.10.0)
m4_define(totem_required_version,             1.4.0)
m4_define(libecal_required_version,           1.4.0)
m4_define(libebook_required_version,          1.4.0)

AC_INIT(gnome-python-desktop, gnome_python_desktop_version,
        [http://bugzilla.gnome.org/enter_bug.cgi?product=gnome-python])
dnl AC_CONFIG_SRCDIR([gnome/uimodule.c])
AM_CONFIG_HEADER(config.h)

AM_INIT_AUTOMAKE

AC_DEFINE(GNOME_PYTHON_DESKTOP_MAJOR_VERSION, gnome_python_desktop_major_version,
                                            [Gnome-Python-Desktop major version])
AC_DEFINE(GNOME_PYTHON_DESKTOP_MINOR_VERSION, gnome_python_desktop_minor_version,
                                            [Gnome-Python-Desktop minor version])
AC_DEFINE(GNOME_PYTHON_DESKTOP_MICRO_VERSION, gnome_python_desktop_micro_version,
                                            [Gnome-Python-Desktop macro version])

dnl AC_ARG_BINDING(NAME, DEFAULT [, MODULENAME])
AC_DEFUN([AC_ARG_BINDING],
[AC_ARG_ENABLE([$1],
             AC_HELP_STRING([--ifelse([$2], [YES], dis, en)able-[$1]],
                            [build ifelse([$3], , [$1], [$3]) bindings (default is [$2])]),
             [if test "$enable_[$1]" = "yes"; then 
	     	build_[$1]=true
	      else
	      	build_[$1]=false
	      fi])
])

GNOME_COMMON_INIT

AC_DISABLE_STATIC
AC_PROG_LIBTOOL
dnl when using libtool 2.x create libtool early, because it's used in configure
m4_ifdef([LT_OUTPUT], [LT_OUTPUT])


dnl check for python
AM_PATH_PYTHON(2.3)
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers)])

dnl check for pygtk
PKG_CHECK_MODULES(PYGTK, pygtk-2.0 >= pygtk_required_version)
AC_SUBST(PYGTK_CFLAGS)
AC_PATH_PROG(PYGTK_CODEGEN, pygtk-codegen-2.0, no)
if test "x$PYGTK_CODEGEN" = xno; then
  AC_MSG_ERROR(could not find pygtk-codegen-2.0 script)
fi

AC_MSG_CHECKING([for conflicting pygtk versions])
pygtk_version=`$PKG_CONFIG --modversion pygtk-2.0`
case $pygtk_version in
     2.9.0|2.9.1)
        AC_MSG_RESULT([found $pygtk_version])
        AC_MSG_ERROR([invalid pygtk version found; please upgrade])
        ;;
     *)
        AC_MSG_RESULT([none])
        ;;
esac

AC_MSG_CHECKING(for pygobject defs)
PYGOBJECT_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygobject-2.0`
AC_SUBST(PYGOBJECT_DEFSDIR)
AC_MSG_RESULT($PYGOBJECT_DEFSDIR)

AC_MSG_CHECKING(for pygtk defs)
PYGTK_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygtk-2.0`
AC_SUBST(PYGTK_DEFSDIR)
AC_MSG_RESULT($PYGTK_DEFSDIR)

AC_MSG_CHECKING(for gnome-python defs)
GNOMEPYTHON_DEFSDIR=`$PKG_CONFIG --variable=defsdir gnome-python-2.0`
AC_SUBST(GNOMEPYTHON_DEFSDIR)
AC_MSG_RESULT($GNOMEPYTHON_DEFSDIR)

AC_MSG_CHECKING(for gnome-python argtypes dir)
GNOME_PYTHON_ARGTYPES_DIR=`$PKG_CONFIG --variable=argtypesdir gnome-python-2.0`
AC_SUBST(GNOME_PYTHON_ARGTYPES_DIR)
AC_MSG_RESULT($GNOME_PYTHON_ARGTYPES_DIR)

dnl get rid of the -export-dynamic stuff from the configure flags ...
export_dynamic=`(./libtool --config; echo eval echo \\$export_dynamic_flag_spec) | sh`

dnl check for glib
AM_PATH_GLIB_2_0(glib_required_version,,[AC_MSG_ERROR(maybe you want the gtk-gnome-1-2 branch?)],$extras_mods)
if test -n "$export_dynamic"; then
  GLIB_LIBS=`echo $GLIB_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl check to make sure we can find gtk
AM_PATH_GTK_2_0(gtk_required_version,,[AC_MSG_ERROR(maybe you want the gtk-gnome-1-2 branch?)],$extras_mods)
if test -n "$export_dynamic"; then
  GTK_LIBS=`echo $GTK_LIBS | sed -e "s/$export_dynamic//"`
fi


AC_ARG_ENABLE([gtk-doc],
             AC_HELP_STRING([--disable-gtk-doc],
                            [Disables gtk-doc documentation generation]),,
		[enable_gtk_doc="yes"])
AM_CONDITIONAL(BUILD_DOCS, [test "$enable_gtk_doc" = "yes"])

dnl default bindings to build:
default_bindings_on="applet gnomeprint gnomeprintui gtksourceview wnck totem_plparser gtop nautilusburn mediaprofiles rsvg gnomekeyring gnomedesktop bugbuddy metacity evolution evolution_ecal evince braseromedia braseroburn"
default_bindings_off="metacity"
default_bindings_all="$default_bindings_on $default_bindings_off"

AC_ARG_ENABLE([allbindings],
             AC_HELP_STRING([--disable-allbindings],
                            [Changes all the bindings default values to be either enabled or disabled, overridden by any explicit bindings on the commandline.]),
             [if test "$enable_allbindings" = "no"; then
	     	default_bindings_off="$default_bindings_all"
		default_bindings_on=""
	      else
	     	default_bindings_off=""
		default_bindings_on="$default_bindings_all"
	      fi])
for binding in $default_bindings_on; do
	eval build_$binding=true
done
for binding in $default_bindings_off; do
	eval build_$binding=false
done

dnl should we build the gnome.applet module?
AC_ARG_BINDING([applet],[YES],[gnome.applet])
if $build_applet; then
	PKG_CHECK_MODULES(LIBPANELAPPLET, [libpanelapplet-2.0 >= libpanelapplet_required_version
					   gnome-python-2.0 >= gnome_python_required_version
                                           libgnome-2.0 libgnomeui-2.0],
	  build_applet=true,
	  build_applet=false)
fi
AC_SUBST(LIBPANELAPPLET_CFLAGS)
AC_SUBST(LIBPANELAPPLET_LIBS)
AM_CONDITIONAL(BUILD_APPLET, $build_applet)
if test -n "$export_dynamic"; then
  LIBPANELAPPLET_LIBS=`echo $LIBPANELAPPLET_LIBS | sed -e "s/$export_dynamic//"`
fi




dnl should we build the gnomeprint module?
AC_ARG_BINDING([gnomeprint],[YES])
if $build_gnomeprint; then
	PKG_CHECK_MODULES(LIBGNOMEPRINT, [libgnomeprint-2.2 >= libgnomeprint_required_version
					 gnome-python-2.0 >= gnome_python_required_version],
	  build_gnomeprint=true,
	  build_gnomeprint=false)
fi
AC_SUBST(LIBGNOMEPRINT_CFLAGS)
AC_SUBST(LIBGNOMEPRINT_LIBS)
AM_CONDITIONAL(BUILD_GNOMEPRINT, $build_gnomeprint)
if test -n "$export_dynamic"; then
  LIBGNOMEPRINT_LIBS=`echo $LIBGNOMEPRINT_LIBS | sed -e "s/$export_dynamic//"`
fi

if [ $build_gnomeprint = true ]; then
   AC_MSG_CHECKING([for libgnomeprint 2.8 API])
   if $PKG_CONFIG --modversion "libgnomeprint-2.2 >= 2.7.2" > /dev/null 2>&1; then
      AC_MSG_RESULT([found])
      PYGNOMEPRINT_DEFS="-DHAVE_GNOMEPRINT28";
   else
      AC_MSG_RESULT([not found])
   fi
fi
AC_SUBST(PYGNOMEPRINT_DEFS)

dnl should we build the gnomeprint.ui module?
AC_ARG_BINDING([gnomeprintui],[YES],[gnomeprint.ui])
if $build_gnomeprintui; then
	PKG_CHECK_MODULES(LIBGNOMEPRINTUI, [libgnomeprintui-2.2 >= libgnomeprintui_required_version,
					   gnome-python-2.0 >= gnome_python_required_version],
	  build_gnomeprintui=true,
	  build_gnomeprintui=false)
fi
AC_SUBST(LIBGNOMEPRINTUI_CFLAGS)
AC_SUBST(LIBGNOMEPRINTUI_LIBS)
AM_CONDITIONAL(BUILD_GNOMEPRINTUI, $build_gnomeprintui)
if test -n "$export_dynamic"; then
  LIBGNOMEPRINTUI_LIBS=`echo $LIBGNOMEPRINTUI_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gtksourceview module?
AC_ARG_BINDING([gtksourceview],[YES])
if $build_gtksourceview; then
	PKG_CHECK_MODULES(GTKSOURCEVIEW, gtksourceview-1.0 >= gtksourceview_required_version,
	  build_gtksourceview=true,
	  build_gtksourceview=false)
fi
AM_CONDITIONAL(BUILD_GTKSOURCEVIEW, $build_gtksourceview)
if test -n "$export_dynamic"; then
  GTKSOURCEVIEW_LIBS=`echo $GTKSOURCEVIEW_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the wnck module
AC_ARG_BINDING([wnck],[YES])
if $build_wnck; then
	PKG_CHECK_MODULES(WNCK, libwnck-1.0 >= wnck_required_version,
	  build_wnck=true,
	  build_wnck=false)
fi
AM_CONDITIONAL(BUILD_WNCK, $build_wnck)
if test -n "$export_dynamic"; then
  WNCK_LIBS=`echo $WNCK_LIBS | sed -e "s/$export_dynamic//"`
fi



dnl should we build the totem.plparser module?
AC_ARG_BINDING([totem_plparser],[YES],[totem.plparser])
if $build_totem_plparser; then
	PKG_CHECK_MODULES(TOTEM_PLPARSER, [totem-plparser >= totem_required_version  pygtk-2.0 >= pygtk_required_version],
	  build_totem_plparser=true,
	  build_totem_plparser=false)
fi
AM_CONDITIONAL(BUILD_TOTEM_PLPARSER, $build_totem_plparser)
if test -n "$export_dynamic"; then
  TOTEM_PLPARSER_LIBS=`echo $TOTEM_PLPARSER_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gtop module?
AC_ARG_BINDING([gtop],[YES])
if $build_gtop; then
	PKG_CHECK_MODULES(GTOP, [libgtop-2.0 >= libgtop_required_version pygtk-2.0 >= pygtk_required_version],
	  build_gtop=true,
	  build_gtop=false)
fi
AM_CONDITIONAL(BUILD_GTOP, $build_gtop)
if test -n "$export_dynamic"; then
  GTOP_LIBS=`echo $GTOP_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the nautilusburn module?
AC_ARG_BINDING([nautilusburn],[YES])
if $build_nautilusburn; then
	PKG_CHECK_MODULES(NAUTILUSBURN, [libnautilus-burn >= libnautilus_burn_required_version
					 pygtk-2.0 >= pygtk_required_version],
	  build_nautilusburn=true,
	  build_nautilusburn=false)
fi
AM_CONDITIONAL(BUILD_NAUTILUSBURN, $build_nautilusburn)
if test -n "$export_dynamic"; then
  NAUTILUSBURN_LIBS=`echo $NAUTILUSBURN_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the braseromedia module?
AC_ARG_BINDING([braseromedia],[YES])
if $build_braseromedia; then
	PKG_CHECK_MODULES(BRASEROMEDIA, [libbrasero-media >= libbrasero_media_required_version
					 pygtk-2.0 >= pygtk_required_version],
	  build_braseromedia=true,
	  build_braseromedia=false)
fi
AM_CONDITIONAL(BUILD_BRASEROMEDIA, $build_braseromedia)
if test -n "$export_dynamic"; then
  BRASEROMEDIA_LIBS=`echo $BRASEROMEDIA_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the braseroburn module?
AC_ARG_BINDING([braseroburn],[YES])
if $build_braseroburn; then
	PKG_CHECK_MODULES(BRASEROBURN, [libbrasero-burn >= 2.29
					 pygtk-2.0 >= pygtk_required_version],
	  build_braseroburn=true,
	  build_braseroburn=false)
fi
AM_CONDITIONAL(BUILD_BRASEROBURN, $build_braseroburn)
if test -n "$export_dynamic"; then
  BRASEROBURN_LIBS=`echo $BRASEROBURN_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the mediaprofiles module?
AC_ARG_BINDING([mediaprofiles],[YES])
if $build_mediaprofiles; then
	PKG_CHECK_MODULES(MEDIAPROFILES, [gnome-media-profiles >= mediaprofiles_required_version
				   pygtk-2.0 >= pygtk_required_version
				   gconf-2.0 >= gconf_required_version],
	  build_mediaprofiles=true,
	  build_mediaprofiles=false)
fi
AM_CONDITIONAL(BUILD_MEDIAPROFILES, $build_mediaprofiles)
if test -n "$export_dynamic"; then
  MEDIAPROFILES_LIBS=`echo $MEDIAPROFILES_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the rsvg module?
AC_ARG_BINDING([rsvg],[YES])
if $build_rsvg; then
	PKG_CHECK_MODULES(RSVG, [librsvg-2.0 >= rsvg_required_version
				 pycairo
				 pygtk-2.0 >= pygtk_required_version],
	  build_rsvg=true,
	  build_rsvg=false)
fi
AM_CONDITIONAL(BUILD_RSVG, $build_rsvg)
if test -n "$export_dynamic"; then
  RSVG_LIBS=`echo $RSVG_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the metacity module
AC_ARG_BINDING([metacity],[NO])
if $build_metacity; then
    PKG_CHECK_MODULES(METACITY, libmetacity-private >= metacity_required_version,
      build_metacity=true,
      build_metacity=false)
    if test -n "$export_dynamic"; then
      METACITY_LIBS=`echo $METACITY_LIBS | sed -e "s/$export_dynamic//"`
    fi
fi
AM_CONDITIONAL(BUILD_METACITY, $build_metacity)

dnl should we build the gnomekeyring module
AC_ARG_BINDING([gnomekeyring],[YES])
if $build_gnomekeyring; then
	PKG_CHECK_MODULES(GNOMEKEYRING, [gnome-keyring-1 >= gnomekeyring_required_version
					 gobject-2.0 >= glib_required_version],
	  build_gnomekeyring=true,
	  build_gnomekeyring=false)
fi
AM_CONDITIONAL(BUILD_GNOMEKEYRING, $build_gnomekeyring)
if test -n "$export_dynamic"; then
  GNOMEKEYRING_LIBS=`echo $GNOMEKEYRING_LIBS | sed -e "s/$export_dynamic//"`
fi

if $PKG_CONFIG --exists "gnome-keyring-1 >= 2.20.1"; then
  AC_DEFINE(HAVE_KEYRING_2_20_1, 1, [defined if gnomekeyring 2.20.1 API is found])
fi

dnl should we build the gnomedesktop module
AC_ARG_BINDING([gnomedesktop],[YES])
if $build_gnomedesktop; then
	PKG_CHECK_MODULES(GNOMEDESKTOP, [gnome-desktop-2.0 >= gnomedesktop_required_version
					 pygobject-2.0],
	  build_gnomedesktop=true,
	  build_gnomedesktop=false)
fi
AM_CONDITIONAL(BUILD_GNOMEDESKTOP, $build_gnomedesktop)
if test -n "$export_dynamic"; then
  GNOMEDESKTOP_LIBS=`echo $GNOMEDESKTOP_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl Check for bug-buddy
AC_ARG_BINDING([bugbuddy],[YES])
if $build_bugbuddy; then
	AC_PATH_PROG(BUG_BUDDY, bug-buddy)
	if test "x$BUG_BUDDY" != "x"; then 
	  AC_MSG_CHECKING([whether bug-buddy >= 2.16])
	  if $BUG_BUDDY --version | $PYTHON -c ["import sys; sys.exit([int(s) for s in sys.stdin.read().split()[2].split('.')] < [2,16])"]; then
	    AC_MSG_RESULT([yes])
	    build_bugbuddy=true
	  else
	    AC_MSG_RESULT([no])
	    build_bugbuddy=false
	  fi
	fi
fi
AM_CONDITIONAL(BUILD_BUGBUDDY, $build_bugbuddy)

dnl should we build the evolution module
AC_ARG_BINDING([evolution],[YES])

dnl can also build without ecal support (desirable for maemo)
AC_ARG_BINDING([evolution_ecal],[YES],[Evolution ECal])

if $build_evolution; then
    PKG_CHECK_MODULES(EVOLUTION_EBOOK, [libebook-1.2 >= libebook_required_version
                                        pygobject-2.0
                                        gdk-pixbuf-2.0
                                        pango],
    build_evolution=true,
    build_evolution=false)
    if test -n "$export_dynamic"; then
        EVOLUTION_EBOOK_LIBS=`echo $EVOLUTION_EBOOK_LIBS | sed -e "s/$export_dynamic//"`
    fi
    
    if $build_evolution_ecal; then
        PKG_CHECK_MODULES(EVOLUTION_ECAL,  [libecal-1.2 >= libecal_required_version
                                            pygobject-2.0
                                            gdk-pixbuf-2.0
                                            pango],
        build_evolution_ecal=true,
        build_evolution_ecal=false)
        if test -n "$export_dynamic"; then
            EVOLUTION_ECAL_LIBS=`echo $EVOLUTION_ECAL_LIBS | sed -e "s/$export_dynamic//"`
        fi
    fi
else
    if $build_evolution_ecal; then
      AC_MSG_ERROR(You must enable the Evolution module as well if you want the Evolution Cal module)
    fi
fi
AM_CONDITIONAL(BUILD_EVOLUTION, $build_evolution)
AM_CONDITIONAL(BUILD_EVOLUTION_ECAL, $build_evolution_ecal)

dnl should we build the evince module
AC_ARG_BINDING([evince],[YES])
if $build_evince; then
    PKG_CHECK_MODULES(EVINCE, [evince-document-2.29 evince-view-2.29],
      build_evince=true,
      build_evince=false)
    if test -n "$export_dynamic"; then
      EVINCE_LIBS=`echo $EVINCE_LIBS | sed -e "s/$export_dynamic//"`
    fi
fi
AM_CONDITIONAL(BUILD_EVINCE, $build_evince)


dnl add required cflags ...
JH_ADD_CFLAG([-Wall])
JH_ADD_CFLAG([-std=c9x])
JH_ADD_CFLAG([-fno-strict-aliasing])

AC_CONFIG_FILES(
  Makefile
  gnomeapplet/Makefile
  gnomeprint/Makefile
  gtksourceview/Makefile
  wnck/Makefile
  totem/Makefile
  gtop/Makefile
  nautilusburn/Makefile
  braseromedia/Makefile
  braseroburn/Makefile
  mediaprofiles/Makefile
  metacity/Makefile
  rsvg/Makefile
  gnomekeyring/Makefile
  gnomedesktop/Makefile
  evolution/Makefile
  evince/Makefile
  gnome-python-desktop-2.0.pc
  tests/Makefile
  docs/Makefile
  docs/gtksourceview/Makefile
  docs/gnomeprint/Makefile
  docs/gnomeprintui/Makefile
)
AC_OUTPUT

echo
echo "The following modules will be built:"
echo
$build_applet            && $have_pyorbit && echo     gnomeapplet
$build_gnomeprint        && echo     gnomeprint
$build_gnomeprintui      && echo     gnomeprint.ui
$build_gtksourceview     && echo     gtksourceview
$build_wnck              && echo     wnck
$build_totem_plparser    && echo     totem.plparser
$build_gtop              && echo     gtop
$build_nautilusburn      && echo     nautilusburn
$build_braseromedia      && echo     braseromedia
$build_braseroburn       && echo     braseroburn
$build_mediaprofiles     && echo     mediaprofiles
$build_metacity          && echo     metacity
$build_rsvg              && echo     rsvg
$build_gnomekeyring      && echo     gnomekeyring
$build_gnomedesktop      && echo     gnomedesktop
$build_bugbuddy          && echo     bugbuddy
$build_evolution         && echo     evolution
$build_evolution_ecal    && echo     evolution ecal support
$build_evince            && echo     evince
echo

echo "The following modules will NOT be built:"
echo
$build_applet            && $have_pyorbit || echo     gnomeapplet
$build_gnomeprint        || echo     gnomeprint
$build_gnomeprintui      || echo     gnomeprint.ui
$build_gtksourceview     || echo     gtksourceview
$build_wnck              || echo     wnck
$build_totem_plparser    || echo     totem.plparser
$build_gtop              || echo     gtop
$build_nautilusburn      || echo     nautilusburn
$build_braseromedia      || echo     braseromedia
$build_braseroburn       || echo     braseroburn
$build_mediaprofiles     || echo     mediaprofiles
$build_metacity          || echo     metacity
$build_rsvg              || echo     rsvg
$build_gnomekeyring      || echo     gnomekeyring
$build_gnomedesktop      || echo     gnomedesktop
$build_bugbuddy          || echo     bugbuddy
$build_evolution         || echo     evolution
$build_evolution_ecal    || echo     evolution ecal support
$build_evince            || echo     evince


echo "*****************************************************************************"
echo "*** WARNING: You are using a deprecated build system (autotools)."
echo "***          You should be using WAF instead; see the file INSTALL.WAF."
echo "***          The autotools build system will be removed in a future version."
echo "*****************************************************************************"
