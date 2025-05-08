import tkinter as tk
import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Create the main application window
app = tk.Tk()
app.geometry("350x250")
app.title("Music Player")


def play_music():
    pygame.mixer.music.load(r"C:\Users\Admin\Desktop\Project ML\static\Audio\mot1 .mp3")  # Replace with your audio file
    pygame.mixer.music.play()
def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def resume_music():
    pygame.mixer.music.unpause()

def exit_music():
    pygame.mixer.music.stop()
    app.destroy()

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)

# Create buttons for music control
play_button = tk.Button(app, text="Play", command=play_music)
pause_button = tk.Button(app, text="Pause", command=pause_music)
stop_button = tk.Button(app, text="Stop", command=stop_music)
resume_button = tk.Button(app, text="Resume", command=resume_music)
exit_button = tk.Button(app, text="Exit", command=exit_music)

# Place buttons on the window using grid layout
play_button.grid(row=0, column=0, padx=10, pady=10)
pause_button.grid(row=0, column=1, padx=10, pady=10)
stop_button.grid(row=0, column=2, padx=10, pady=10)
resume_button.grid(row=0, column=3, padx=10, pady=10)
exit_button.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

# Create a scale widget for volume control
volume_scale = tk.Scale(app, from_=0, to=1, resolution=0.1, orient="horizontal", label="Volume Control", command=set_volume)
volume_scale.set(0.5)  # Set default volume to 50%
volume_scale.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Run the application
app.mainloop()
