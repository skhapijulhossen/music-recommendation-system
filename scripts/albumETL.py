import sys
import requests
import config


class searchAlbum:
    bik=[]
    def __init__(self, from_path: str, to_path: str) -> None:
        self.from_path = from_path
        self.to_path = to_path
        self.access_token = None
    
    def get_id(self,dt):
        return dt['id']
    
    def extract(self, artist: str) -> str:
        url = 'https://api.spotify.com/v1/artists/{0}/albums?limit=50'.format(
            artist)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(self.access_token)
        }
        response = requests.get(
            url=url,
            headers=headers
        )
        try:
            # print("hello")
            data = response.json()
            ans = list(map(self.get_id, data['items']))
            # print(ans)
            with open(config.album_id_store, "w") as my_file:
                __class__.bik.extend(ans)
                my_file.write(str(__class__.bik))
        except:
            pass

    def run(self) -> bool:
        artists = None

        with open(config.artist_id_store, mode='r') as file:
            artists = file.read().split(',').copy()

        # print("fhidofh")
        r=list(map(self.extract, artists))


if __name__ == '__main__':
    """
    required commandline args : 
    Example : python searchETL.py

    """
    Pipeline = searchAlbum(
        from_path=config.artist_id_store,
        to_path=config.album_id_store
    )
    Pipeline.access_token = config.access_token
    Pipeline.run()
