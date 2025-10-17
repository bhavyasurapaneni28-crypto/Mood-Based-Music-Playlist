import pandas as pd
import webbrowser

def recommend_song(mood):
    df = pd.read_csv("data/songs.csv")
    filtered = df[df["Mood"].str.lower() == mood.lower()]
    if filtered.empty:
        print("No songs found for this mood.")
        return
    song = filtered.sample().iloc[0]
    print(f"Recommended: {song['Song']}")
    webbrowser.open(song['Link'])
