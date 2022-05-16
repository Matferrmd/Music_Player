import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os


music_player = tkinter.Tk()
music_player.title("Music Player")
music_player.geometry("205x340")



directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()
play_list = tkinter.Listbox(music_player, font="Helvetica 12", bg="black", fg="lightgreen", selectmode=tkinter.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
    


pygame.init()
pygame.mixer.init

def play():
    pygame.mixer.music.load(play_list.get(tkinter.ACTIVE))
    vars.set(play_list.get(tkinter.ACTIVE))
    pygame.mixer.music.play()
    

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()


    
Button1 = tkinter.Button(music_player, width=5, height=1,font="Helvetica 12 bold", text="Play" , command=play, bg="black", fg="yellow")
Button2 = tkinter.Button(music_player, width=5, height=1,font="Helvetica 12 bold", text="Stop" , command=stop, bg="black", fg="red")
Button3 = tkinter.Button(music_player, width=5, height=1,font="Helvetica 12 bold", text="Pause" , command=pause, bg="black", fg="green")
Button4 = tkinter.Button(music_player, width=5, height=1,font="Helvetica 12 bold", text="Unpause" , command=unpause, bg="black", fg="lightblue")

vars = tkinter.StringVar()
song_title = tkinter.Label(music_player, font="Helvetica 10", textvariable=vars)


song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")



music_player.mainloop()