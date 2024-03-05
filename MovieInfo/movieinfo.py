import requests
from customtkinter import *

def get_movie_info(title):
    api_key = "9516de6e" 
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    movie_data = response.json()
    return movie_data

def split_text(text, width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    if current_line:
        lines.append(current_line)
    return "\n".join(lines)

def display_movie_info(movie_info):
    if movie_info.get("Response") == "True":
        title = f"Title: {movie_info['Title']}"
        year = f"Year: {movie_info['Year']}"
        genre = f"Genre: {movie_info['Genre']}"
        plot = f"Plot:\n{split_text(movie_info['Plot'], 70)}"  # Adjust width as needed
        imdb_rating = f"IMDB Rating: {movie_info['imdbRating']}"
        rotten_rating = f"Rotten Tomatoes Rating: {movie_info['Ratings'][1]['Value'] if len(movie_info['Ratings']) > 1 else 'N/A'}"
        
        info_str = "\n".join([title, year, genre, plot, imdb_rating, rotten_rating])
        
        label = CTkLabel(app, text=info_str)  
        label.pack()
    else:
        CTkTextbox.showerror("Error", "Movie not found.")

def search_movie():
    movie_title = entry.get()
    movie_info = get_movie_info(movie_title)
    display_movie_info(movie_info)

app = CTk()
app.title("Movie Information")

label = CTkLabel(app, text="Enter the title of the movie:")
label.pack()

app.geometry("600x400")

app.resizable(False, False)

entry = CTkEntry(app)
entry.pack()

button = CTkButton(app, text="Search", command=search_movie, width=350)  # Adjust width as needed
button.pack(side="bottom", pady=10, ipady=20)  # Adjust vertical padding (ipady) as needed

app.mainloop()
