# -*- python -*-

import Params
Params.g_autoconfig = True

VERSION = '2.23.0'
APPNAME = 'gnome-python-desktop'
srcdir = '.'
blddir = 'build'

import misc
import os
import shutil
import glob
import sys
import types


def dist_hook():
    for docs_module in ['gnomeprint', 'gnomeprintui', 'gtksourceview']:
        for html_file in glob.glob(os.path.join('..', 'build', 'default', 'docs', docs_module, 'html', '*')):
            shutil.copy2(html_file, os.path.join('docs', docs_module, 'html'))
    ## Copy WAF to the distdir
    assert os.path.basename(sys.argv[0]) == 'waf'
    shutil.copy(sys.argv[0], '.')

def set_options(opt):
    opt.tool_options('compiler_cc')
    opt.tool_options('gnome')
    opt.sub_options('metacity')


def configure(conf):
    conf.check_tool('misc')
    conf.check_tool('compiler_cc')
    conf.check_tool('gnome')
    conf.check_tool('python')
    conf.check_python_version((2,4))
    conf.check_python_headers()
    conf.find_program('xsltproc', var='XSLTPROC')
    conf.define('VERSION', VERSION)

    version = [int(s) for s in VERSION.split('.')]
    conf.define('GNOME_PYTHON_DESKTOP_MAJOR_VERSION', version[0])
    conf.define('GNOME_PYTHON_DESKTOP_MINOR_VERSION', version[1])
    conf.define('GNOME_PYTHON_DESKTOP_MICRO_VERSION', version[2])

    # Define pygtk required version, for runtime check
    pygtk_version = [2, 10, 3]
    conf.define('PYGTK_REQUIRED_MAJOR_VERSION', pygtk_version[0])
    conf.define('PYGTK_REQUIRED_MINOR_VERSION', pygtk_version[1])
    conf.define('PYGTK_REQUIRED_MICRO_VERSION', pygtk_version[2])

    values = conf.check_pkg('pygtk-2.0', destvar='PYGTK',
                            vnum='.'.join([str(x) for x in pygtk_version]),
                            pkgvars=['defsdir'], mandatory=True)
    conf.env['PYGTK_DEFSDIR'] = values['PYGTK_DEFSDIR']

    gnome_python_version = [2, 10, 0]
    values = conf.check_pkg('gnome-python-2.0', destvar='GNOME_PYTHON',
                            vnum='.'.join([str(x) for x in gnome_python_version]),
                            pkgvars=['defsdir', 'argtypesdir'], mandatory=True)
    conf.env['GNOME_PYTHON_DEFSDIR'] = values['GNOME_PYTHON_DEFSDIR']
    conf.env['GNOME_PYTHON_ARG_TYPES_DIR'] = values['GNOME_PYTHON_ARGTYPESDIR']

    conf.env.append_value('CCDEFINES', 'HAVE_CONFIG_H')
    
    conf.sub_config('gnomekeyring')
    conf.sub_config('gnomeapplet')
    conf.sub_config('gnomedesktop')
    conf.sub_config('gnomeprint')
    conf.sub_config('evolution')
    conf.sub_config('gtksourceview')
    conf.sub_config('gtop')
    conf.sub_config('mediaprofiles')
    conf.sub_config('metacity')
    conf.sub_config('nautilusburn')
    conf.sub_config('rsvg')
    conf.sub_config('totem')
    conf.sub_config('wnck')

    conf.write_config_header('config.h')


def build(bld):

    ## cater for WAF API change between 1.3 and 1.4
    waf_version = [int (s) for s in Params.g_version.split('.')]
    if waf_version >= [1,4]:
        def create_pyext(bld):
            return bld.create_obj('cc', 'shlib', 'pyext')
    else:
        def create_pyext(bld):
            return bld.create_obj('cc', 'plugin', 'pyext')
    bld.create_pyext = types.MethodType(create_pyext, bld)


    ## generate and install the .pc file
    obj = bld.create_obj('subst')
    obj.source = 'gnome-python-desktop-2.0.pc.in'
    obj.target = 'gnome-python-desktop-2.0.pc'
    obj.dict = {
        'VERSION': VERSION,
        'prefix': bld.env()['PREFIX'],
        'exec_prefix': bld.env()['PREFIX'],
        'libdir': bld.env()['LIBDIR'],
        'includedir': os.path.join(bld.env()['PREFIX'], 'include'),
        'datadir': bld.env()['DATADIR'],
        'datarootdir': bld.env()['DATADIR'],
        }
    obj.fun = misc.subst_func
    obj.inst_var = 'LIBDIR'
    obj.inst_dir = 'pkgconfig'

    ## subdirs
    bld.add_subdirs('gnomekeyring')
    bld.add_subdirs('gnomeapplet')
    bld.add_subdirs('gnomedesktop')
    bld.add_subdirs('gnomeprint')
    bld.add_subdirs('evolution')
    bld.add_subdirs('gtksourceview')
    bld.add_subdirs('gtop')
    bld.add_subdirs('mediaprofiles')
    bld.add_subdirs('metacity')
    bld.add_subdirs('nautilusburn')
    bld.add_subdirs('rsvg')
    bld.add_subdirs('totem')
    bld.add_subdirs('wnck')

    bld.add_subdirs('docs/gnomeprint')
    bld.add_subdirs('docs/gnomeprintui')
    bld.add_subdirs('docs/gtksourceview')

