from pymediainfo import MediaInfo
media_info = MediaInfo.parse('test.mp4')
for track in media_info.tracks:
  if track.track_type == 'General':
    data_size = int(track.datasize)
  if track.track_type == 'Video':
    video_size = int(track.stream_size)
  if track.track_type == 'Audio':
    audio_size = int(track.stream_size)
print(f"data size = {data_size}")
print(f"video size = {video_size}")
print(f"audio size = {audio_size}")
surplus = data_size - video_size - audio_size
print(f"surplus = {surplus}")
