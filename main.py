from tkinter import * 
from tkinter import filedialog 
import pygame 
import os 
import tkinter.messagebox as fmsg 
import random 
from mutagen.mp3 import MP3 
from PIL import Image, ImageTk 

def play_music(): 
    if playlist: 
        pygame.mixer.music.load(playlist[current_track]) 
        pygame.mixer.music.play() 
 
def stop_music(): 
    pygame.mixer.music.stop() 
 
def pause_music(): 
    pygame.mixer.music.pause() 
 
def resume_music(): 
    pygame.mixer.music.unpause() 
 
def next_track(): 
    global current_track 
    current_track = (current_track + 1) % len(playlist) 
    play_music() 
 
def add_to_playlist(): 
    file_path = filedialog.askopenfilename( 
        defaultextension=".mp3", filetypes= 
        [("MP3 files", "*.mp3")]) 
     
    if file_path: 
        playlist.append(file_path) 
        playlistbox.insert(END, os.path.basename 
                           (file_path)) 
 
def add_song_multi(): 
    file_paths = filedialog.askopenfilenames( 
        defaultextension=".mp3", filetypes=[ 
            ("MP3 files", "*.mp3")]) 
    for file_path in file_paths: 
        playlist.append(file_path) 
        playlistbox.insert(END,  
                           os.path.basename(file_path)) 
 
    

def set_volume(val): 
    volume = int(val) / 100 
    pygame.mixer.music.set_volume(volume) 
 
def forward_10_seconds(): 
 # Convert milliseconds to seconds 
    current_pos = pygame.mixer.music.get_pos() // 1000  
    new_pos = current_pos + 10 
    pygame.mixer.music.set_pos(new_pos) 
 
def backward_10_seconds(): 
     # Convert milliseconds to seconds 
    current_pos = pygame.mixer.music.get_pos() // 1000  
    new_pos = max(0, current_pos - 10) 
    pygame.mixer.music.set_pos(new_pos) 
 
def shuffle_playlist(): 
    random.shuffle(playlist) 
 
def repeat_track(): 
    if playlist: 
        pygame.mixer.music.load(playlist[current_track]) 
        pygame.mixer.music.play(-1) 
 
def remove_song(): 
    selected_songs = playlistbox.curselection() 
    if selected_songs: 
         # Iterate in reverse order for proper deletion 
        for index in selected_songs[::-1]:  
            playlist.pop(index) 
            playlistbox.delete(index) 
 
def play_previous_track(): 
    global current_track 
    if playlist: 
        current_track = (current_track - 1) % len(playlist) 
        play_music() 
 
            

def set_song_position(val): 
    if playlist: 
        if float(val) > 99:
            fmsg.showerror("Error", 
 "Previous Song was just Finished. Please play another song") 
             # Set the slider back to the maximum value 
            song_slider.set(99)  
        else: 
            song_length = MP3(playlist[current_track]).info.length 
            song_position = int(val) * song_length / 100 
            pygame.mixer.music.set_pos(song_position) 
 
def exit_app(): 
    root.destroy() 
 
def msg(): 
    fmsg.showinfo("About us","""We are students of class 11 
 and this is our Computer Science 
Project Desined by Farhan😎 "A mp3 player"
based on Python and its 
 module named tkinter and pygame""") 
     
def help(): 
    fmsg.showinfo("Help","""Play=Play the music\n 
Stop=Stop the music\n 
Pause=Pause the music at current position and when you play  
it will resume from same position of being paused\n 
Resume=Resume music from paused position\n 
Next Track=Play Next song for you\n 
Play Previous Track=Play the Previous Song\n 
Shuffle=Play music randomlly\n 
Repeat=Repeat the current song\n 
Forword 10 seconds=Forword 10 seconds of music\n 
Backword 10 seconds=Play the 10 seconds position of music\n 
Add to PlayList=Add song in Playlist\n 
Remove song=Remove songs from Playlist """) 
     
# Create the main window 
root = Tk() 
root.title("MUSIC PLAYER") 
root.geometry("49x10") 
root.maxsize(1080,637) 
root.minsize(1080,637) 
root.iconbitmap("i.ico") 
 
 
 
 

 
# Initialize Pygame mixer 
pygame.mixer.init() 
 
# Track list 
playlist = [] 
 
# Current playing track 
current_track = 0 
 
# Create frames 
frame1 = Frame(root, 
               borderwidth=3,relief=GROOVE, bg="black", 
                 highlightthickness=1,highlightbackground="red") 
 
frame2 = Frame(root, borderwidth=3,relief=GROOVE, bg="black", 
                highlightthickness=2,highlightbackground="red") 
 
frame3 = Frame(root, borderwidth=3,relief=GROOVE, bg="black", 
                highlightthickness=1,highlightbackground="red") 
 
frame4 = Frame(root, height=75,borderwidth=3,relief=GROOVE,bg="black", 
                highlightthickness=1,highlightbackground="red") 
 
frame5 = Frame(root, height=75,borderwidth=3,relief=GROOVE,bg="black", 
                highlightthickness=1,highlightbackground="red") 
 
# Place frames on the GUI 
frame1.grid(row=0, column=0, sticky="nw") 
frame2.grid(row=0, column=1) 
frame3.grid(row=1, column=0, columnspan=2, sticky="nsew") 
frame4.grid(row=2, column=0, columnspan=2, sticky="nsew") 
frame5.grid(row=3, column=0, columnspan=2, sticky="nsew") 

img = Image.open("i.png") 
img = ImageTk.PhotoImage(img) 
 
# Create labels 
Label(frame2,text="MUSIC PLAYER",font= 
      "algerian 42 bold",bg="black",fg="white",width=20).grid(padx=133, 
                                                     pady=9) 
 
Label(frame1,image=img).grid(padx=5,pady=5) 
 
Label(frame3,text="Playlist",font= 
      "arial 22 ",bg="black",fg="white").grid(row=2,padx=5,pady=5) 

volume_label = Label(frame5, text="Volume Rocker",  
                     font="arial 11", bg="black", fg="white") 
volume_label.grid(column=13, columnspan=2,padx=10) 
 
# create  playlistbox 
playlistbox = Listbox(frame3, selectmode=MULTIPLE,  
selectbackground="white",selectforeground= 
"black", bg="black",fg="white", width=150, height=9,  
borderwidth=12) 
playlistbox.grid(padx=55, pady=30) 
# length adjuster 
song_slider = Scale(frame4, from_=0, to=100, orient=HORIZONTAL, 
        command=set_song_position,borderwidth=6, bg="black", 
            fg="white", length=970) 
song_slider.set(0)  # Default position 
song_slider.grid(pady=25,padx=30) 
# volume_slider 
volume_slider = Scale(frame5, from_=0, to=200,  
        orient=HORIZONTAL, command=set_volume,  
            borderwidth=6, bg="black", fg="white") 
volume_slider.set(69)  # Default volume 
volume_slider.grid(row=1, column=13, columnspan=2,  
                   pady=5,padx=10) 

# Accessing photos of buttons 219 
pause_button_img = PhotoImage(file="pause.png") 
play_button_img = PhotoImage(file="play.png") 
resume_button_img = PhotoImage(file="resume.png") 
stop_button_img = PhotoImage(file="stop.png") 
shuffle_button_img = PhotoImage(file="shuffle.png") 
forward_10_seconds_img = PhotoImage(file="f10.png") 
backward_10_seconds_img = PhotoImage(file="b10.png") 
repeat_button_img = PhotoImage(file="repeat.png") 
next_button_img = PhotoImage(file="next.png") 
play_previous_button_img = PhotoImage(file="previous.png") 
add_button_img = PhotoImage(file="add.png") 
remove_button_img = PhotoImage(file="remove.png") 

# assignning images and command 242 
pause_button = Button(frame5, image=pause_button_img, 
        borderwidth=5, pady=10, bg="black", command=pause_music) 
play_button = Button(frame5, image=play_button_img, 
         borderwidth=5, pady=10, bg="black", command=play_music) 
resume_button = Button(frame5, image=resume_button_img,  
        borderwidth= 5, pady=10, bg="black", command=resume_music,) 
stop_button = Button(frame5, image=stop_button_img, 
        borderwidth=5, pady=10, bg="black", command=stop_music) 
shuffle_button = Button(frame5, image=shuffle_button_img, 
        borderwidth=5, pady=10, bg="black", command=shuffle_playlist) 
forward_10_seconds1 = Button(frame5, image=forward_10_seconds_img, 
        borderwidth=5, pady=10, bg="black", command=forward_10_seconds) 
backward_10_seconds1 = Button(frame5, image=backward_10_seconds_img, 
        borderwidth= 5, pady=10, bg="black", command=backward_10_seconds) 
repeat_button = Button(frame5, image=repeat_button_img,  
        borderwidth=5, pady=10, bg="black", command=repeat_track) 
next_button = Button(frame5, image=next_button_img, 
        borderwidth= 5, pady=10, bg="black", command=next_track) 
play_previous_button = Button(frame5, image=play_previous_button_img, 
        borderwidth=5, pady=10, bg="black", command=play_previous_track) 
add_button = Button(frame5, image=add_button_img, borderwidth= 
        5, pady=10, bg="black", command=add_to_playlist) 
remove_button = Button(frame5, image=remove_button_img, borderwidth= 
        5, pady=10, bg="black", command=remove_song) 
 
pause_button.grid(row=1, column=6,pady=10,padx=8) 
play_button.grid(row=1, column=7,pady=10,padx=8) 
resume_button.grid(row=1, column=8,pady=10,padx=8) 
stop_button.grid(row=1, column=5,pady=10,padx=8) 
shuffle_button.grid(row=1, column=4,pady=10,padx=8) 
forward_10_seconds1.grid(row=1, column=10,pady=10,padx=8) 
backward_10_seconds1.grid(row=1, column=3,pady=10,padx=8) 
repeat_button.grid(row=1, column=9,pady=10,padx=8) 
next_button.grid(row=1, column=11,pady=10,padx=8) 
play_previous_button.grid(row=1, column=2,pady=10,padx=8) 
add_button.grid(row=1,column=1,pady=10,padx=8) 
remove_button.grid(row=1,column=12,pady=10,padx=8) 

# Create menu 290 
mainmenu = Menu(root) 
# menu 1 
menu1 = Menu(mainmenu, tearoff=0, 
 background="black", foreground="white") 
# sub menu 1 
menu1.add_command(label="Add a Song",  
            command=add_to_playlist) 
# seperator 
menu1.add_separator() 
# sub menu 2 
menu1.add_command(label="Add Multiple Songs", 
                   command=add_song_multi) 
menu1.add_separator() 
# submenu 3 
menu1.add_command(label="Exit", command=exit_app) 
root.config(menu=mainmenu) 
# 1 menu 
mainmenu.add_cascade(label="File", menu=menu1, 
                      background="black") 
 
# menu2  311 
menu2= Menu(mainmenu, tearoff=0, background="black", 
             foreground="white") 
menu2.add_command(label="About us", command=msg) 
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="About", menu=menu2, 
                      background="black") 
 
menu3= Menu(mainmenu, tearoff=0, background="black",  
            foreground="white") 
menu3.add_command(label="Help", command=help) 
root.config(menu=mainmenu) 
mainmenu.add_cascade(label="Help", menu=menu3, 
                      background="black") 
 
# Start the Tkinter event loop 
root.mainloop() 
