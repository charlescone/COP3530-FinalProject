import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from knn import Knn
from tfidf import TfIdf

from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

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

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', font=BUTTON_FONT, background=BUTTON_COLOR, foreground=FG_COLOR)
style.configure('TRadiobutton', font=RADIO_FONT, background=BG_COLOR, foreground=FG_COLOR)

root.configure(bg=BG_COLOR)

# knn_algo = Knn()
# tfidf_algo = TfIdf()


def enterpressed():
    selected_option = radio_var.get()

    if selected_option == "tfidf":
        print(entryVal.get() + " tfidf")
        print(type(entryVal.get()))
        # recs = tfidf_algo.get_movie_recommendations(entryVal.get(), top_n=10)
        # for recommendation in recs:
           # print(tfidf_algo.get_movie_title(recommendation))
    else:
        print(entryVal.get() + " knn")
        # knn_algo.return_recommendation(entryVal.get())


button = tk.Button(root, text="ENTER", command=enterpressed, width=20, height=2, bg=BUTTON_COLOR, fg=BG_COLOR,
                   font=BUTTON_FONT)
label = tk.Label(root, text="Enter a Movie Title", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
entryVal = StringVar()
entry = tk.Entry(root, textvariable=entryVal, font=ENTRY_FONT)
radio_var = tk.StringVar(value="knn")
radio_button_knn = tk.Radiobutton(root, text="Knn Algorithm", variable=radio_var, value="knn", bg=BG_COLOR,
                                  fg="#FFFFFF", font=BUTTON_FONT)
radio_button_tfidf = tk.Radiobutton(root, text="Tf-Idf", variable=radio_var, value="tfidf", bg=BG_COLOR,
                                    fg="#FFFFFF", font=BUTTON_FONT)

label.pack(pady=(20, 10))
entry.pack(pady=10)
radio_button_knn.pack()
radio_button_tfidf.pack()
button.pack(pady=10)

root.mainloop()
