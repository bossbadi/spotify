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
python main.py
```

Sync specific playlists from `playlists.json`.

```bash
python main.py PLAYLIST_NAME PLAYLIST_NAME_2 ...
```

If there are spaces in the playlist name, put the name in quotes

```bash
python main.py "PLAYLIST NAME" "PLAYLIST NAME 2" ...
```

## Android (Termux)

For Android users, download Termux, Termux:API, and run the following commands:

```bash
# setup storage
yes | termux-setup-storage

# install dependencies
pkg update
pkg install -y git
pkg install -y termux-api
pkg install -y ffmpeg
pkg install -y tur-repo
pkg install -y python3.11
pkg install -y rust

# download repository
git clone "https://github.com/bossbadi/spotify" ~/storage/music/
cd ~/storage/music/
pip3.11 install --upgrade pip
pip3.11 install -r requirements.txt

# activate scripts
mkdir -p ~/.local/bin/
cp bin/* ~/.local/bin/
chmod -R +x ~/.local/bin/
echo 'export PATH=/data/data/com.termux/files/home/.local/bin:$PATH' >> ~/.bashrc

cd
```

Then, whenever you want to sync your playlists to your phone, just open Termux and run one of the following commands:

```bash
spotify
spotify PLAYLIST_NAME PLAYLIST_NAME_2 ...
spotify "PLAYLIST NAME" "PLAYLIST NAME 2" ...
```
