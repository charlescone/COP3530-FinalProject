import tkinter as tk
import time
from tkinter import *
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

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', font=BUTTON_FONT, background=BUTTON_COLOR, foreground=FG_COLOR)
style.configure('TRadiobutton', font=RADIO_FONT, background=BG_COLOR, foreground=FG_COLOR)

root.configure(bg=BG_COLOR)

knn_algo = Knn()
tfidf_algo = TfIdf()

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


def raise_frame(frame):
    frame.tkraise()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating frames for each page
page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='news')

# Nested frames page 1
top_frame1 = tk.Frame(page1)
center_frame1 = tk.Frame(page1)
top_frame1.pack(side=tk.TOP, fill=tk.X)
center_frame1.pack(expand=True)

# Nested frames page 2
top_frame2 = tk.Frame(page2)
center_frame2 = tk.Frame(page2)
top_frame2.pack(side=tk.TOP, fill=tk.X)
center_frame2.pack(expand=True)

# Nested frames page 3
top_frame3 = tk.Frame(page3)
center_frame3 = tk.Frame(page3)
top_frame3.pack(side=tk.TOP, fill=tk.X)
center_frame3.pack(expand=True)

# Add content page 1

# Configure grid rows and columns for expansion in center_frame1
for i in range(4):
    center_frame1.columnconfigure(i, weight=1)
    center_frame1.rowconfigure(i, weight=1)

# Top buttons for page1
tk.Button(top_frame1, text='Homepage', command=lambda: raise_frame(page1)).pack(side=tk.LEFT)
tk.Button(top_frame1, text='Knn Algorithm', command=lambda: raise_frame(page2)).pack(side=tk.LEFT)
tk.Button(top_frame1, text='Tf-Idf Algorithm', command=lambda: raise_frame(page3)).pack(side=tk.LEFT)

# Centered content for page1
label = tk.Label(center_frame1, text="Welcome to CineMatch!\n", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label.grid(row=0, column=0)
label2 = tk.Label(center_frame1, text="There are two possible ways\nto find the best movie match \naccording to your likes.\n"
                              "\nChoose one of the options\nfrom the menu on the top left\ncorner to get started", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label2.grid(row=3, column=0)


# Add content to page2

# Configure grid rows and columns for expansion in center_frame1
for i in range(4):
    center_frame2.columnconfigure(i, weight=1)
    center_frame2.rowconfigure(i, weight=1)

# Top buttons for page2
tk.Button(top_frame2, text='Knn Algorithm', command=lambda: raise_frame(page2)).pack(side=tk.LEFT)
tk.Button(top_frame2, text='Go to Homepage', command=lambda: raise_frame(page1)).pack(side=tk.LEFT)
tk.Button(top_frame2, text='Tf-Idf Algorithm', command=lambda: raise_frame(page3)).pack(side=tk.LEFT)

# Centered content for page2
label_KNN_title = tk.Label(center_frame2, text="KNN Algorithm\n", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_KNN_title.grid(row=0, column=2)
label_KNN = tk.Label(center_frame2, text="Input a movie title in the box below\nthat has similar genre and style\nas the movie you would like to watch.\n", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_KNN.grid(row=1, column=2)
button_knn = tk.Button(center_frame2, text="ENTER", command=enterpressed, width=20, height=2, bg=BUTTON_COLOR, fg=BG_COLOR,
                   font=BUTTON_FONT)
button_knn.grid(row = 3, column = 2)
entryVal = StringVar()
entry = tk.Entry(center_frame2, textvariable=entryVal, font=ENTRY_FONT)
entry.grid(row = 2, column = 2)

# Add content to page3

# Configure grid rows and columns for expansion in center_frame3
for i in range(4):
    center_frame3.columnconfigure(i, weight=1)
    center_frame3.rowconfigure(i, weight=1)

# Top buttons for page3
tk.Button(top_frame3, text='Tf-Idf Algorithm', command=lambda: raise_frame(page3)).pack(side=tk.LEFT)
tk.Button(top_frame3, text='Go to Homepage', command=lambda: raise_frame(page1)).pack(side=tk.LEFT)
tk.Button(top_frame3, text='Knn Algorithm', command=lambda: raise_frame(page2)).pack(side=tk.LEFT)

# Centered content for page3
label_TF_title = tk.Label(center_frame3, text="TF-IDF Algorithm\n", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_TF_title.grid(row=0, column=2)
label_TF = tk.Label(center_frame3, text="Input a movie title in the box below\nthat has similar genre and style\nas the movie you would like to watch.\n", bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_TF.grid(row=1, column=2)
button_tf = tk.Button(center_frame3, text="ENTER", command=enterpressed, width=20, height=2, bg=BUTTON_COLOR, fg=BG_COLOR,
                   font=BUTTON_FONT)
button_tf.grid(row = 3, column = 2)
entryTF = StringVar()
entry2 = tk.Entry(center_frame3, textvariable=entryTF, font=ENTRY_FONT)
entry2.grid(row = 2, column = 2)


radio_var = tk.StringVar(value="knn")


# Start with Homepage
raise_frame(page1)


root.mainloop()
