import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import *
from knn import Knn
from tfidf import TfIdf

from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

root = tk.Tk()
root.title("CineMatch")
root.geometry("500x500")
root.resizable(False, False)
root.bind('<Escape>', lambda e, w=root: w.destroy())

knn_algo = Knn()
tfidf_algo = TfIdf()


def enterpressed():
    selected_option = radio_var.get()

    if selected_option == "tfidf":
        print(entryVal.get() + " tfidf")
        # print(type(entryVal.get()))
        recs = tfidf_algo.get_movie_recommendations(entryVal.get(), top_n=10)
        for recommendation in recs:
           print(tfidf_algo.get_movie_title(recommendation))
    else:
        print(entryVal.get() + " knn")
        knn_algo.return_recommendation(entryVal.get())


button = tk.Button(root, text="Enter", command=enterpressed, width=40, height=3)
label = tk.Label(root, text="Enter a Movie Title")
entryVal = StringVar()
entry = tk.Entry(root, textvariable=entryVal)
radio_var = tk.StringVar(value="knn")
radio_button_knn = tk.Radiobutton(root, text="kNN Algorithm", variable=radio_var, value="knn")
radio_button_tfidf = tk.Radiobutton(root, text="Tf-Idf", variable=radio_var, value="tfidf")


label.pack()
entry.pack()
button.pack()
radio_button_knn.pack()
radio_button_tfidf.pack()

root.mainloop()
