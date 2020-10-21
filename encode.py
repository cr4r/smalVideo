import os, subprocess

mediaa='video'

for subdirs, dirs, files in os.walk(mediaa):
    for file in files:
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".mp4":
            if not os.path.exists(subdirs+ '/compressed'):
                os.makedirs(subdirs+ '/compressed')
        mediain = subdirs +'/'+ file
        mediaout = subdirs +'/compressed/'+file
        subprocess.run('ffmpeg -i '+ mediain.replace(" ","\\ ") +' -vcodec h264 -acodec mp3 -crf 22 ' + mediaout.replace(" ","\\ "), shell=True)
