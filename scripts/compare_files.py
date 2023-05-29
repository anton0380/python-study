import filecmp
import sys
from pathlib import Path
import os

#  for colored output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# find files and check them
directory = ''
if len(sys.argv) > 1:
    directory = sys.argv[1]
print(f"searching path: {directory}")
pathlist = list(Path(directory).glob('**/*.*'))
quickly = True # wishout shallow and print only same
equal = 0
different = 0
for path1 in pathlist:
    for path2 in pathlist:
        if path1 < path2:
            # compare files
            same = filecmp.cmp(path1, path2, shallow=not quickly)
            # for print local path in selected folder
            p1 = str(path1).replace(directory, '', 1)
            p2 = str(path2).replace(directory, '', 1)
            if same:
                equal += 1
                os.remove(path2)
                pathlist.remove(path2)
            else:
                different += 1
            if not quickly or same:
                print(f"{p1} {p2} " + f"{bcolors.FAIL + 'equal'  + bcolors.ENDC if same else bcolors.OKGREEN + 'different' + bcolors.ENDC}")
            

print(f"{equal=}, {different=}")

