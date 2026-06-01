## creating a songs playlist


# create account 
user = input("Enter the username: ").split()

# create a empty playlist
playlist = []

while True:
    print("1. Add songs")
    print("2.view playlist")
    print("Remove song")
    print("Exit")

    chioce = input("Enter the your chioce: ")

    if chioce == "1":
        song = input("Enter song name: ")
        playlist.append(song)
        print("Song added! ")
    elif chioce == "2":
        print("\nPlaylist: ")
        for song in playlist:
            print(song)

    elif chioce == "3":
        song = input("Enter the song to be removed: ")

        if song in playlist:
            playlist.remove(song)
            print("Song remove!")
        else:
            print("Song not found!")
    elif chioce == "4":
        print("GOODBYE!!!!  ")

        break
    else:

        print("invalid choice! ")