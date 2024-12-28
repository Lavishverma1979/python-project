import tkinter as tk
from tkinter import messagebox
import yt_dlp as ytdl
import os

# Function to download the video
def download_video():
    url = url_entry.get()

    if not url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return
    
    try:
        # Get the download folder from the input
        download_folder = folder_entry.get()

        # If no folder is specified, use the home directory
        if not download_folder:
            download_folder = os.path.expanduser("~")  # Default to home directory
        
        # Make sure the folder exists
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Setup download options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save with the video title
        }

        # Download video using yt-dlp
        with ytdl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Show success message
        messagebox.showinfo("Success", f"Video downloaded successfully!\nSaved to {download_folder}")

    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")

# Set up the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")  # Window size

# Create URL entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create Folder entry
folder_label = tk.Label(root, text="Enter Download Folder (Optional):")
folder_label.pack(pady=10)

folder_entry = tk.Entry(root, width=50)
folder_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()
