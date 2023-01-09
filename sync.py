# sync spotify playlists from playlists.json

import json
import os
import sys


CMD_BASE = 'python -m spotdl --output "{list-name}/{title}.{output-ext}" --save-file "%s/.sync.spotdl" sync %s'

with open('playlists.json', 'r') as f:
    PLAYLISTS = json.load(f)


def sync_playlist(query):
    for playlist in PLAYLISTS:
        if playlist.startswith(query):
            print(f'Syncing playlist "{playlist}"')

            # create playlist directory
            os.makedirs(playlist, exist_ok=True)

            # create .sync.spotdl file
            sync_filename = f'{playlist}/.sync.spotdl'
            if not os.path.exists(sync_filename):
                with open(sync_filename, 'w') as f:
                    f.write('')

            os.system(CMD_BASE % (playlist, PLAYLISTS[playlist]))
            break
    else:
        print(f'Playlist "{query}" not found')


def main():
    if len(sys.argv) > 1:
        sync_playlist(sys.argv[1])
    else:
        print('Syncing all playlists')
        for name in PLAYLISTS:
            sync_playlist(name)


if __name__ == '__main__':
    main()
