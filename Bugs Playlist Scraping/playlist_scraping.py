from bs4 import BeautifulSoup

with open("playlist.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

track_titles = [element['title'] for element in soup.find_all(class_='tracktitle') if 'title' in element.attrs]
artist_names = [element['title'] for element in soup.find_all(class_='artistname') if 'title' in element.attrs]

if artist_names:
    artist_names.pop(0)

track_artist_pairs = [f"{track} - {artist}" for track, artist in zip(track_titles, artist_names)]

with open("track_artist_pairs.txt", "w", encoding="utf-8") as file:
    for pair in track_artist_pairs:
        file.write(pair + "\n")

print("track_artist_pairs.txt 파일이 저장되었습니다.")