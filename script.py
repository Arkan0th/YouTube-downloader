import subprocess
import sys
import pathlib

DOWNLOAD_DIR = pathlib.Path(__file__).parent

def download(target):
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mkv",

        "--add-metadata",
        "--embed-thumbnail",
        "--embed-chapters",

        "-P", str(DOWNLOAD_DIR),
        "-o", "%(title)s.%(ext)s",

        target
    ]

    subprocess.run(cmd, check=True)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 yt.py <URL | file.txt>")
        sys.exit(1)

    arg = sys.argv[1]

    if pathlib.Path(arg).is_file():
        arg = f"--batch-file={arg}"

    download(arg)


if __name__ == "__main__":
    main()

