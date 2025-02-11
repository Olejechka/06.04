import json
tracks = [
    {"genre": "Synthwave", "artist": "Mr.Kitty", "year": 2014, "title": "After Dark"},
    {"genre": "Synthwave", "artist": "Mr.Kitty", "year": 2015, "title": "Rats"},
    {"genre": "Synthwave", "artist": "Mr.Kitty", "year": 2016, "title": "Pathogen"},
    {"genre": "Synthwave", "artist": "The Midnight", "year": 2016, "title": "Vampires"},
    {"genre": "Synthwave", "artist": "The Midnight", "year": 2017, "title": "Crystalline"},
    {"genre": "Synthwave", "artist": "The Midnight", "year": 2018, "title": "America 2"},
    {"genre": "Synthwave", "artist": "Carpenter Brut", "year": 2015, "title": "Turbo Killer"},
    {"genre": "Synthwave", "artist": "Carpenter Brut", "year": 2016, "title": "Inferno Galore"},
    {"genre": "Synthwave", "artist": "Carpenter Brut", "year": 2017, "title": "Cheerleader Effect"},

    {"genre": "Rock", "artist": "Queen", "year": 1975, "title": "Bohemian Rhapsody"},
    {"genre": "Rock", "artist": "Queen", "year": 1976, "title": "Somebody to Love"},
    {"genre": "Rock", "artist": "Queen", "year": 1977, "title": "We Will Rock You"},
    {"genre": "Rock", "artist": "Nirvana", "year": 1991, "title": "Smells Like Teen Spirit"},
    {"genre": "Rock", "artist": "Nirvana", "year": 1992, "title": "Come As You Are"},
    {"genre": "Rock", "artist": "Nirvana", "year": 1993, "title": "Heart-Shaped Box"},
    {"genre": "Rock", "artist": "AC/DC", "year": 1980, "title": "Back in Black"},
    {"genre": "Rock", "artist": "AC/DC", "year": 1981, "title": "For Those About to Rock"},
    {"genre": "Rock", "artist": "AC/DC", "year": 1982, "title": "Let's Get It Up"},

    {"genre": "Pop", "artist": "Michael Jackson", "year": 1982, "title": "Billie Jean"},
    {"genre": "Pop", "artist": "Michael Jackson", "year": 1983, "title": "Beat It"},
    {"genre": "Pop", "artist": "Michael Jackson", "year": 1984, "title": "Thriller"},
    {"genre": "Pop", "artist": "Madonna", "year": 1984, "title": "Like a Virgin"},
    {"genre": "Pop", "artist": "Madonna", "year": 1985, "title": "Material Girl"},
    {"genre": "Pop", "artist": "Madonna", "year": 1986, "title": "Papa Don't Preach"},
    {"genre": "Pop", "artist": "Taylor Swift", "year": 2014, "title": "Shake It Off"},
    {"genre": "Pop", "artist": "Taylor Swift", "year": 2015, "title": "Blank Space"},
    {"genre": "Pop", "artist": "Taylor Swift", "year": 2016, "title": "Wildest Dreams"},

    {"genre": "Hip-Hop", "artist": "Eminem", "year": 2002, "title": "Lose Yourself"},
    {"genre": "Hip-Hop", "artist": "Eminem", "year": 2003, "title": "Without Me"},
    {"genre": "Hip-Hop", "artist": "Eminem", "year": 2004, "title": "Mockingbird"},
    {"genre": "Hip-Hop", "artist": "Kanye West", "year": 2010, "title": "Power"},
    {"genre": "Hip-Hop", "artist": "Kanye West", "year": 2011, "title": "All of the Lights"},
    {"genre": "Hip-Hop", "artist": "Kanye West", "year": 2013, "title": "Black Skinhead"},
    {"genre": "Hip-Hop", "artist": "Jay-Z", "year": 2003, "title": "99 Problems"},
    {"genre": "Hip-Hop", "artist": "Jay-Z", "year": 2004, "title": "Encore"},
    {"genre": "Hip-Hop", "artist": "Jay-Z", "year": 2009, "title": "Empire State of Mind"},

    {"genre": "Post-Punk", "artist": "Сова", "year": 2018, "title": "Временные рамки"},
    {"genre": "Post-Punk", "artist": "Сова", "year": 2019, "title": "Восход"},
    {"genre": "Post-Punk", "artist": "Сова", "year": 2020, "title": "Тени прошлого"},

    {"genre": "Indie", "artist": "MGMT", "year": 2007, "title": "Kids"},
    {"genre": "Indie", "artist": "MGMT", "year": 2010, "title": "Flash Delirium"},
    {"genre": "Indie", "artist": "MGMT", "year": 2013, "title": "Alien Days"},
    {"genre": "Indie", "artist": "MGMT", "year": 2018, "title": "Little Dark Age"},

    {"genre": "Soundtrack", "artist": "Nicholas Britell", "year": 2022, "title": "Andor: Main Title Theme"},
    {"genre": "Soundtrack", "artist": "Nicholas Britell", "year": 2022, "title": "Andor: Niamos!"},
    {"genre": "Soundtrack", "artist": "Nicholas Britell", "year": 2022, "title": "Andor: Ending Theme"},
    {"genre": "Soundtrack", "artist": "Hans Zimmer", "year": 2010, "title": "Time"},
    {"genre": "Soundtrack", "artist": "Hans Zimmer", "year": 2014, "title": "Cornfield Chase"},
    {"genre": "Soundtrack", "artist": "Hans Zimmer", "year": 2020, "title": "No Time for Caution"},

    {"genre": "Soundtrack", "artist": "John Williams", "year": 1977, "title": "Star Wars Main Theme"},
    {"genre": "Soundtrack", "artist": "John Williams", "year": 1981, "title": "Raiders March"},
    {"genre": "Soundtrack", "artist": "John Williams", "year": 1993, "title": "Jurassic Park Theme"},

    {"genre": "Soundtrack", "artist": "Howard Shore", "year": 2001, "title": "The Shire"},
    {"genre": "Soundtrack", "artist": "Howard Shore", "year": 2002, "title": "Gollum's Song"},
    {"genre": "Soundtrack", "artist": "Howard Shore", "year": 2003, "title": "The Return of the King"},

    {"genre": "Indie", "artist": "Arctic Monkeys", "year": 2006, "title": "I Bet You Look Good on the Dancefloor"},
    {"genre": "Indie", "artist": "Arctic Monkeys", "year": 2013, "title": "Do I Wanna Know?"},
    {"genre": "Indie", "artist": "Arctic Monkeys", "year": 2018, "title": "Four Out of Five"},

    {"genre": "Indie", "artist": "The Strokes", "year": 2001, "title": "Last Nite"},
    {"genre": "Indie", "artist": "The Strokes", "year": 2006, "title": "You Only Live Once"},
    {"genre": "Indie", "artist": "The Strokes", "year": 2013, "title": "One Way Trigger"},

    {"genre": "Indie", "artist": "Florence + The Machine", "year": 2009, "title": "Dog Days Are Over"},
    {"genre": "Indie", "artist": "Florence + The Machine", "year": 2015, "title": "Ship to Wreck"},
    {"genre": "Indie", "artist": "Florence + The Machine", "year": 2018, "title": "Hunger"},

    {"genre": "Post-Punk", "artist": "Joy Division", "year": 1979, "title": "Disorder"},
    {"genre": "Post-Punk", "artist": "Joy Division", "year": 1980, "title": "Love Will Tear Us Apart"},
    {"genre": "Post-Punk", "artist": "Joy Division", "year": 1981, "title": "Ceremony"},

    {"genre": "Post-Punk", "artist": "The Cure", "year": 1985, "title": "Close to Me"},
    {"genre": "Post-Punk", "artist": "The Cure", "year": 1989, "title": "Lovesong"},
    {"genre": "Post-Punk", "artist": "The Cure", "year": 1992, "title": "Friday I'm in Love"},

    {"genre": "Post-Punk", "artist": "Molchat Doma", "year": 2017, "title": "Клетка"},
    {"genre": "Post-Punk", "artist": "Molchat Doma", "year": 2018, "title": "Судно (Борис Рыжий)"},
    {"genre": "Post-Punk", "artist": "Molchat Doma", "year": 2020, "title": "Ответа нет"},

    {"genre": "Alternative", "artist": "Muse", "year": 2003, "title": "Time Is Running Out"},
    {"genre": "Alternative", "artist": "Muse", "year": 2006, "title": "Starlight"},
    {"genre": "Alternative", "artist": "Muse", "year": 2012, "title": "Madness"},

    {"genre": "Alternative", "artist": "Placebo", "year": 1998, "title": "Pure Morning"},
    {"genre": "Alternative", "artist": "Placebo", "year": 2003, "title": "The Bitter End"},
    {"genre": "Alternative", "artist": "Placebo", "year": 2009, "title": "For What It's Worth"},

    {"genre": "Alternative", "artist": "Coldplay", "year": 2002, "title": "The Scientist"},
    {"genre": "Alternative", "artist": "Coldplay", "year": 2008, "title": "Viva La Vida"},
    {"genre": "Alternative", "artist": "Coldplay", "year": 2014, "title": "A Sky Full of Stars"}
]


def get_genres():
    return list(set(track["genre"] for track in tracks))

def get_artists_by_genre(genre):
    return list(set(track["artist"] for track in tracks if track["genre"] == genre))

def get_years_by_artist(artist):
    return list(set(track["year"] for track in tracks if track["artist"] == artist))

def recommend_tracks(genre, artist, year):
    return [track for track in tracks if
            track["genre"] == genre and track["artist"] == artist and track["year"] == year]

def save_recommendations_to_json(recommended_tracks, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(recommended_tracks, f, ensure_ascii=False, indent=4)

def main():
    genres = get_genres()
    print("Выберите жанр:")
    print(", ".join(genres))
    selected_genre = input("Ввод: ")

    artists = get_artists_by_genre(selected_genre)
    print("Выберите исполнителя:")
    print(", ".join(artists))
    selected_artist = input("Ввод: ")

    years = get_years_by_artist(selected_artist)
    print("Выберите год выпуска треков:")
    print(", ".join(map(str, years)))
    selected_year = int(input("Ввод: "))

    recommended_tracks = recommend_tracks(selected_genre, selected_artist, selected_year)
    print("Рекомендованные треки:")
    for track in recommended_tracks:
        print(f"{track['title']} by {track['artist']} ({track['year']})")

    save_recommendations_to_json(recommended_tracks, 'recommendations.json')

if __name__ == "__main__":
    main()
