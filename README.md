# spotify

Easily sync your Spotify playlists to a local folder

## Setup

Install the requirements

```bash
pip install -r requirements.txt
```

Put your Spotify playlist urls in `playlists.json` in the following format

```json
{
  "PLAYLIST_NAME": "PLAYLIST_URL",
  "PLAYLIST_NAME_2": "PLAYLIST_URL_2",
  "PLAYLIST_NAME_3": "..."
}
```

## General usage

Sync all playlists from `playlists.json`

```bash
python spotify.py
```

Sync specific playlists from `playlists.json`.

```bash
python spotify.py PLAYLIST_NAME PLAYLIST_NAME_2 ...
```

If there are spaces in the playlist name, put the name in quotes

```bash
python spotify.py "PLAYLIST NAME" "PLAYLIST NAME 2" ...
```

## Windows

For Windows users, you can use the batch script. Just replace `python spotify.py` with `spotify` in the above commands:

```pwsh
spotify
spotify PLAYLIST_NAME PLAYLIST_NAME_2 ...
spotify "PLAYLIST NAME" "PLAYLIST NAME 2" ...
```

## Android (Termux)

For Android users, download Termux (preferably from F-Droid) and run the following commands:

```bash
# setup storage
yes | termux-setup-storage

# install dependencies
pkg update
pkg install -y python
pkg install -y ffmpeg

# download repository
git clone "https://github.com/bossbadi/spotify" ~/storage/music/
cd ~/storage/music/
pip install -r requirements.txt
chmod +x spotify  # this script is the playlist downloader
mv spotify ~/
cd
```

Then, whenever you want to sync your playlists to your phone, just open Termux and run one of the following commands:

```bash
./spotify
./spotify PLAYLIST_NAME PLAYLIST_NAME_2 ...
./spotify "PLAYLIST NAME" "PLAYLIST NAME 2" ...
```
