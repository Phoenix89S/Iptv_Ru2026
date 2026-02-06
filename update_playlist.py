import requests
import m3u8

def fetch_playlist(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return response.text


def merge_playlists(playlist1, playlist2):
    # Parse the playlists
    m3u_playlist1 = m3u8.loads(playlist1)
    m3u_playlist2 = m3u8.loads(playlist2)

    # Combine the playlists, taking unique segments only
    combined_segments = {segment.uri: segment for segment in m3u_playlist1.segments}
    combined_segments.update({segment.uri: segment for segment in m3u_playlist2.segments})

    # Create a new m3u8 object
    merged_playlist = m3u8.M3U8()
    merged_playlist.segments.extend(combined_segments.values())

    return merged_playlist.dumps()


if __name__ == '__main__':
    url1 = 'https://smolnp.github.io/IPTVru//IPTVru.m3u'
    url2 = 'https://raw.githubusercontent.com/Domk04/RusskiIPTV/main/my_list.iptvcat.com.m3u8'

    playlist1 = fetch_playlist(url1)
    playlist2 = fetch_playlist(url2)
    merged_playlist = merge_playlists(playlist1, playlist2)

    # Save merged playlist to a file
    with open('merged_playlist.m3u8', 'w') as f:
        f.write(merged_playlist)  
    print("Merged playlist saved as 'merged_playlist.m3u8'"))