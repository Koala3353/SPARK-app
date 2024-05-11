from musicai_sdk import MusicAiClient
import tkinter as tk
from tkinter import filedialog, font
import PIL.Image, PIL.ImageTk as Imagetk
import requests
import json
import time
import sounddevice as sd
import numpy as np
import wave
import pathlib
import soundfile as sf
from tkVideoPlayer import TkinterVideo
import winsound
from tkinter import ttk
import tkinter as tk
from tkinter import font
from PIL import Image
import os


S = False
index = 1
global master
start_time = None
client = MusicAiClient(api_key='e1582db2-6ef0-4bb7-a1cd-f08c76125a12')
app_info = client.get_application_info()
print('Application Info:', app_info)
media_path = "video/Rain Rain Go Away.mp4"
audio_path = "audio/Rain Rain Go Away.wav"

def process_audio_file(file_path, api_key):
    try:
        audio_url = client.upload_file(file_path=file_path)
        print('File Url:', audio_url)
        # Create Job
        workflow_params = {
            'inputUrl': audio_url,
        }
        create_job_info = client.create_job(job_name='Chords Website', workflow_id='chords-detection',
                                            params=workflow_params)
        job_id = create_job_info['id']
        print('Job Created:', job_id)

        # Wait for job to complete
        job_info = client.wait_for_job_completion(job_id)
        print('Job Status:', job_info['status'])

        # Get job info
        job_info = client.get_job(job_id=job_id)
        print('Job Status:', job_info['status'])

        chords_json_url = job_info['result']['chordsJSON']

        chords_json_response = requests.get(chords_json_url)
        chords_json_response.raise_for_status()
        chords_data = chords_json_response.json()

        result = chords_data

        return result
    except Exception as e:
        print("Error:", e)


def matrify(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    matrix = []
    for entry in data:
        matrix.append([entry['start'], entry['end'], entry['chord_simple_pop']])

    return matrix

def process_chordfile(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    if data is not None:
        for entry in data:
            if entry['chord_simple_pop'] != "None":
                if entry['chord_simple_pop'] != "N":
                    return entry['chord_simple_pop']
    else:
        print("No data in JSON file")
        return None


def record_audio(button_image_6, button_image_6_stop):
    global S
    if S == False:
        record_button.config(image=button_image_6_stop)
        S = True
        record_audio_start()

    else:
        record_button.config(image=button_image_6)
        S = False
        record_audio_stop();


def record_audio_start():
    global media_path, audio_path
    player.load(media_path)

    player.play()
    winsound.PlaySound(audio_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    global recording, file_path, start_time
    fs = 44100  # Sample rate
    seconds = 700  # Maximum duration of recording
    print(pathlib.Path(__file__).parent.resolve())
    print("Recording started...")
    start_time = time.time()
    print(start_time)
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    print('a')
    strpath = "recorded_audio" + str(index) + ".wav"
    file_path = pathlib.Path(__file__).parent.resolve() / strpath
    print(file_path)


def record_audio_stop():
    # player.play()
    global recording, file_path, start_time
    sd.stop()
    sd.wait()

    duration = time.time() - start_time
    time.sleep(3)
    print(f"Recording stopped and saved to {file_path}")

    recording_trimmed = recording[:int(duration * 44100)]
    sf.write(file_path, recording_trimmed, 44100)
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)
    player.pause()
    winsound.PlaySound(None, winsound.SND_PURGE)
    
# chords
def record_audio_chord(button_image_6, button_image_6_stop):
    global S
    if S == False:
        record_button.config(image=button_image_6_stop)
        S = True
        record_audio_start_chord()
    else:
        record_button.config(image=button_image_6)
        S = False
        record_audio_stop_chord()


def record_audio_start_chord():    
    global recording, file_path, start_time
    fs = 44100  # Sample rate
    seconds = 700  # Maximum duration of recording
    print(pathlib.Path(__file__).parent.resolve())
    print("Recording started...")
    start_time = time.time()
    print(start_time)
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
    print('a')
    strpath = "recorded_audio" + str(index) + ".wav"
    file_path = pathlib.Path(__file__).parent.resolve() / strpath
    print(file_path)


def record_audio_stop_chord():
    # player.play()
    global recording, file_path, start_time
    sd.stop()
    sd.wait()

    duration = time.time() - start_time
    time.sleep(3)
    print(f"Recording stopped and saved to {file_path}")

    recording_trimmed = recording[:int(duration * 44100)]
    sf.write(file_path, recording_trimmed, 44100)
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)
    winsound.PlaySound(None, winsound.SND_PURGE)


def compare_matrices(matrix1, matrix2):

    total_same_time = 0
    wrong_chords = []  # List to store the chords that were not matched correctly

    for entry1 in matrix1:
        for entry2 in matrix2:
            start1, end1, chord1 = entry1
            start2, end2, chord2 = entry2

            # Calculate the overlapping time duration
            overlap_start = max(start1, start2)
            overlap_end = min(end1, end2)

            # If there's an overlap and chords are the same
            if overlap_start < overlap_end:
                if chord1 == chord2:
                    total_same_time += overlap_end - overlap_start
                else:
                    wrong_chords.append((chord1, chord2))  # Store the original and identified chord

    return total_same_time, wrong_chords


def select_song(song):
    global j, media_path, media, audio_path
    print("Selected Song:", song)
    j = f"{song}.json"
    media_path = f"video/{song}.mp4"
    audio_path = f"audio/{song}.wav"
    print(media_path)
    print(audio_path)
    
def select_chord(chord):
    global j, media_path, media, audio_path
    print("Selected Song:", chord)
    j = f"{chord}.json"
    media_path = f"video/{chord}.mp4"
    audio_path = f"audio/{chord}.wav"
    print(media_path)
    print(audio_path)
    
    # Update the global song variable
    global selected_song
    selected_song.set(chord)

    # Update the image label
    global image_label
    global images
    global songs
    song_index = songs.index(chord)
    image_label.configure(image=images[song_index])
    image_label.image = images[song_index]  # Keep a reference to prevent garbage collection

import threading

def process_file(image_12):
    image_12.place(
        x=512.0,
        y=321.0,
        anchor="center"
    )
    # Run the long-running task in a separate thread
    threading.Thread(target=long_running_task, args=(image_12,)).start()
    
def process_file_chord(image_12):
    image_12.place(
        x=512.0,
        y=321.0,
        anchor="center"
    )
    

    # Run the long-running task in a separate thread
    threading.Thread(target=long_running_task_chord, args=(image_12,)).start()

def disable_event():
    pass  # do nothing when the user tries to close the window

def long_running_task_chord(image_12):
    # os.remove("n.json")
    # os.mkdir("n.json")
    api_key = "e1582db2-6ef0-4bb7-a1cd-f08c76125a12"
    file_path = input_entry.get()
    print(file_path)
    result = process_audio_file(file_path, api_key)
    out_file = open("n.json", "w")
    json.dump(result, out_file)
    out_file.close()
    print(result)
    m = process_chordfile("n.json")
    out_file.close()
    selected_chord = selected_song.get()
    print(selected_song.get())
    print(m)
    # Create a Text widget 
    

    master = tk.Tk()
    master.geometry("600x70")  # Set the size of the window
    master.title("Results")
    
    # Create a Text widget
    results_text = tk.Text(master, bg="#00416C", font=("Poppins Medium", 16), foreground="white")
    # Place the Text widget at the center
    results_text.place(relx=0.5, rely=0.5, anchor='center')
    # Configure a tag for centered text
    results_text.tag_configure("center", justify='center')

    # Add the "center" tag to all the text

    # Make sure the window stays on top
    master.attributes('-topmost', True)

    if selected_chord == m:
        results_text.insert(tk.END, m + ' ', 'black')
        results_text.insert(tk.END, "\nCongratulations! You correctly played the chord!")

    else:
        results_text.insert(tk.END, m + ' ', 'red')
        results_text.insert(tk.END, "\nPractice more and try again!")

    # Configure the red tag to change the text color to red
    results_text.tag_config('red', foreground='#FF474C')
    results_text.tag_add("center", 1.0, "end")

    image_12.place_forget()

    # Pack the Text widget
    results_text.pack()

    master.mainloop()

def long_running_task(image_12):
    api_key = "e1582db2-6ef0-4bb7-a1cd-f08c76125a12"
    file_path = input_entry.get()
    result = process_audio_file(file_path, api_key)
    out_file = open("n.json", "w")
    result_json = json.dump(result, out_file)
    print(result_json)
    out_file.close()
    m = matrify(f"{selected_song.get()}.json")
    n = matrify("n.json")
    print(n)
    total_same_time, wrong_chords = compare_matrices(m, n)
    # Create a Text widget
    

    master = tk.Tk()
    master.geometry("600x350")  # Set the size of the window
    master.title("Results")
    
    # Create a Text widget
    results_text = tk.Text(master, bg="#00416C", font=("Poppins Medium", 16), foreground="white")

    # Place the Text widget at the center

    # Make sure the window stays on top
    master.attributes('-topmost', True)

    chords = [8, 2, 1, 1]
    pattern = [4, 4, 2, 2, ]
    output_chords = ["C", "D", "G", "C"]
    output = []

    from itertools import groupby

    # Remove consecutive duplicates from wrong_chords based on the first element of each tuple
    wrong_chords = [next(group) for key, group in groupby(wrong_chords, key=lambda x: x[0])]

    # Create a dictionary from wrong_chords for faster lookup
    wrong_chords_dict = dict(wrong_chords)
    print(wrong_chords_dict)

    # Loop through output_chords
    for i, chord in enumerate(output_chords):
        # If the chord is in wrong_chords, replace it with wrong_chord
        if chord in wrong_chords_dict:
            output_chords[i] = wrong_chords_dict[chord]

    # Repeat each chord by the corresponding count in chords
    output = [chord for chord, count in zip(output_chords, chords) for _ in range(count)]

    # Create an iterator for the pattern
    pattern_iter = iter(pattern)

    # Get the first number from pattern
    chords_per_line = next(pattern_iter)

    # Create a counter for the chords
    counter = 0

    # Insert the chords into the Text widget
    for chord in output:
        if chord in wrong_chords_dict.values():
            # If the chord is wrong, insert it with a red tag
            results_text.insert(tk.END, chord + ' ', 'red')
        else:
            # If the chord is correct, insert it without a tag
            results_text.insert(tk.END, chord + ' ')

        counter += 1
        if counter == chords_per_line:
            # If the counter is equal to chords_per_line, insert a newline and get the next number from pattern
            results_text.insert(tk.END, '\n')
            counter = 0
            try:
                chords_per_line = next(pattern_iter)
            except StopIteration:
                # If pattern is exhausted, default to 1 chord per line
                chords_per_line = 1
        elif chords_per_line == 2 and counter % 2 != 0:
            # If chords_per_line is 2 and the counter is even, insert a space
            results_text.insert(tk.END, '    ')

    # Configure the red tag to change the text color to red
    results_text.tag_config('red', foreground='#FF474C')

    image_12.place_forget()

    # Pack the Text widget
    results_text.pack()

    if total_same_time > 0.75 * songTimes[selected_song.get()]:
        print("Congratulations!")
        results_text.insert(tk.END, "\nCongratulations! Rating 100%\n")
    else:
        print("practice more and try again! ")
        score = int((total_same_time / songTimes[selected_song.get()]) * 100)
        results_text.insert(tk.END, "\nPractice more and try again! Rating " + str(score) + "%\n")
    master.mainloop()


def input():
    input_path = filedialog.askopenfilename()
   
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_path)


def create_chords_screen():

    # Your existing code to create the song screen goes here
    master = tk.Tk()
    master.geometry("1000x620")
    master.configure(bg='lightblue')

    logo_image = Imagetk.PhotoImage(file="logo.webp")

    # Use a custom font for labels and buttons
    custom_font = font.Font(size=14)

    # Set a background color for the frames
    left_frame = tk.Frame(master, bg='lightblue')
    top_frame = tk.Frame(left_frame, bg='lightblue')
    bottom_frame = tk.Frame(left_frame, bg='lightblue')
    global right_frame
    right_frame = tk.Frame(master, bg='lightblue')

    logo_label = tk.Label(top_frame, image=logo_image, bg='lightblue')

    global input_path
    input_path = tk.Label(top_frame, text="Input File Path:", bg='lightblue', font=custom_font)
    global input_entry
    input_entry = tk.Entry(top_frame, text="", width=40, font=custom_font)
    browse1 = tk.Button(top_frame, text="Browse", command=input, font=custom_font)

    begin_button = tk.Button(bottom_frame, text='Begin!', command=process_file_chord, font=custom_font)
    global song
    global songs
    songs = ["C", "D", "G", "A", "Em"]

    global selected_song
    selected_song = tk.StringVar(master, )
    selected_song.set(songs[0])
    song_label = tk.Label(top_frame, text="Select a Chord to Learn:", bg='lightblue', font=custom_font)
    song_dropdown = tk.OptionMenu(top_frame, selected_song, *songs, command=select_chord)
    new_size = (600, 700)

    global record_button
    record_button = tk.Button(bottom_frame, text="Start Recording", command=record_audio_chord, font=custom_font)
    global images
    images = [Imagetk.PhotoImage(Image.open(f"chords/{song}.png").resize(new_size)) for song in songs]
    left_frame.pack(side=tk.LEFT, anchor="nw")
    right_frame.pack(side=tk.RIGHT, anchor="ne")
    global image_label

    image_label = tk.Label(right_frame, image=images[0], bg='lightblue')
    image_label.pack()

    top_frame.pack(anchor="nw")
    bottom_frame.pack(anchor="sw")

    logo_label.pack(pady=5)
    input_path.pack(pady=5)
    input_entry.pack(pady=5)
    browse1.pack(pady=5)
    song_label.pack(pady=5, side=tk.LEFT)
    song_dropdown.pack(pady=5, side=tk.LEFT)

    record_button.pack(pady=5)

    begin_button.pack(pady=20, fill=tk.X)

    master.mainloop()
    pass

def set_input_entry(input):
    global input_entry
    input_entry = input
    
def set_input_path(input):
    global input_path
    input_path = input

def set_input_song(input):
    global song
    input_song = input
    
def set_input_songs(input):
    global songs
    songs = input
    
def set_selected_song(input):
    global selected_song
    selected_song = input
    
def set_record_button(input):
    global record_button
    record_button = input
    
def set_images(input):
    global images
    images = input
    
def set_image_label(input):
    global image_label
    image_label = input
    
def set_player(input):
    global player
    player = input
    
global songTimes
songTimes = {
    "Rain Rain Go Away": 16,
}

def create_song_screen():

    # Your existing code to create the song screen goes here
    master = tk.Tk()
    master.geometry("1000x620")
    master.configure(bg='lightblue')

    logo_image = Imagetk.PhotoImage(file="logo.webp")

    # Use a custom font for labels and buttons
    custom_font = font.Font(size=14)

    # Set a background color for the frames
    left_frame = tk.Frame(master, bg='lightblue')
    top_frame = tk.Frame(left_frame, bg='lightblue')
    bottom_frame = tk.Frame(left_frame, bg='lightblue')
    right_frame = tk.Frame(master, bg='lightblue')

    logo_label = tk.Label(top_frame, image=logo_image, bg='lightblue')

    global input_path
    input_path = tk.Label(top_frame, text="Input File Path:", bg='lightblue', font=custom_font)
    global input_entry
    input_entry = tk.Entry(top_frame, text="", width=40, font=custom_font)
    browse1 = tk.Button(top_frame, text="Browse", command=input, font=custom_font)

    begin_button = tk.Button(bottom_frame, text='Begin!', command=process_file, font=custom_font)
    songs = ["Rain Rain Go Away"]
    global songTimes
    songTimes = {
        "Rain Rain Go Away": 16,
    }
    global selected_song
    selected_song = tk.StringVar(master, )
    selected_song.set(songs[0])
    song_label = tk.Label(top_frame, text="Select a Song:", bg='lightblue', font=custom_font)
    song_dropdown = tk.OptionMenu(top_frame, selected_song, *songs, command=select_song)

    global record_button
    record_button = tk.Button(bottom_frame, text="Start Recording", command=record_audio, font=custom_font)

    left_frame.pack(side=tk.LEFT, anchor="nw")
    right_frame.pack(side=tk.RIGHT, anchor="ne")

    global player
    player = TkinterVideo(master=master)
    player.load(media_path)  # Replace "path_to_video_file.mp4" with your video file
    player.pack(fill="both", expand=True)
    player.set_size((711, 400))

    top_frame.pack(anchor="nw")
    bottom_frame.pack(anchor="sw")

    logo_label.pack(pady=5)
    input_path.pack(pady=5)
    input_entry.pack(pady=5)
    browse1.pack(pady=5)
    song_label.pack(pady=5, side=tk.LEFT)
    song_dropdown.pack(pady=5, side=tk.LEFT)

    record_button.pack(pady=5)

    begin_button.pack(pady=20, fill=tk.X)

    master.mainloop()

