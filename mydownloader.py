import yt_dlp
import os

def download_playlist(playlist_url):
    # These options are optimized for playlists
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        # This template creates a folder for the playlist and numbers the files
        'outtmpl': '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'yes_playlist': True,          # Explicitly tell it to expect a playlist
        'ignoreerrors': True,          # Skip videos that are deleted or private
        'quiet': False,                # Show progress for each video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting playlist download...")
            ydl.download([playlist_url])
            print("\nFinished! Check the folder created in your directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Paste your playlist link here
url = "https://youtube.com/playlist?list=PL7Fz0zORTAON05WGrOQvAgHx6Cc4YlN8Z&si=zFZRwb0j2EmJ8Kmz"
download_playlist(url)