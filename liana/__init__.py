import os
import pathlib
parent_dir = pathlib.Path(__file__).parent.parent.absolute()

with open(os.path.join(parent_dir, 'pyproject.toml'), 'r') as toml_file:
    for line in toml_file:
        if line.strip().startswith('version'):
            version = line.split('=')[1].strip().strip('"')
            break
__version__ = version

from liana import method as mt, plotting as pl, resource as rs, multi as mu, utils as ut, testing

# done after everything has been imported (adapted from scanpy)
import sys
from scanpy._utils import annotate_doc_types

sys.modules.update({f'{__name__}.{m}': globals()[m] for m in ['mt', 'pl', 'rs', 'ut']})
annotate_doc_types(sys.modules[__name__], 'liana')

del sys, annotate_doc_types
