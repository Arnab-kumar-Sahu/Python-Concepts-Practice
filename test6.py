import subprocess
from yt_dlp import YoutubeDL

# Replace with your PotPlayer path
POTPLAYER_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"

def play_song(query):
    # Step 1: Search and get best audio URL
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'default_search': 'ytsearch1',
        'noplaylist': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if 'entries' in info:
            info = info['entries'][0]  # first result
        audio_url = info['url']
        title = info['title']
        print(f"Now playing: {title}")

    # Step 2: Play in PotPlayer
    subprocess.run([POTPLAYER_PATH, audio_url])

# Example usage
if __name__ == "__main__":
    song_name = input("Enter song name to play: ")
    play_song(song_name)
