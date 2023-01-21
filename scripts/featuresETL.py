import sys
from pprint import pprint
from orcIO import IO
import requests


class getAudioFeatureService:
    """
    Service to get audio feature.
    """

    def __init__(self, track_ids: str) -> None:
        self.track_ids = track_ids

    def run(self, access_token: str) -> list:
        io = IO()
        ids = '%2C'.join([row[0] for row in io.read(self.track_ids)])

        try:
            url = f'https://api.spotify.com/v1/audio-features?ids={ids}'
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f'Bearer {access_token}'
            }
            response = requests.get(
                url=url,
                headers=headers
            )
            if response.ok:
                return response.json()['audio_features']
        except Exception as e:
            return e


if __name__ == '__main__':
    """
    required commandline args : 
    Example : python featuresETL.py source=./track_ids.orc dest=./track_features.orc access_token=BQBaeCzbfTIY0npFsW3c36WYznmXab0ChptOEC1pKczRTkWIg3-hCmSmqVxUx3ZK4NgKtA6Z88U9ie2yPHjmOpIf9rJ21YJ75j9N9nxO9yEnZtc-JEt2YWZSVqZyRyocsOBnUtclVykxwoAereqVlUH3ZvwXtGSEWR6o5ZGmCC7Z485h2W1_iqYAMwFY8qCxlss

    """
    kwargs = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
    service = getAudioFeatureService(track_ids=kwargs['track_ids'])
    data = service.run(access_token=kwargs['access_token'])

    # writing to raw datastore
    io = IO()
    io.write(
        path='../rawDataStore/tracks_features.orc',
        rows=data,
        schema="struct<acousticness:float,analysis_url:string,danceability:float,energy:float,id:string,instrumentalness:float,key:float,liveness:float,loudness:float,mode:float,speechiness:float,tempo:float,time_signature:float,track_href:string,type:string,uri:string,valence:float>"
    )
    print("Finished!")
