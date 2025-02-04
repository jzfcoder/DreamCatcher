import os
import pygame

def play_mp3_files(folder_path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Get all MP3 files in the folder
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

    # Play each MP3 file
    for i, mp3_file in enumerate(mp3_files):
        print(i, 'out of', len(mp3_files))

        file_path = os.path.join(folder_path, mp3_file)
        print('now playing: ' + file_path)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait until the song finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        os.remove(file_path)

# Provide the path to your folder containing MP3 files
folder_path = './output'
play_mp3_files(folder_path)