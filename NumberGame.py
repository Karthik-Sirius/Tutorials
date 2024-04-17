#Number Guessing Game:
import random
print("Welcome to the number guessing game")
Number = input("Enter the number")
if Number.isdigit():
    Number = int(Number)
    if Number<=0:
        print("Please enter the number greater then 0")
        quit()
else:
    print("Enter the number once again")
    quit()
RandomNum = random.randint(0,Number)
Guess = 0
while True:
    Guess = Guess+1
    User = input("Make a guess")
    if User.isdigit():
        User = int(User)
    else:
        print("enter the number once again")
        continue
    if User == RandomNum:
        print("You Got it")
        break
    elif User>RandomNum:
        print("You were above the number")
    else:
        print("You are just below")
print("You got it in",Guess,"guesses")

#Video Downloader:
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
