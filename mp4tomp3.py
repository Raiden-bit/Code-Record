#converted the mp4 video to mp3 audio
from moviepy.editor import VideoFileClip
import os
def get_movie(dir):                                                       #get mp4 dir
    list_movie = os.listdir(dir)
    return list_movie
movie_list = get_movie('D:/mp4tomp3')
#print(movie_list)
for each_movie in movie_list:
    if '.' in each_movie:                                                   #only get mp4 file
        movie_name = each_movie.split('.')[0]
        video = VideoFileClip(f'D:/mp4tomp3/{each_movie}')
        c_audio = video.audio                                                #mp3 audio
        c_audio.write_audiofile(f'D:/mp4tomp3/mp3/{movie_name}.mp3')
    else:
        continue



