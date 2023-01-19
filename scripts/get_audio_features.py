import os
import sys
from pprint import pprint
from write_to_orc import IO


class getAudioFeatureService:
    """
    Service to get audio feature.
    """

    def __init__(self, track_ids: str) -> None:
        self.track_ids = track_ids

    def run(self, access_token: str) -> list:
        io = IO()
        ids = '%2C'.join([ row[0] for row in io.read(self.track_ids) ])
        
        try:
            return os.system(
                'curl -X "GET" "https://api.spotify.com/v1/audio-features?ids={1}"\
                     -H "Accept: application/json" -H "Content-Type: application/json"\
                         -H "Authorization: Bearer {0}"'.format(access_token, ids)
            )
        except Exception as e:
            return e


if __name__ == '__main__':
    """
    required commandline args : 
    Example : python get_audio_features.py track_ids=./track_ids.orc store=./track_features.orc access_token=BQBaeCzbfTIY0npFsW3c36WYznmXab0ChptOEC1pKczRTkWIg3-hCmSmqVxUx3ZK4NgKtA6Z88U9ie2yPHjmOpIf9rJ21YJ75j9N9nxO9yEnZtc-JEt2YWZSVqZyRyocsOBnUtclVykxwoAereqVlUH3ZvwXtGSEWR6o5ZGmCC7Z485h2W1_iqYAMwFY8qCxlss

    """
    kwargs = { arg.split('=')[0]:arg.split('=')[1] for arg in sys.argv[1:] }
    service = getAudioFeatureService(track_ids=kwargs['track_ids'])
    data = service.run(access_token=kwargs['access_token'])    
    pprint(data)
    

