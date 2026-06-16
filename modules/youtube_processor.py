import yt_dlp

def download_audio(url):

    options = {
        "format": "bestaudio",
        "outtmpl": "uploads/youtube_audio/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])