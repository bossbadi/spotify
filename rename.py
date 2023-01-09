import os

# rename the song by splitting name by "-" and keeping everything to the right
# of the first "-"

folder = input("Enter directory: ")

for filename in os.listdir(folder):
    if not filename.endswith('.mp3'):
        continue

    # get the name of the song
    parts = filename.split(' - ', 1)
    if len(parts) == 2:
        song_name = parts[1].strip()
        print(song_name)
        # rename the song
        os.rename(os.path.join(folder, filename), os.path.join(folder, song_name))
