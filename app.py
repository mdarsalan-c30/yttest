import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp as youtube_dl
import os

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    download_path = filedialog.askdirectory()
    if not download_path:
        messagebox.showerror("Error", "Please select a download folder.")
        return

    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save video in selected folder
            'format': 'best',
        }

        # Download the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Label
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

# URL Entry
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Start the GUI loop
root.geometry("400x200")
root.mainloop()
