import os
import sys

from functions import ROOT_DIR

sys.argv = [1, 'arg2']  # Pass PreID number to use
exec(open(os.path.join(ROOT_DIR, 'Hico Group', 'openUrl.py'), "r").read())
exec(open(os.path.join(ROOT_DIR, 'Hico Group', 'hico.py'), "r").read())
