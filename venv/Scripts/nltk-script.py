#!C:\Users\conso\PycharmProjects\Hallo\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nltk==3.5','console_scripts','nltk'
__requires__ = 'nltk==3.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nltk==3.5', 'console_scripts', 'nltk')()
    )
