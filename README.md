# YouTube Downloader

Minimal Python script using the `yt-dlp` library for downloading YouTube videos with the **highest video + audio quality**, all in a single MKV file!

---

## Dependencies

**Install system dependencies:**

sudo apt update && sudo apt install -y ffmpeg pipx mediainfo


**Install `yt-dlp` via pipx:**

pipx install yt-dlp && yt-dlp --version && pipx ensurepath


**Install `mediainfo` (optional):**

sudo apt install mediainfo

---

## Usage

**Download a single video:**

py script.py <URL>


**Download multiple videos or playlists from a file:**

py script.py links.txt

Format of `links.txt`: one URL per line.


**Check downloaded file:**

mediainfo "filename.mkv"
