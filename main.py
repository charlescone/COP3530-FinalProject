import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

from knn import Knn
from tfidf import TfIdf

root = tk.Tk()
root.title("CineMatch - Personalized Movie Recommendations")
root.geometry("700x700")
root.resizable(False, False)
root.bind('<Escape>', lambda e, w=root: w.destroy())

# Styling constants
BG_COLOR = "#B22222"
FG_COLOR = "#ffd700"
BUTTON_COLOR = "#ffd700"
LABEL_FONT = ("Strong Sans", 18, "bold")
TEXT_FONT = ("Strong Sans", 12)
ENTRY_FONT = ("Vogue", 12)
BUTTON_FONT = ("Gabba All Caps", 12, "bold")
RADIO_FONT = ("Arial", 10)

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', font=BUTTON_FONT, background=BUTTON_COLOR, foreground=FG_COLOR)
style.configure('TRadiobutton', font=RADIO_FONT, background=BG_COLOR, foreground=FG_COLOR)

root.configure(background=BG_COLOR)

start_time = time.time()
knn_algo = Knn()
print("kNN Data processing time %0.3f" % (time.time() - start_time))
start_time = time.time()
tfidf_algo = TfIdf()
print("Tf-Idf Data processing time %0.3f" % (time.time() - start_time))


def raise_frame(frame):
    frame.tkraise()


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creating frames for each page
page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

for frame in (page1, page2, page3):
    frame.configure(bg=BG_COLOR)
    frame.grid(row=0, column=0, sticky='news')

# Nested frames page 1
top_frame1 = tk.Frame(page1)
top_frame1.configure(bg=BG_COLOR)
center_frame1 = tk.Frame(page1)
center_frame1.configure(bg=BG_COLOR)
top_frame1.pack(side=tk.TOP, fill=tk.X)
center_frame1.pack(expand=True)

# Nested frames page 2
top_frame2 = tk.Frame(page2)
top_frame2.configure(bg=BG_COLOR)
center_frame2 = tk.Frame(page2)
center_frame2.configure(bg=BG_COLOR)
top_frame2.pack(side=tk.TOP, fill=tk.X)
center_frame2.pack(expand=True)

# Nested frames page 3
top_frame3 = tk.Frame(page3)
top_frame3.configure(bg=BG_COLOR)
center_frame3 = tk.Frame(page3)
center_frame3.configure(bg=BG_COLOR)
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
label2 = tk.Label(center_frame1,
                  text="There are two possible ways\nto find the best movie match \naccording to your likes.\n"
                       "\nChoose one of the options\nfrom the menu on the top left\ncorner to get started", bg=BG_COLOR,
                  fg=FG_COLOR, font=LABEL_FONT)
label2.grid(row=3, column=0)


# Add content to page2
def enter_pressed_knn():
    movie_input = entry_val_knn.get()
    knn_start_time = time.time()
    recs = knn_algo.return_recommendation(movie_input)
    print("kNN runtime: %0.3f" % (time.time() - knn_start_time))
    recommendations_knn_label.configure(
        text="1. " + recs[0] + "\n2. " + recs[1] + "\n3. " + recs[2] + "\n4. " + recs[3] + "\n5. " + recs[4] + "\n6. " +
             recs[5] + "\n7. " + recs[6] + "\n8. " + recs[7] + "\n9. " + recs[8] + "\n10. " + recs[9])


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
label_KNN = tk.Label(center_frame2,
                     text="Input a movie title in the box below\nthat has similar genre and style\nas the movie you "
                          "would like to watch.\n",
                     bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_KNN.grid(row=1, column=2)
button_knn = tk.Button(center_frame2, text="ENTER", command=enter_pressed_knn, width=20, height=2, bg=BUTTON_COLOR,
                       fg=BG_COLOR,
                       font=BUTTON_FONT)
button_knn.grid(row=3, column=2)
entry_val_knn = StringVar()
entry = tk.Entry(center_frame2, textvariable=entry_val_knn, font=ENTRY_FONT)
entry.grid(row=2, column=2)
recommendations_knn_label = tk.Label(center_frame2, text="", bg=BG_COLOR, fg=FG_COLOR, font=TEXT_FONT)
recommendations_knn_label.grid(row=4, column=2)


# Add content to page3
def enter_pressed_tfidf():
    movie_input = entry_val_tf.get()
    knn_start_time = time.time()
    recs = tfidf_algo.get_movie_recommendations(movie_input)
    print("Tf-Idf runtime: %0.3f" % (time.time() - knn_start_time))
    recommendations_tf_label.configure(
        text="1. " + recs[0] + "\n2. " + recs[1] + "\n3. " + recs[2] + "\n4. " + recs[3] + "\n5. " + recs[4] + "\n6. " +
             recs[5] + "\n7. " + recs[6] + "\n8. " + recs[7] + "\n9. " + recs[8] + "\n10. " + recs[9])


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
label_TF = tk.Label(center_frame3,
                    text="Input a movie title in the box below\nthat has similar genre and style\nas the movie you "
                         "would like to watch.\n",
                    bg=BG_COLOR, fg=FG_COLOR, font=LABEL_FONT)
label_TF.grid(row=1, column=2)
button_tf = tk.Button(center_frame3, text="ENTER", command=enter_pressed_tfidf, width=20, height=2, bg=BUTTON_COLOR,
                      fg=BG_COLOR,
                      font=BUTTON_FONT)
button_tf.grid(row=3, column=2)
entry_val_tf = StringVar()
entryTF = tk.Entry(center_frame3, textvariable=entry_val_tf, font=ENTRY_FONT)
entryTF.grid(row=2, column=2)
recommendations_tf_label = tk.Label(center_frame3, text="", bg=BG_COLOR, fg=FG_COLOR, font=TEXT_FONT)
recommendations_tf_label.grid(row=4, column=2)

radio_var = tk.StringVar(value="knn")

# Start with Homepage
raise_frame(page1)

root.mainloop()
