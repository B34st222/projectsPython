from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import pytube

print(pytube.__file__)
def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Download complete")

    except Exception as e:
        print(e)


url = "https://www.youtube.com/watch?v=FZUcpVmEHuk"

save_path = "C:/Users/wmadg/Documents/GitHub/projectsPython/youtube"

download_video(url, save_path)