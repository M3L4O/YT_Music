from pytube import YouTube
import subprocess


def get_stream(link):
    yt = YouTube(link)
    infos = f"Title: {yt.title}\nDescription: {yt.description} "
    print(infos)
    stream = yt.streams.filter(only_audio=True)[0]

    return stream


def download_audio(stream, output_dir="/home/melao/Música/"):
    path = stream.download(output_dir)
    subprocess.run(f"ffmpeg -i '{path}' '{path.replace('mp4','mp3')}'", shell=True)
    
    return path.replace('mp4', 'mp3')

def main():
    link = input("Enter with the link\n~")
    path = download_audio(get_stream(link))
    
    print(f"The song was saved in {path}")


if __name__ == "__main__":
    main()
