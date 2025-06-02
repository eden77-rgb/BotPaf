import yt_dlp

class serviceYoutube:
    def __init__(self):
        ytdl_format_options = {
            "format": "bestaudio/best",
            "quiet": True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'no_warnings': True,
            'default_search': 'ytsearch'
        }
        self.ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

    def search(self, query):
        try:
            results = self.ytdl.extract_info(f"ytsearch:{query}", download=False)
            entry = results["entries"][0]
            return {
                "title": entry["title"],
                "url": entry["webpage_url"]
            }
        except Exception as e:
            print(f"[serviceYoutube] Erreur de recherche : {e}")
            return None
