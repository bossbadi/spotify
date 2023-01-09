# sync spotify playlists from playlists.txt

import os


def main():
    cmd_base = 'python -m spotdl --output "{list-name}/{title}.{output-ext}" --save-file .sync.spotdl sync'

    with open('playlists.txt', 'r') as f:
        for line in f.read().splitlines():
            if '#' in line:
                line = line.rsplit('#', 1)[0].strip()
            cmd_base += f' {line}'

    os.system(cmd_base)


if __name__ == '__main__':
    main()
