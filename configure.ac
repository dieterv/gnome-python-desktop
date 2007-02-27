-*- mode: autoconf -*-
AC_PREREQ(2.52)

dnl the gnome-python version number
m4_define(gnome_python_desktop_major_version, 2)
m4_define(gnome_python_desktop_minor_version, 17)
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
m4_define(wnck_required_version,              2.15.5)
m4_define(libgtop_required_version,           2.13.0)
m4_define(libnautilus_burn_required_version,  2.15.3)
m4_define(mediaprofiles_required_version,     2.10.0)
m4_define(gconf_required_version,             2.10.0)
m4_define(metacity_required_version,          2.17.5)
m4_define(rsvg_required_version,              2.13.93)
m4_define(gnomekeyring_required_version,      0.5.0)
m4_define(gnomedesktop_required_version,      2.10.0)
m4_define(totem_required_version,             1.4.0)


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

GNOME_COMMON_INIT

AC_DISABLE_STATIC
AC_PROG_LIBTOOL

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


dnl should we build the gnome.applet module?
build_applet=false
PKG_CHECK_MODULES(LIBPANELAPPLET, [libpanelapplet-2.0 >= libpanelapplet_required_version
                                   gnome-python-2.0 >= gnome_python_required_version],
  build_applet=true,
  build_applet=false)
AC_SUBST(LIBPANELAPPLET_CFLAGS)
AC_SUBST(LIBPANELAPPLET_LIBS)
AM_CONDITIONAL(BUILD_APPLET, $build_applet)
if test -n "$export_dynamic"; then
  LIBPANELAPPLET_LIBS=`echo $LIBPANELAPPLET_LIBS | sed -e "s/$export_dynamic//"`
fi




dnl should we build the gnomeprint module?
build_gnomeprint=false
PKG_CHECK_MODULES(LIBGNOMEPRINT, [libgnomeprint-2.2 >= libgnomeprint_required_version
                                 gnome-python-2.0 >= gnome_python_required_version],
  build_gnomeprint=true,
  build_gnomeprint=false)
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
build_gnomeprintui=false
PKG_CHECK_MODULES(LIBGNOMEPRINTUI, [libgnomeprintui-2.2 >= libgnomeprintui_required_version,
                                   gnome-python-2.0 >= gnome_python_required_version],
  build_gnomeprintui=true,
  build_gnomeprintui=false)
AC_SUBST(LIBGNOMEPRINTUI_CFLAGS)
AC_SUBST(LIBGNOMEPRINTUI_LIBS)
AM_CONDITIONAL(BUILD_GNOMEPRINTUI, $build_gnomeprintui)
if test -n "$export_dynamic"; then
  LIBGNOMEPRINTUI_LIBS=`echo $LIBGNOMEPRINTUI_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gtksourceview module?
build_gtksourceview=false
PKG_CHECK_MODULES(GTKSOURCEVIEW, gtksourceview-1.0 >= gtksourceview_required_version,
  build_gtksourceview=true,
  build_gtksourceview=false)
AM_CONDITIONAL(BUILD_GTKSOURCEVIEW, $build_gtksourceview)
if test -n "$export_dynamic"; then
  GTKSOURCEVIEW_LIBS=`echo $GTKSOURCEVIEW_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the wnck module
build_wnck=false
PKG_CHECK_MODULES(WNCK, libwnck-1.0 >= wnck_required_version,
  build_wnck=true,
  build_wnck=false)
AM_CONDITIONAL(BUILD_WNCK, $build_wnck)
if test -n "$export_dynamic"; then
  WNCK_LIBS=`echo $WNCK_LIBS | sed -e "s/$export_dynamic//"`
fi



dnl should we build the totem.plparser module?
build_totem_plparser=false
PKG_CHECK_MODULES(TOTEM_PLPARSER, [totem-plparser >= totem_required_version  pygtk-2.0 >= pygtk_required_version],
  build_totem_plparser=true,
  build_totem_plparser=false)
AM_CONDITIONAL(BUILD_TOTEM_PLPARSER, $build_totem_plparser)
if test -n "$export_dynamic"; then
  TOTEM_PLPARSER_LIBS=`echo $TOTEM_PLPARSER_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gtop module?
build_gtop=false
PKG_CHECK_MODULES(GTOP, [libgtop-2.0 >= libgtop_required_version pygtk-2.0 >= pygtk_required_version],
  build_gtop=true,
  build_gtop=false)
AM_CONDITIONAL(BUILD_GTOP, $build_gtop)
if test -n "$export_dynamic"; then
  GTOP_LIBS=`echo $GTOP_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the nautilusburn module?
build_nautilusburn=false
PKG_CHECK_MODULES(NAUTILUSBURN, [libnautilus-burn >= libnautilus_burn_required_version
                                 pygtk-2.0 >= pygtk_required_version],
  build_nautilusburn=true,
  build_nautilusburn=false)
AM_CONDITIONAL(BUILD_NAUTILUSBURN, $build_nautilusburn)
if test -n "$export_dynamic"; then
  NAUTILUSBURN_LIBS=`echo $NAUTILUSBURN_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the mediaprofiles module?
build_mediaprofiles=false
PKG_CHECK_MODULES(MEDIAPROFILES, [gnome-media-profiles >= mediaprofiles_required_version
                           pygtk-2.0 >= pygtk_required_version
                           gconf-2.0 >= gconf_required_version],
  build_mediaprofiles=true,
  build_mediaprofiles=false)
AM_CONDITIONAL(BUILD_MEDIAPROFILES, $build_mediaprofiles)
if test -n "$export_dynamic"; then
  MEDIAPROFILES_LIBS=`echo $MEDIAPROFILES_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the rsvg module?
build_rsvg=false
PKG_CHECK_MODULES(RSVG, [librsvg-2.0 >= rsvg_required_version
                         pycairo
                         pygtk-2.0 >= pygtk_required_version],
  build_rsvg=true,
  build_rsvg=false)
AM_CONDITIONAL(BUILD_RSVG, $build_rsvg)
if test -n "$export_dynamic"; then
  RSVG_LIBS=`echo $RSVG_LIBS | sed -e "s/$export_dynamic//"`
fi


dnl should we build the metacity module
AC_ARG_ENABLE([metacity],
             AC_HELP_STRING([--enable-metacity],
                            [build metacity bindings (default is NO)]),
             [build_metacity=true], [build_metacity=false])
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
build_gnomekeyring=false
PKG_CHECK_MODULES(GNOMEKEYRING, [gnome-keyring-1 >= gnomekeyring_required_version
                                 gobject-2.0 >= glib_required_version],
  build_gnomekeyring=true,
  build_gnomekeyring=false)
AM_CONDITIONAL(BUILD_GNOMEKEYRING, $build_gnomekeyring)
if test -n "$export_dynamic"; then
  GNOMEKEYRING_LIBS=`echo $GNOMEKEYRING_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl should we build the gnomekeyring module
build_gnomedesktop=false
PKG_CHECK_MODULES(GNOMEDESKTOP, [gnome-desktop-2.0 >= gnomedesktop_required_version
                                 pygobject-2.0],
  build_gnomedesktop=true,
  build_gnomedesktop=false)
AM_CONDITIONAL(BUILD_GNOMEDESKTOP, $build_gnomedesktop)
if test -n "$export_dynamic"; then
  GNOMEDESKTOP_LIBS=`echo $GNOMEDESKTOP_LIBS | sed -e "s/$export_dynamic//"`
fi

dnl Check for bug-buddy
build_bugbuddy=false
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
AM_CONDITIONAL(BUILD_BUGBUDDY, $build_bugbuddy)

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
  mediaprofiles/Makefile
  metacity/Makefile
  rsvg/Makefile
  gnomekeyring/Makefile
  gnomedesktop/Makefile
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
$build_mediaprofiles     && echo     mediaprofiles
$build_metacity          && echo     metacity
$build_rsvg              && echo     rsvg
$build_gnomekeyring      && echo     gnomekeyring
$build_gnomedesktop      && echo     gnomedesktop
$build_bugbuddy          && echo     bugbuddy
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
$build_mediaprofiles     || echo     mediaprofiles
$build_metacity          || echo     metacity
$build_rsvg              || echo     rsvg
$build_gnomekeyring      || echo     gnomekeyring
$build_gnomedesktop      || echo     gnomedesktop
$build_bugbuddy          || echo     bugbuddy
