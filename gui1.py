
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from new import *

# from tkinter import *
# Explicit imports to satisfy Flake8
from PIL import Image, ImageTk

from tkinter import Tk, Canvas, Entry, Text, Button, OptionMenu, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\SPARK\assets\frame1")
ASSETS_PATH1 = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\SPARK\assets\frame0")
ASSETS_PATH2 = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\SPARK\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assets1(path: str) -> Path:
    return ASSETS_PATH1 / Path(path)

def relative_to_assets2(path: str) -> Path:
    return ASSETS_PATH2 / Path(path)

def home_page(window):
    canvas = Canvas(
        window,
        bg = "#00416C",
        height = 643,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        9.9998779296875,
        19.999996181503548,
        1450.0000895209125,
        1044.0,
        fill="#00416C",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets1("image_1.png"))
    image_1 = canvas.create_image(
        612.0,
        321.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets1("image_2.png"))
    image_2 = canvas.create_image(
        609.0,
        118.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets1("image_3.png"))
    image_3 = canvas.create_image(
        1252.0,
        134.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets1("image_4.png"))
    image_4 = canvas.create_image(
        1328.0,
        134.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets1("image_5.png"))
    image_5 = canvas.create_image(
        192.0,
        231.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets1("image_6.png"))
    image_6 = canvas.create_image(
        94.0,
        228.0,
        image=image_image_6
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets1("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            chords_page(window)
            },
        relief="flat"
    )
    button_1.place(
        x=27.0,
        y=277.0,
        width=150.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets1("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            songs_page(window)
            },
        relief="flat"
    )
    button_2.place(
        x=27.0,
        y=333.0,
        width=150.0,
        height=41.0
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets1("image_7.png"))
    image_7 = canvas.create_image(
        103.0,
        415.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets1("image_8.png"))
    image_8 = canvas.create_image(
        775.6622314453125,
        375.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets1("image_9.png"))
    image_9 = canvas.create_image(
        486.0,
        197.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets1("image_10.png"))
    image_10 = canvas.create_image(
        450.0,
        375.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets1("image_11.png"))
    image_11 = canvas.create_image(
        129.0,
        118.0,
        image=image_image_11
    )
    window.resizable(False, False)
    window.mainloop()
    
def chords_page(window):
    canvas = Canvas(
    window,
    bg = "#00416C",
    height = 643,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        9.9998779296875,
        19.999996181503548,
        1450.0000895209125,
        1044.0,
        fill="#00416C",
        outline="")
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        614.0,
        331.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1252.0,
        134.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1328.0,
        134.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        192.0,
        294.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            home_page(window)
            },
        relief="flat"
    )
    button_1.place(
        x=27.0,
        y=207.0,
        width=150.0,
        height=41.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        99.0,
        291.0,
        image=image_image_5
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            songs_page(window)
            },
        relief="flat"
    )
    button_2.place(
        x=27.0,
        y=333.0,
        width=150.0,
        height=41.0
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        103.0,
        415.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        369.0,
        113.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        129.0,
        118.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        411.0,
        173.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        390.0,
        223.0,
        image=image_image_10
    )

    input_entry = Entry(canvas)
    input_entry.place(x=522, y=207, width=283, height=33)
    input_entry.configure(bg="#D9D9D9", bd=0)
    set_input_entry(input_entry)
    songs = ["C", "D", "G", "A", "Em"]
    set_input_songs(songs)
    selected_song = tk.StringVar(window, )
    selected_song.set(songs[0])
    set_selected_song(selected_song)


    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=input,
        relief="flat"
    )
    button_4.place(
        x=823.0,
        y=207.0,
        width=88.0,
        height=33.0
    )

    button_image_hover_4 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_4_hover(e):
        button_4.config(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        button_4.config(
            image=button_image_4
        )

    button_4.bind('<Enter>', button_4_hover)
    button_4.bind('<Leave>', button_4_leave)

    new_size = (220, 250)

    image_image_11 = [ImageTk.PhotoImage(Image.open(f"chords/{song}.png").resize(new_size)) for song in songs]
    image_11 = tk.Label(
        canvas,
        image=image_image_11[0]
    )
    image_11.place(
        x=482.0,
        y=415.0,
        anchor="center"
    )
    
    print(image_11)
    
    set_images(image_image_11)
    set_image_label(image_11)

    dropdown = OptionMenu(canvas, selected_song, *songs, command=select_chord)
    dropdown.config(bg="#D9D9D9", fg="#000000", font=("Poppins Medium", 16))
    dropdown["menu"].config(bg="#D9D9D9", fg="#000000", font=("Poppins Medium", 16))

    # Place the OptionMenu widget
    dropdown.place(x=522, y=156, anchor="nw", width=100, height=40)

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_image_6_stop = PhotoImage(
        file=relative_to_assets("button_6_stop.png"))
    
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            record_audio_chord(button_image_6, button_image_6_stop)
            },
        relief="flat"
    )
    button_6.place(
        x=680.0,
        y=321.0,
        width=200.0,
        height=64.0
    )
    
    set_record_button(button_6)

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png")
    )   
    image_12 = tk.Label(
        canvas,
        image=image_image_12
    )
    image_12.place(
        x=512.0,
        y=321.0,
        anchor="center"
    )
    
    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13.png")
    )   
    image_13 = tk.Label(
        canvas,
        image=image_image_13
    )
    image_13.place(
        x=512.0,
        y=321.0,
        anchor="center"
    )


    
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            process_file_chord(image_12, image_13)
        },
        relief="flat"
    )
    button_3.place(
        x=680.0,
        y=423.0,
        width=200.0,
        height=58.0
    )

    button_image_hover_3 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_3_hover(e):
        button_3.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        button_3.config(
            image=button_image_3
        )

    button_3.bind('<Enter>', button_3_hover)
    button_3.bind('<Leave>', button_3_leave)
    image_12.place_forget()
    image_13.place_forget()

    window.resizable(False, False)
    window.mainloop()
    
def songs_page(window):


    canvas = Canvas(
        window,
        bg = "#00416C",
        height = 643,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        9.9998779296875,
        19.999996181503548,
        1450.0000895209125,
        1044.0,
        fill="#00416C",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets2("image_1.png"))
    image_1 = canvas.create_image(
        614.0,
        331.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets2("image_2.png"))
    image_2 = canvas.create_image(
        1252.0,
        134.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets2("image_3.png"))
    image_3 = canvas.create_image(
        1328.0,
        134.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets2("image_4.png"))
    image_4 = canvas.create_image(
        200.0,
        357.0,
        image=image_image_4
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets2("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            home_page(window)
        },
        relief="flat"
    )
    button_1.place(
        x=27.0,
        y=207.0,
        width=150.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets2("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            chords_page(window)
        },
        relief="flat"
    )
    button_2.place(
        x=22.0,
        y=265.0,
        width=178.0,
        height=52.0
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets2("image_5.png"))
    image_5 = canvas.create_image(
        95.0,
        355.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets2("image_6.png"))
    image_6 = canvas.create_image(
        103.0,
        415.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets2("image_7.png"))
    image_7 = canvas.create_image(
        369.0,
        113.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets2("image_8.png"))
    image_8 = canvas.create_image(
        129.0,
        118.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets2("image_9.png"))
    image_9 = canvas.create_image(
        411.0,
        173.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets2("image_10.png"))
    image_10 = canvas.create_image(
        390.0,
        223.0,
        image=image_image_10
    )

    input_entry = Entry(canvas)
    input_entry.place(x=522, y=207, width=283, height=33)
    input_entry.configure(bg="#D9D9D9", bd=0)
    set_input_entry(input_entry)
    songs = ["Rain Rain Go Away"]
    set_input_songs(songs)
    selected_song = tk.StringVar(window, )
    selected_song.set(songs[0])
    set_selected_song(selected_song)

    button_image_3 = PhotoImage(
        file=relative_to_assets2("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=input,
        relief="flat"
    )
    button_3.place(
        x=823.0,
        y=207.0,
        width=88.0,
        height=33.0
    )

    button_image_hover_3 = PhotoImage(
        file=relative_to_assets2("button_hover_1.png"))

    def button_3_hover(e):
        button_3.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        button_3.config(
            image=button_image_3
        )

    button_3.bind('<Enter>', button_3_hover)
    button_3.bind('<Leave>', button_3_leave)

    dropdown = OptionMenu(canvas, selected_song, *songs, command=select_song)
    dropdown.config(bg="#D9D9D9", fg="#000000", font=("Poppins Medium", 16))
    dropdown["menu"].config(bg="#D9D9D9", fg="#000000", font=("Poppins Medium", 16))
    # Place the OptionMenu widget
    dropdown.place(x=522, y=153, anchor="nw", width=300, height=40)


    player = TkinterVideo(master=canvas)
    player.load(media_path)

    player.place(x=374, y=254, width=492, height=277)


    set_player(player)
    
    image_image_12 = PhotoImage(
        file=relative_to_assets2("image_12.png")
    )   
    image_12 = tk.Label(
        canvas,
        image=image_image_12
    )
    image_12.place(
        x=512.0,
        y=321.0,
        anchor="center"
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets2("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            process_file(image_12)
        },
        relief="flat"
    )
    button_5.place(
        x=682.0,
        y=546.0,
        width=131.25,
        height=42.0
    )

    button_image_hover_5 = PhotoImage(
        file=relative_to_assets2("button_hover_3.png"))

    def button_5_hover(e):
        button_5.config(
            image=button_image_hover_5
        )
    def button_5_leave(e):
        button_5.config(
            image=button_image_5
        )

    button_5.bind('<Enter>', button_5_hover)
    button_5.bind('<Leave>', button_5_leave)

    button_image_6 = PhotoImage(
        file=relative_to_assets2("button_6.png"))
    button_image_6_stop = PhotoImage(
        file=relative_to_assets2("button_6_stop.png"))
    
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: {
            record_audio(button_image_6, button_image_6_stop)
            },
        relief="flat"
    )
    button_6.place(
        x=414.0,
        y=545.0,
        width=142.0,
        height=45.439998626708984
    )
    
    set_record_button(button_6)
    image_12.place_forget()

    window.resizable(False, False)
    window.mainloop()
