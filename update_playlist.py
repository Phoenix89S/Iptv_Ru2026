import requests

# URLs of the IPTV channels
iptv_urls = [
    'https://smolnp.github.io/IPTVru//IPTVru.m3u',
    'https://raw.githubusercontent.com/Domk04/RusskiIPTV/main/my_list.iptvcat.com.m3u8'
]

# Function to fetch channels from a given URL

def fetch_channels(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        return []

# Fetch channels from all URLs
combined_channels = set()
for url in iptv_urls:
    channels = fetch_channels(url)
    combined_channels.update(channels)

# Remove duplicates and save to playlist.m3u
with open('playlist.m3u', 'w') as f:
    f.write('\n'.join(combined_channels))
