import sys
import requests
import config


class searchArtist:

    def __init__(self, from_path: str, to_path: str) -> None:
        self.from_path = from_path
        self.to_path = to_path
        self.access_token = None

    def extract(self, artist: str) -> str:
        url = 'https://api.spotify.com/v1/search'
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(self.access_token)
        }
        params = {
            "q": artist,
            "type": 'artist',
            "limit": 1
        }
        response = requests.get(
            url=url,
            params=params,
            headers=headers
        )
        return response.json()['artists']['items'][0]['id']

    def run(self) -> bool:
        artists = None
        with open(config.artist_name_store, mode='r') as file:
            artists = file.read().split(',').copy()

        artist_ids = tuple(
            map(
                self.extract, artists
            )
        )
        artist_ids = ','.join(artist_ids)
        with open(config.artist_id_store, mode='w') as file:
            file.write(',')
            file.write(artist_ids)


if __name__ == '__main__':
    """
    required commandline args : 
    Example : python searchETL.py

    """
    Pipeline = searchArtist(
        from_path=config.artist_name_store,
        to_path=config.artist_id_store
    )
    Pipeline.access_token = config.access_token
    Pipeline.run()
