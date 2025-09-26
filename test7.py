import subprocess
from yt_dlp import YoutubeDL

POTPLAYER_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"

def search_youtube(prompt, max_results=10):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # only metadata, no download
        'noplaylist': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        query = f"ytsearch{max_results}:{prompt}"
        result = ydl.extract_info(query, download=False)
        return [entry['url'] for entry in result['entries']]

def play_video(url):
    print(f"Playing: {url}")
    subprocess.run([POTPLAYER_PATH, url])

def main():
    prompt = input("Enter search prompt for YouTube: ").strip()
    urls = search_youtube(prompt, max_results=20)
    if not urls:
        print("⚠️ No videos found.")
        return

    print(f"Found {len(urls)} videos. Playing now...")
    for url in urls:
        play_video(url)

if __name__ == "__main__":
    main()












