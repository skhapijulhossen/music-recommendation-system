import os
import sys
from pprint import pprint


class getAudioFeatureService:
    """
    Service to get audio feature.
    """

    def __init__(self, track_ids: str) -> None:
        self.track_ids = track_ids

    def run(self, access_token: str) -> list:
        try:
            return os.system(
                'curl -X "GET" "https://api.spotify.com/v1/audio-features?ids=56zZ48jdyY2oDXHVnwg5Di%2C56zZ48jdyY2oDXHVnwg5Di"\
                     -H "Accept: application/json" -H "Content-Type: application/json"\
                         -H "Authorization: Bearer {0}"'.format(access_token)
            )
        except Exception as e:
            return e


if __name__ == '__main__':
    service = getAudioFeatureService('...')
    data = service.run(access_token='BQBrYrSYA03Pi-7tPGioJy8BESMiWm2Lfhx_ov-iH8w5JHlpH08y6FFiNvdnzXNqBXlQA7qmkuDvVu1dRMAit1XowRDgb3Penq_vrhelFJdbeOOer8HRpGEtYeR9Vryx4WoW01gRh632Q6YBbR3Xj7E96K_Dw-EN06pUdtk8_3Da0DeelUlaG1FaRVD_AvVyg9s')
    pprint(data)
