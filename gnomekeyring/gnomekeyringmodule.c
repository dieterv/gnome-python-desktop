/* -*- Mode: C; c-basic-offset: 4 -*- */
#include <Python.h>
#include <gnome-keyring.h>

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

/* include this first, before NO_IMPORT_PYGOBJECT is defined */
#include <pygobject.h>

static PyObject *PyGKExc_Error;

static PyObject *PyGKExc_DeniedError; /* GNOME_KEYRING_RESULT_DENIED */
static PyObject *PyGKExc_NoKeyringDaemonError; /* GNOME_KEYRING_RESULT_NO_KEYRING_DAEMON */
static PyObject *PyGKExc_AlreadyUnlockedError; /* GNOME_KEYRING_RESULT_ALREADY_UNLOCKED */
static PyObject *PyGKExc_NoSuchKeyringError; /* GNOME_KEYRING_RESULT_NO_SUCH_KEYRING */
static PyObject *PyGKExc_BadArgumentsError; /* GNOME_KEYRING_RESULT_BAD_ARGUMENTS */
static PyObject *PyGKExc_IOError; /* GNOME_KEYRING_RESULT_IO_ERROR */
static PyObject *PyGKExc_CancelledError; /* GNOME_KEYRING_RESULT_CANCELLED */
static PyObject *PyGKExc_AlreadyExistsError; /* GNOME_KEYRING_RESULT_ALREADY_EXISTS */

PyObject *
pygnomekeyring_result_to_exception(GnomeKeyringResult result)
{
    switch(result)
    {
#define keyring_result_case(result_suffix, exc_middle)  \
    case GNOME_KEYRING_RESULT_##result_suffix:          \
        return PyGKExc_##exc_middle##Error;

        keyring_result_case(DENIED, Denied);
        keyring_result_case(NO_KEYRING_DAEMON, NoKeyringDaemon);
        keyring_result_case(ALREADY_UNLOCKED, AlreadyUnlocked);
        keyring_result_case(NO_SUCH_KEYRING, NoSuchKeyring);
        keyring_result_case(BAD_ARGUMENTS, BadArguments);
        keyring_result_case(IO_ERROR, IO);
        keyring_result_case(CANCELLED, Cancelled);
        keyring_result_case(ALREADY_EXISTS, AlreadyExists);

#undef keyring_result_case

    case GNOME_KEYRING_RESULT_OK:
        return Py_None;

    default:
        g_warning("unhandled GnomeKeyringResult code %i => "
                  "http://bugzilla.gnome.org/enter_bug.cgi?product=gnome-python-desktop",
                  result);
        return PyGKExc_Error;
    }
}

gboolean
pygnomekeyring_result_check(GnomeKeyringResult result)
{
    PyObject *exc;

    /* be optimistic */
    if (G_LIKELY(result == GNOME_KEYRING_RESULT_OK))
	return FALSE;

    exc = pygnomekeyring_result_to_exception(result);

    PyErr_SetNone(exc);
    return TRUE;
}

static void
initialize_exceptions(PyObject *d)
{
    PyGKExc_Error = PyErr_NewException("gnomekeyring.Error",
                                       PyExc_Exception, NULL);
    PyDict_SetItemString(d, "Error", PyGKExc_Error);

#define register_exception(name)                                        \
    PyGKExc_##name##Error =                                             \
        PyErr_NewException("gnomekeyring." #name "Error",               \
                            PyGKExc_Error, NULL);                       \
    PyDict_SetItemString(d, #name "Error", PyGKExc_##name##Error);


    register_exception(Denied);
    register_exception(NoKeyringDaemon);
    register_exception(AlreadyUnlocked);
    register_exception(NoSuchKeyring);
    register_exception(BadArguments);
    register_exception(IO);
    register_exception(Cancelled);
    register_exception(AlreadyExists);

#undef register_exception
}


void pygnomekeyring_register_classes(PyObject *d);
void pygnomekeyring_add_constants(PyObject *module, const gchar *strip_prefix);
extern PyMethodDef pygnomekeyring_functions[];

DL_EXPORT(void)
initgnomekeyring(void)
{
    PyObject *m, *d;

    init_pygobject();

    m = Py_InitModule("gnomekeyring", pygnomekeyring_functions);
    d = PyModule_GetDict(m);
    initialize_exceptions(d);
    pygnomekeyring_register_classes(d);
    pygnomekeyring_add_constants(m, "GNOME_KEYRING_");
}

