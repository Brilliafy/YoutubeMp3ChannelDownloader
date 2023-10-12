import scrapetube
import yt_dlp as youtube_dl
import sys
import os
from concurrent.futures import ThreadPoolExecutor

def download_ytvid_as_mp3(url, filenamePath):
    video_url = url
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = os.path.join(filenamePath, f"{video_info['title']}.mp3")
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete: {}".format(filename))

channelID = sys.argv[1]
folderLocation = sys.argv[2]
threads = int(sys.argv[3])

videos = scrapetube.get_channel(channelID)
print("Starting download of channel...")
pool = ThreadPoolExecutor(threads)
for video in videos:
    pool.submit(download_ytvid_as_mp3, video['videoId'], folderLocation)
print("Channel successfully downloaded!")