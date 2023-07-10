from tkinter import Tk

from Player.src.playlist import Playlist
from Player.src.player_controls import PlayerControls
from Player.src.utils import load_songs_directory

# Creating the master GUI
root = Tk()
root.geometry('700x320')
root.title('Music Player From Python')
root.resizable(0, 0)

# Adding icon in window
root.iconbitmap('..//icon2.png')



# Initialize the playlist
playlist = Playlist()

# Create player controls
controls = PlayerControls(root, playlist)

# Finalize the GUI
root.update()
root.mainloop()
