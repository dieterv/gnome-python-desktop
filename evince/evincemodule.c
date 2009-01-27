#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

void pyevince_register_classes (PyObject *d);

extern PyMethodDef pyevince_functions[];

DL_EXPORT(void)
initevince(void)
{
    PyObject *m, *d;

    init_pygobject ();

    m = Py_InitModule ("evince", pyevince_functions);
    d = PyModule_GetDict (m);

    pyevince_register_classes (d);
    pyevince_add_constants(m, "EV_");

    if (PyErr_Occurred ()) {
        return;
    }
}
