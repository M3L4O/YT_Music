from pytube import YouTube, Playlist
import subprocess
import re
import os


def get_stream(link):
    yt = YouTube(link)
    infos = f"Title: {yt.title}"
    print(infos)
    stream = yt.streams.filter(only_audio=True)[0]

    return stream


def download_music_from_video(link, output_dir="/home/melao/Música/"):
    stream = get_stream(link)
    path = stream.download(output_dir)
    subprocess.run(f"ffmpeg -i '{path}' '{path.replace('mp4','mp3')}'")
    os.remove(path)
    
    print(f"Save in {path.replace('mp4','mp3')}")

def download_music_from_playlist(link, output_dir="/home/melao/Música/"):
    p = Playlist(link)
    print(f"Playlist tile: {p.title}")
    for url in p.video_urls:
        download_music_from_video(url, output_dir=output_dir) 

def main():
    link = input("Enter with the link\n~")

    if re.search("playlist", link):
        print("This is link for a playlist...")
        download_music_from_playlist(link, output_dir="/home/melao/Música/NightCore/")
    else:
        download_music_from_video(link)



if __name__ == "__main__":
    main()
