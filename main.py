from moviepy import editor

video = editor.VideoFileClip('88.mp4')
audio = video.audio
audio.write_audiofile('audio_1.mp3')