import os
songs=[]
def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield(filename)

for mp3file in mp3gen():
    songs.append(mp3file)
print(songs)
