#adhoc script that locates pyfiglet.  Also contains command to create binary distribution of the script
#script is not using ppyfiglet so this functionality is deprecated

import pyfiglet
import os

print(pyfiglet.__file__)
path = os.path.dirname(pyfiglet.__file__)
print(path)

#pyinstaller --clean --distpath dist --name console --additional-hooks-dir pyinstaller/ --onefile console.py