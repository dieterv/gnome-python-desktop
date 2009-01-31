/* -*- Mode: C; c-basic-offset: 4 -*- */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>
#include <panel-applet.h>
#include <bonobo/bonobo-main.h>
#include <signal.h>
#include <libgnome/gnome-program.h>
#include <libgnomeui/gnome-ui-init.h>

void pyapplet_register_classes (PyObject *d);

extern PyMethodDef pyapplet_functions[];

DL_EXPORT(void)
initgnomeapplet(void)
{
    PyObject *m, *d;

    struct sigaction sa;
    PyObject *av;
    int argc, i;
    char **argv;
	
    init_pygobject();
    PyImport_ImportModule("bonobo.ui");
    if (PyErr_Occurred())
        return;

    m = Py_InitModule ("gnomeapplet", pyapplet_functions);
    d = PyModule_GetDict (m);
	
    pyapplet_register_classes (d);
    PyModule_AddIntConstant (m, "NO_BACKGROUND", PANEL_NO_BACKGROUND);
    PyModule_AddIntConstant (m, "COLOR_BACKGROUND", PANEL_COLOR_BACKGROUND);
    PyModule_AddIntConstant (m, "PIXMAP_BACKGROUND", PANEL_PIXMAP_BACKGROUND);

    PyModule_AddIntConstant (m, "ORIENT_UP", PANEL_APPLET_ORIENT_UP);
    PyModule_AddIntConstant (m, "ORIENT_DOWN", PANEL_APPLET_ORIENT_DOWN);
    PyModule_AddIntConstant (m, "ORIENT_LEFT", PANEL_APPLET_ORIENT_LEFT);
    PyModule_AddIntConstant (m, "ORIENT_RIGHT", PANEL_APPLET_ORIENT_RIGHT);

    PyModule_AddIntConstant (m, "SIZE_XX_SMALL", GNOME_Vertigo_PANEL_XX_SMALL);
    PyModule_AddIntConstant (m, "SIZE_X_SMALL", GNOME_Vertigo_PANEL_X_SMALL);
    PyModule_AddIntConstant (m, "SIZE_SMALL", GNOME_Vertigo_PANEL_SMALL);
    PyModule_AddIntConstant (m, "SIZE_MEDIUM", GNOME_Vertigo_PANEL_MEDIUM);
    PyModule_AddIntConstant (m, "SIZE_LARGE", GNOME_Vertigo_PANEL_LARGE);
    PyModule_AddIntConstant (m, "SIZE_X_LARGE", GNOME_Vertigo_PANEL_X_LARGE);
    PyModule_AddIntConstant (m, "SIZE_XX_LARGE", GNOME_Vertigo_PANEL_XX_LARGE);

    PyModule_AddIntConstant (m, "EXPAND_MAJOR", PANEL_APPLET_EXPAND_MAJOR);
    PyModule_AddIntConstant (m, "EXPAND_MINOR", PANEL_APPLET_EXPAND_MINOR);
    PyModule_AddIntConstant (m, "HAS_HANDLE", PANEL_APPLET_HAS_HANDLE);

    /* make sure ORBit2-python is ready? */
    /* this code is copy-pasted from bonobomodule.c */

    av = PySys_GetObject("argv");
    if (av != NULL) {
	argc = PyList_Size(av);

	argv = g_new(char *, argc);
	for (i = 0; i < argc; i++)
	    argv[i] = g_strdup(PyString_AsString(PyList_GetItem(av, i)));
    } else {
	argc = 0;
	argv = NULL;
    }
    memset(&sa, 0, sizeof(sa));
    sigaction(SIGCHLD, NULL, &sa);

    if (!bonobo_init(&argc, argv)) {
	if (argv != NULL) {
	    for (i = 0; i < argc; i++)
		g_free(argv[i]);
	    g_free(argv);
	}
	sigaction(SIGCHLD, &sa, NULL);
	PyErr_SetString(PyExc_RuntimeError, "could not initialise Bonobo");
	return;
    }
    sigaction(SIGCHLD, &sa, NULL);

    if (argv != NULL) {
	PySys_SetArgv(argc, argv);
	for (i = 0; i < argc; i++)
	    g_free(argv[i]);
	g_free(argv);
    }

    gnome_program_module_register (LIBGNOMEUI_MODULE);
}
