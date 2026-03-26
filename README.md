# YouTube Downloader

Minimal Python script using the `yt-dlp` library for downloading YouTube videos with the **highest video + audio quality**, all in a single MKV file!

---

## Dependencies

**Install system dependencies:**

`sudo apt update && sudo apt install -y ffmpeg pipx mediainfo`

<br>

**Install `yt-dlp` via pipx:**

`pipx install yt-dlp && yt-dlp --version && pipx ensurepath`

<br>

**Install `mediainfo` (optional):**

`sudo apt install mediainfo`

---

## Usage

**Download one video:**

`py script.py <URL>`

<br>

**Download multiple videos or playlists:**

`py script.py <URL1> <URL2> <URLn>`
or
`py script.py file`

Format of `file`: one video URL per line.

<br>

**Check downloaded file:**

`mediainfo <filename.mkv>"`

<br>

**If file download fails, reinstall yt-dlp library:**

`pipx uninstall yt-dlp && pipx install yt-dlp && pipx ensurepath`
