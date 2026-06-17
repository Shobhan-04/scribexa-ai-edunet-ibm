import yt_dlp
import os

def download_audio(url):

    os.makedirs("downloads", exist_ok=True)

    output_path = "downloads/lecture.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("downloads"):

        if file.startswith("lecture"):

            return os.path.join(
                "downloads",
                file
            )

    return None
