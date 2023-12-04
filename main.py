import tkinter as tk
import time

from tkinter import ttk
from tkinter import PhotoImage
from knn import Knn
from tfidf import TfIdf


class KnnAlgo:
    def return_recommendation(self, movie_name):
        return ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5", "Movie 6", "Movie 7", "Movie 8", "Movie 9",
                "Movie 10"]


class TfIdfAlgo:
    def get_movie_recommendations(self, movie_name, top_n=10):
        return ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5", "Movie 6", "Movie 7", "Movie 8",
                "Movie 9", "Movie 10"]


root = tk.Tk()
root.title("CineMatch")
root.geometry("700x700")
root.resizable(False, False)
root.bind('<Escape>', lambda e, w=root: w.destroy())

# Styling constants
BG_COLOR = "#B22222"
FG_COLOR = "#ffd700"
BUTTON_COLOR = "#ffd700"
LABEL_FONT = ("Strong Sans", 18, "bold")
ENTRY_FONT = ("Signature", 12)
BUTTON_FONT = ("Gabba All Caps", 12, "bold")
RADIO_FONT = ("Arial", 10)

# styling
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=BUTTON_FONT, background=BUTTON_COLOR, foreground=FG_COLOR)
style.configure('TRadiobutton', font=RADIO_FONT, background=BG_COLOR, foreground=FG_COLOR)
root.configure(bg=BG_COLOR)

# Getting time for comparison
start_time = time.time()
knn_algo = Knn()
print("kNN Data processing time %0.3f" % (time.time() - start_time))
start_time = time.time()
tfidf_algo = TfIdf()
print("Tf-Idf Data processing time %0.3f" % (time.time() - start_time))


# Enter button functionality
def enter_pressed():
    selected_option = radio_var.get()

    if selected_option == "tfidf":
        print(entryVal.get() + " tfidf")
        recs = tfidf_algo.get_movie_recommendations(entryVal.get(), top_n=10)
        first_label.config(text="1. " + tfidf_algo.get_movie_title(recs[0]))
        second_label.config(text="2. " + tfidf_algo.get_movie_title(recs[1]))
        third_label.config(text="3. " + tfidf_algo.get_movie_title(recs[2]))
        fourth_label.config(text="4. " + tfidf_algo.get_movie_title(recs[3]))
        fifth_label.config(text="5. " + tfidf_algo.get_movie_title(recs[4]))
        sixth_label.config(text="6. " + tfidf_algo.get_movie_title(recs[5]))
        seventh_label.config(text="7. " + tfidf_algo.get_movie_title(recs[6]))
        eighth_label.config(text="8. " + tfidf_algo.get_movie_title(recs[7]))
        ninth_label.config(text="9. " + tfidf_algo.get_movie_title(recs[8]))
        tenth_label.config(text="10. " + tfidf_algo.get_movie_title(recs[9]))
    else:
        print(entryVal.get() + " knn")
        recs = knn_algo.return_recommendation(entryVal.get())
        first_label.config(text="1. " + recs[0])
        second_label.config(text="2. " + recs[1])
        third_label.config(text="3. " + recs[2])
        fourth_label.config(text="4. " + recs[3])
        fifth_label.config(text="5. " + recs[4])
        sixth_label.config(text="6. " + recs[5])
        seventh_label.config(text="7. " + recs[6])
        eighth_label.config(text="8. " + recs[7])
        ninth_label.config(text="9. " + recs[8])
        tenth_label.config(text="10. " + recs[9])


# Initialize button and title
button = tk.Button(root, text="ENTER", command=enter_pressed, width=20, height=2, bg=BUTTON_COLOR, fg=BG_COLOR,
                   font=BUTTON_FONT)
title_label = tk.Label(root, text="Enter a Movie Title", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
entryVal = tk.StringVar()
entry = ttk.Entry(root, textvariable=entryVal, font=ENTRY_FONT)

# Create Radiobuttons
radio_var = tk.StringVar()
radio_button_knn = ttk.Radiobutton(root, text="Knn Algorithm", variable=radio_var, value="knn")
radio_button_tfidf = ttk.Radiobutton(root, text="Tf-Idf", variable=radio_var, value="tfidf")

# Blank labels for Top 10
first_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
second_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
third_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
fourth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
fifth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
sixth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
seventh_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
eighth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
ninth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)
tenth_label = tk.Label(root, text="", bg=BG_COLOR, fg=FG_COLOR, font=ENTRY_FONT)


# Packing all tkinter objects to be viewed
title_label.pack(pady=(20, 10))
entry.pack(pady=10)
radio_button_knn.pack()
radio_button_tfidf.pack()
button.pack(pady=10)
first_label.pack(pady=5)
second_label.pack(pady=5)
third_label.pack(pady=5)
fourth_label.pack(pady=5)
fifth_label.pack(pady=5)
sixth_label.pack(pady=5)
seventh_label.pack(pady=5)
eighth_label.pack(pady=5)
ninth_label.pack(pady=5)
tenth_label.pack(pady=5)

root.mainloop()
