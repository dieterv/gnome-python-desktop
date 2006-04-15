/* -*- Mode: C; c-basic-offset: 4 -*- */
#include <Python.h>

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

#include <pygtk/pygtk.h>

void pymetacity_register_classes(PyObject *d);
extern PyMethodDef pymetacity_functions[];

DL_EXPORT(void)
initmetacity (void)
{
	PyObject *m, *d;

	init_pygobject();
	init_pygtk ();

	m = Py_InitModule ("metacity", pymetacity_functions);
	d = PyModule_GetDict (m);

	pymetacity_register_classes (d);
        pymetacity_add_constants(m, "META_");
}