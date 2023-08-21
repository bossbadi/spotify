# sync spotify playlists from playlists.json

import json
import os
import sys

# this command is initially run to create the .sync.spotdl file
CMD_BASE_INIT = (
    'spotdl sync %s'
    ' --output "{list-name}/{title}.{output-ext}"'
    ' --save-file "%s/.sync.spotdl"'
)

# this command is run when the .sync.spotdl file already exists
CMD_BASE_MAIN = (
    'spotdl sync "%s/.sync.spotdl"'
    ' --output "{list-name}/{title}.{output-ext}"'
)

with open('playlists.json', 'r') as f:
    PLAYLISTS = json.load(f)


def sync_playlist(query):
    for playlist in PLAYLISTS:
        if not playlist.startswith(query):
            continue

        print(f'>>> Syncing playlist "{playlist}"')

        # create playlist directory
        os.makedirs(playlist, exist_ok=True)

        if os.path.exists(f'{playlist}/.sync.spotdl'):
            os.system(CMD_BASE_MAIN % (playlist))
        else:
            os.system(CMD_BASE_INIT % (PLAYLISTS[playlist], playlist))

        break
    else:
        print(f'Playlist "{query}" not found')


def main():
    if len(sys.argv) > 1:
        for name in sys.argv[1:]:
            sync_playlist(name)
    else:
        print('>>> Syncing all playlists')
        for name in PLAYLISTS:
            sync_playlist(name)


if __name__ == '__main__':
    main()
