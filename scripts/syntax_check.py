import os
from glob import glob

for file in glob('*.py') + glob('examples/*py'):
    os.system('pep8.py --repeat %s' % file)

