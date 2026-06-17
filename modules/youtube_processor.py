import yt_dlp

def download_audio(url):

    try:

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            return ydl.prepare_filename(info)

    except Exception as e:

        raise Exception(
            f"YouTube download failed: {str(e)}"
        )
