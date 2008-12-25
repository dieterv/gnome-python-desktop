import os
import sys


modules = [
    "gnomeapplet",
    "gnomeprint",
    ("gnomeprint.ui", "gnomeprint"),
    "gtksourceview",
    "wnck",
    ("totem.plparser", "totem"),
    "gtop",
    "nautilusburn",
    "mediaprofiles",
    "metacity",
    "rsvg",
    "gnomekeyring",
    "gnomedesktop",
    ("evolution.ebook", "evolution"),
    ("evolution.ecal", "evolution"),
    ]

def run_import_tests(builddir, no_import_hooks):
    if not no_import_hooks:
        import ltihooks
        ltihooks.install()

    for item in modules:
        if isinstance(item, tuple):
            module, dirname = item
        else:
            module = item
            dirname = item
        sys.path.insert(0, os.path.join(builddir, dirname))
        print "Trying to import module %s... " % (module,),
        try:
            __import__(module) # try to import the module to catch undefined symbols
        except ImportError, ex:
            if ex.args[0].startswith("No module named"):
                print "not found"
            else:
                raise
        else:
            print "ok."

    if not no_import_hooks:
        ltihooks.uninstall()
