import os, subprocess

mediaa='video/'

for subdirs, dirs, files in os.walk(mediaa):
    for file in files:
        extension = os.path.splitext(file)[-1].lower()
        if extension == ".mp4":
            mediain = subdirs +"/"+ file
            mediaout = subdirs +"/"+ 'compressed_'+file
            subprocess.run('ffmpeg -i '+ mediain.replace(" ","\\ ") +' -vcodec libx264 -crf 22 ' + mediaout.replace(" ","\\ "), shell=True)
