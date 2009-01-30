#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

#include <evince-document.h>

void pyevince_register_classes (PyObject *d);
void pyevince_add_constants(PyObject *module, const gchar *strip_prefix);

extern PyMethodDef pyevince_functions[];

DL_EXPORT(void)
initevince(void)
{
    PyObject *m, *d;

    /* Init glib threads asap */
    if (!g_thread_supported ())
       g_thread_init (NULL);

    init_pygobject ();

    pyg_enable_threads ();

    ev_init ();

    m = Py_InitModule ("evince", pyevince_functions);
    d = PyModule_GetDict (m);

    pyevince_register_classes (d);
    pyevince_add_constants(m, "EV_");

    if (PyErr_Occurred ()) {
        return;
    }
}
