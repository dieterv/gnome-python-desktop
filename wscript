# -*- python -*-

VERSION = '2.32.1'
APPNAME = 'gnome-python-desktop'
srcdir = '.'
blddir = 'build'

import Options

import Configure
Configure.autoconfig = True

import ccroot
ccroot.USE_TOP_LEVEL = True

import Task
Task.file_deps = Task.extract_deps

import Logs
import Build
import Utils

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
    shutil.copy(os.path.join('..', sys.argv[0]), '.')

    subprocess.Popen([os.path.join(srcdir, "generate-ChangeLog")],  shell=True).wait()
    try:
        os.chmod(os.path.join(srcdir, "ChangeLog"), 0644)
    except OSError:
        pass
    shutil.copy(os.path.join(srcdir, "ChangeLog"), '.')


def set_options(opt):
    opt.tool_options('compiler_cc')
    opt.tool_options('gnome')
    opt.tool_options('gnu_dirs')
    opt.tool_options('cflags')

    opt.sub_options('metacity')

    opt.add_option('--enable-modules',
                   help=('Enable only the specified modules.'),
                   type="string", default='all', metavar="MODULES_LIST (comma separated)",
                   dest='enable_modules')

def _bug_buddy_check(conf):
    conf.env.append_value('MODULES_AVAILABLE', 'bugbuddy')
    if conf.find_program('bug-buddy', var='BUG_BUDDY'):
        ver_string = Utils.cmd_output("%s --version" % (conf.env['BUG_BUDDY'],))
        ver = ver_string.split()[-1]
        ver = [int(x) for x in ver.split('.')]
        if ver >= [2,16]:
            conf.env.append_value('MODULES_TO_BUILD', 'bugbuddy')

def configure(conf):
    conf.check_tool('misc')
    conf.check_tool('compiler_cc')
    conf.check_tool('gnome')
    conf.check_tool('gnu_dirs')
    conf.check_tool('python')
    conf.check_tool('command')
    conf.check_tool('pkgconfig')
    conf.check_tool('cflags')
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

    conf.pkg_check_modules('PYGTK', 'pygtk-2.0 >= %s' % ('.'.join([str(x) for x in pygtk_version]),))
    conf.env['PYGTK_DEFSDIR'] = conf.pkg_check_module_variable('pygtk-2.0', 'defsdir')

    gnome_python_version = [2, 10, 0]
    values = conf.pkg_check_modules('GNOME_PYTHON',
                                    'gnome-python-2.0 >= %s' % ('.'.join([str(x) for x in gnome_python_version]),))
    conf.env['GNOME_PYTHON_DEFSDIR'] = conf.pkg_check_module_variable('gnome-python-2.0', 'defsdir')
    conf.env['GNOME_PYTHON_ARG_TYPES_DIR'] = conf.pkg_check_module_variable('gnome-python-2.0', 'argtypesdir')

    if not conf.find_program('pygobject-codegen-2.0', var='CODEGEN'):
        if not conf.find_program('pygtk-codegen-2.0', var='CODEGEN'):
            Logs.error("Could not find pygobject/pygtk codegen")

    conf.env.append_value('CCDEFINES', 'HAVE_CONFIG_H')

    conf.env['ENABLE_MODULES'] = Options.options.enable_modules.split(',')
    
    conf.sub_config('gnomekeyring')
    conf.sub_config('gnomeapplet')
    conf.sub_config('gnomedesktop')
    conf.sub_config('gnomeprint')
    conf.sub_config('evince')
    conf.sub_config('evolution')
    conf.sub_config('gtksourceview')
    conf.sub_config('gtop')
    conf.sub_config('mediaprofiles')
    conf.sub_config('metacity')
    conf.sub_config('nautilusburn')
    conf.sub_config('braseromedia')
    conf.sub_config('braseroburn')
    conf.sub_config('rsvg')
    conf.sub_config('totem')
    conf.sub_config('wnck')

    _bug_buddy_check(conf)

    for module in conf.env['ENABLE_MODULES']:
        if module == 'all':
            continue
        if module not in conf.env['MODULES_AVAILABLE']:
            Params.warning("Requested module %r is not available in this source tree." % module)
    if conf.env['MODULES_TO_BUILD']:
        print "** The following modules will be built:"
        for m in conf.env['MODULES_TO_BUILD']:
            print "\t%s" % m

    not_built = list(conf.env['MODULES_AVAILABLE'])
    for mod in conf.env['MODULES_TO_BUILD']:
        not_built.remove(mod)
    if not_built:
        print "** The following modules will NOT be built:"
        for m in not_built:
            print "\t%s" % m

    conf.write_config_header('config.h')

    for docs_module in ['gnomeprint', 'gnomeprintui', 'gtksourceview']:
        d = os.path.join('docs', docs_module, 'html')
        try:
            os.mkdir(d)
        except OSError:
            pass
        #    print "* Directory %r already exists." % (d,)
        #else:
        #    print "* Creating directory %r." % (d,)

def codegen(bld, module, local_load_types=(), register=(), local_register=(), prefix=None, py_ssize_t_clean=True):
    cmd = bld.new_task_gen('command',
                           source=['%s.defs' % module, '%s.override' % module],
                           target=['%s.c' % module])
    cmd.command = ['${CODEGEN}']

    if py_ssize_t_clean:
        cmd.command.append('--py_ssize_t-clean')

    register = [os.path.join(bld.env['PYGTK_DEFSDIR'], 'pango-types.defs'),
                os.path.join(bld.env['PYGTK_DEFSDIR'], 'gdk-types.defs'),
                os.path.join(bld.env['PYGTK_DEFSDIR'], 'gtk-types.defs'),
                os.path.join(bld.env['GNOME_PYTHON_DEFSDIR'], 'bonobo-types.defs'),
                os.path.join(bld.env['GNOME_PYTHON_DEFSDIR'], 'bonoboui-types.defs'),
                ] + list(register)

    cmd.command.extend(['--load-types', os.path.join(bld.env['GNOME_PYTHON_ARG_TYPES_DIR'], 'bonobo-arg-types.py')])
    
    for load in local_load_types:
        cmd.source.append(load)
        cmd.command.extend(['--load-types', '${SRC[%i]}' % (len(cmd.source)-1)])
    
    for reg in local_register:
        cmd.source.append(reg)
        cmd.command.extend(['--register', '${SRC[%i]}' % (len(cmd.source)-1)])

    for reg in register:
        cmd.command.extend(['--register', reg])

    if prefix:
        cmd.command.extend(['--prefix', prefix])
    else:
        cmd.command.extend(['--prefix', 'py'+module])

    cmd.command.extend(['--override', "${SRC[1]}",
                        '${SRC[0]}',
                        '>', '${TGT[0]}'])

    return cmd



def build_docs_for_module(bld, module_name):
    d = bld.path.find_dir('html').abspath()
    if bld.env['XSLTPROC'] and not os.path.exists(os.path.join(d, 'index.html')):
        html_dir = os.path.join(bld.env['DATADIR'], 'gtk-doc', 'html')
        target_dir = os.path.join('html_dir', module_name)

        cmd = bld.new_task_gen('command',
                               target='html/index.html',
                               source=('../ref-html-style.xsl %s-classes.xml' % module_name),
                               command=(
                '${XSLTPROC} --nonet --xinclude -o ${TGT[0].parent}/'
                ' --stringparam gtkdoc.bookname py%s'
                ' --stringparam gtkdoc.version ${VERSION}'
                ' --stringparam chunker.output.encoding UTF-8'
                ' ${SRC[0]} ${SRC[1]}' % module_name))

        #cmd = bld.new_task_gen('command',
        #                       target=('html/%s-class-reference.html' % module_name),
        #                       source='html/index.html',
        #                       command='gtkdoc-fixxref --module=${MODULE} --module-dir=${TGT[0].parent} --html-dir=${HTMLDIR}',
        #                       variables=dict(HTMLDIR=html_dir,
        #                                      MODULE=module_name))

    html_files = glob.glob(os.path.join(bld.path.find_dir('html').abspath(bld.env), '*'))
    html_files += glob.glob(os.path.join(bld.path.find_dir('html').abspath(), '*'))
    bld.install_files('${DATADIR}/gtk-doc/html/py%s' % module_name, html_files)


def build(bld):
    env = bld.env

    # Attach the 'codegen' method to the build context
    bld.codegen = types.MethodType(codegen, bld)
    # Generic template for building docs
    bld.build_docs_for_module = types.MethodType(build_docs_for_module, bld)

    def create_pyext(bld):
        return bld.new_task_gen('cc', 'shlib', 'pyext')
    bld.create_pyext = types.MethodType(create_pyext, bld)


    ## generate and install the .pc file
    obj = bld.new_task_gen('subst')
    obj.source = 'gnome-python-desktop-2.0.pc.in'
    obj.target = 'gnome-python-desktop-2.0.pc'
    obj.dict = {
        'VERSION': VERSION,
        'prefix': env['PREFIX'],
        'exec_prefix': env['PREFIX'],
        'libdir': env['LIBDIR'],
        'includedir': os.path.join(env['PREFIX'], 'include'),
        'datadir': env['DATADIR'],
        'datarootdir': env['DATADIR'],
        }
    obj.fun = misc.subst_func
    obj.install_path = '${LIBDIR}/pkgconfig'

    ## subdirs
    bld.add_subdirs('gnomekeyring')
    bld.add_subdirs('gnomeapplet')
    bld.add_subdirs('gnomedesktop')
    bld.add_subdirs('gnomeprint')
    bld.add_subdirs('evince')
    bld.add_subdirs('evolution')
    bld.add_subdirs('gtksourceview')
    bld.add_subdirs('gtop')
    bld.add_subdirs('mediaprofiles')
    bld.add_subdirs('metacity')
    bld.add_subdirs('nautilusburn')
    bld.add_subdirs('braseromedia')
    bld.add_subdirs('braseroburn')
    bld.add_subdirs('rsvg')
    bld.add_subdirs('totem')
    bld.add_subdirs('wnck')

    bld.add_subdirs('docs/gnomeprint')
    bld.add_subdirs('docs/gnomeprintui')
    bld.add_subdirs('docs/gtksourceview')

    if 'bugbuddy' in bld.env['MODULES_TO_BUILD']:
        py = bld.new_task_gen('py')
        py.install_path = '${PYTHONDIR}/gtk-2.0'
        py.source = "bugbuddy.py"


def shutdown():
    env = Build.bld.env
    if Options.commands['check']:
        _run_tests(env)


def _run_tests(env):
    import pproc as subprocess
    import shutil
    builddir = os.path.join(blddir, env.variant())
    # copy the __init__.py files
    for subdir in ["evolution", "gnomedesktop", "gnomeprint", "totem"]:
        src = os.path.join(subdir, "__init__.py")
        dst = os.path.join(builddir, subdir)
        try:
            shutil.copy(src, dst + os.path.sep)
        except IOError:
            pass
    os_env = dict(os.environ)
    if 'PYTHONPATH' in os_env:
        os_env['PYTHONPATH'] = os.pathsep.join([builddir, os_env['PYTHONPATH']])
    else:
        os_env['PYTHONPATH'] = builddir
    cmd = [env['PYTHON'], os.path.join('tests', 'runtests.py'), builddir]
    retval = subprocess.Popen(cmd, env=os_env).wait()
    if retval:
        sys.exit(retval)
