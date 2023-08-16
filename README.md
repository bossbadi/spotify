# spotify
Easily sync your Spotify playlists to a local folder

## Setup
1. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
1. Put your Spotify playlist urls in `playlists.json` in the following format
    ```json
    {
        "PLAYLIST_NAME": "PLAYLIST_URL",
        "PLAYLIST_NAME": "PLAYLIST_URL",
        "PLAYLIST_NAME": "PLAYLIST_URL...",
    }
    ```

## Python usage
Sync all playlists from `playlists.json`
```bash
python sync.py
```

Sync a specific playlist from `playlists.json` (you can type the first few letters of the playlist name)
```bash
python sync.py SOME PLAYLIST NAME
```

## Batch usage
There's also a batch script for convenience. Just replace `python sync.py` with `sync` in the above commands, e.g.
```bash
sync
```
```bash
sync SOME PLAYLIST NAME
```

## Termux setup
```bash
# setup storage
yes | termux-setup-storage

# install dependencies
pkg update
pkg install -y python
pkg install -y ffmpeg

# download repository
git clone "https://github.com/bossbadi/spotify"
cd spotify/
pip install -r requirements.txt
chmod +x spotify  # this script is the playlist downloader
mv spotify ..
mv * ~/storage/music/
cd ..
rm -rf spotify/
```
