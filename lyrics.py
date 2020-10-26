
import lyricsgenius as lg 


file = open("auto_.txt", "w")  # File to write lyrics to
genius = lg.Genius('btUspYNxfEDmb0NA_1Gsxvlste8GxwE52pOFk-7J2hVh_DzCXgLxLzqCZw0R3XIs',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

while True:
    artist = input("Enter artist: ")
    song = input("Enter song: ")


    song = genius.search_song(song, artist)
    print(song.lyrics)

    flag = input("Do you want to look up another song? (Yes/No)")
    if flag == "No":
        print("Exiting Search Engine")
        break

