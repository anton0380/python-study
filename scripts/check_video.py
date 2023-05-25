from pymediainfo import MediaInfo

def check_file(file_name: str) -> bool:
    media_info = MediaInfo.parse(file_name)
    for track in media_info.tracks:
        if track.track_type == 'General':
            data_size = int(track.datasize)
        if track.track_type == 'Video':
            video_size = int(track.stream_size)
        if track.track_type == 'Audio':
            audio_size = int(track.stream_size)
    surplus = data_size - video_size - audio_size
    return surplus

from pathlib import Path

directory = ''
pathlist = Path(directory).glob('**/*.mp4')
for path in pathlist:
    res = check_file(path)
    print(str(path) + ' ' + f"{'ok' if res >= 0 else 'error'} ({res})")