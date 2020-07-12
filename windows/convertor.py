def main():
    root = tk.Tk()
    root.withdraw()

    dir = ''
    files = filedialog.askopenfilenames()
    for file in files:
        paths = [i.strip() for i in file.split('/')]
        first_dir = '/'.join(paths[0:-1]) + '/'
        dir = first_dir
        last_one = paths[-1]
        mp4 = first_dir
        mp3 = first_dir

        if last_one[-4:]=='.mp4':
            mp4 += last_one
            mp3 += last_one[:-1] + '3'
        else:
            mp4 += last_one + '.mp4'
            mp3 += last_one + '.mp3'
        
        try:
            video = VideoFileClip(mp4)
            video.audio.write_audiofile(mp3)
            ctypes.windll.user32.MessageBoxW(
                0, 
                f'"{paths[-1]}" is converted', 
                'Result', 
                1
            )
        except:
            ctypes.windll.user32.MessageBoxW(
                0, 
                'An Error Occured!\n'+ 
                f'can\'t convert "{paths[-1]}"', 
                'Error', 
                1
            )
    webbrowser.open(dir)

import os, sys, webbrowser, ctypes

try:
    import tkinter as tk
    from tkinter import filedialog
except:
    import Tinter as tk
    from Tkinter import filedialog

try:
    import easygui
    from moviepy.editor import *
except:
    os.system("install.bat")
    try:
        import easygui
        from moviepy.editor import *
    except:
        print('\n--- An Error Occured! ---\n')
        input('\npress enter...')
        sys.exit()

main()