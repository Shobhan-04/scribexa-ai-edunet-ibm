import yt_dlp

def download_audio(url):

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/audio.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        ydl.download([url])

    return "downloads/audio.webm"
