from pymediainfo import MediaInfo
from pathlib import Path
import sys
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

# check file size
def check_file(file_name: str) -> int:
    media_info = MediaInfo.parse(file_name)
    audio_size = 0 # video can be without audio
    for track in media_info.tracks:
        if track.track_type == 'General':
            data_size = int(track.datasize)
        if track.track_type == 'Video':
            video_size = int(track.stream_size)
        if track.track_type == 'Audio':
            audio_size = int(track.stream_size)
    surplus = data_size - video_size - audio_size
    return surplus

# find files and check them
directory = ''
if len(sys.argv) > 1:
    directory = sys.argv[1]
print(f"searching path: {directory}")
pathlist = Path(directory).glob('**/*.mp4')
success = 0
errors = 0
warnings = 0
for path in pathlist:
    p = str(path).replace(directory, '', 1) # for print local path in selected folder
    try:
        res = check_file(path)
        if res >= 0:
            success += 1
        else:
            errors += 1
        if res < 0:
            print(str(p) + ' ' + f"{bcolors.FAIL + 'error' + bcolors.ENDC} ({res})")
            os.remove(path)
    except Exception as err:
        # error in parse file header
        warnings += 1
        print(str(p) + ' ' + bcolors.WARNING + 'warning: something wrong'  + bcolors.ENDC)
        os.remove(path)
print(f"count {success=}, {errors=}, {warnings=}")


