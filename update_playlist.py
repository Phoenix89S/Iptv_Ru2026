import requests

def fetch_m3u_sources(sources):
    channels = []
    for source in sources:
        response = requests.get(source)
        if response.status_code == 200:
            channels.extend(parse_m3u(response.text))
        else:
            print(f"Failed to fetch from {source}")
    return channels

def parse_m3u(m3u_content):
    lines = m3u_content.splitlines()
    channels = []
    for i in range(len(lines)):
        if lines[i].startswith('#EXTINF'):
            channel_info = lines[i]
            channel_url = lines[i + 1]
            channels.append((channel_info, channel_url))
    return channels

def create_playlist(channels):
    playlist_lines = []
    for channel_info, channel_url in channels:
        playlist_lines.append(f"{channel_info}\n{channel_url}")
    return "\n".join(playlist_lines)

def main():
    m3u_sources = [
        "http://example.com/source1.m3u",
        "http://example.com/source2.m3u",
    ]
    
    channels = fetch_m3u_sources(m3u_sources)
    complete_playlist = create_playlist(channels)

    with open("complete_playlist.m3u", "w") as playlist_file:
        playlist_file.write(complete_playlist)
        print("Playlist created successfully.")

if __name__ == "__main__":
    main()