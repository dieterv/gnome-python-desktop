# -*- Mode: Python; py-indent-offset: 4 -*-
import warnings
warnings.warn("The module gnomeprint is deprecated; "
              "please use gtk 2.10 and cairo instead.",
              DeprecationWarning, stacklevel=2)
del warnings

from _print import *

