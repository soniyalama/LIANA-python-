__version__ = '0.1.7'
__version_info__ = tuple([int(num) for num in __version__.split('.')])

from liana import method as mt, plotting as pl, resource as rs, multi as mu, funcomics as fun

# done after everything has been imported (adapted from scanpy)
import sys
from scanpy._utils import annotate_doc_types

sys.modules.update({f'{__name__}.{m}': globals()[m] for m in ['mt', 'pl', 'rs', 'mu', 'fun']})
annotate_doc_types(sys.modules[__name__], 'liana')


del sys, annotate_doc_types
