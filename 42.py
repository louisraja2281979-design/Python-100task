from pytubefix import YouTube

def download_video(url):
    try:
        yt = YouTube(url)

        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Views:", yt.views)

        # Get highest resolution stream
        stream = yt.streams.get_highest_resolution()

        print("Downloading...")
        stream.download(output_path="downloads")

        print("Download completed!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ")
    download_video(video_url)