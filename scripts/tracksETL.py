import json
import sys
from orcIO import IO


class TracksPipeline:
    """
    Pipeline to get Tracks from JSON Album  to ORC
    """

    def __init__(self, source: str) -> None:
        self.source = source
        self.tracks = []
        self.items = []

    def extract(self) -> None:
        with open(self.source, mode='r') as f:
            self.items = json.load(f)['items'].copy()

    def get_for_multiple_artists(self, item: dict) -> None:
        itemsTemp = item.copy()
        for item in item['artists']:
            itemsTemp['artists'] = item['id']
            itemsTemp['external_urls'] = item['external_urls']['spotify']
            self.tracks.append(itemsTemp)

    def transform(self) -> None:
        for item in self.items:
            self.get_for_multiple_artists(item)

    def load(self, destination: str) -> None:
        # writing to raw datastore
        io = IO()
        io.write(
            destination,
            rows=self.tracks,
            schema="struct<artists:string,disc_number:int,duration_ms:int,explicit:boolean,external_urls:string,href:string,id:string,is_local:boolean,is_playable:boolean,name:string,preview_url:string,track_number:int,type:string,uri:string>"
        )

    def run(self, destination) -> bool:
        self.extract()
        self.transform()
        self.load(destination=destination)


if __name__ == '__main__':
    """
    required commandline args : 
    Example : python tracksETL.py source=../albumStore/ArijitSingh_album11.json dest=../rawDataStore/tracksDB.orc

    """
    kwargs = {arg.split('=')[0]: arg.split('=')[1] for arg in sys.argv[1:]}
    pipeline = TracksPipeline(source=kwargs['source'])
    pipeline.run(destination=kwargs['dest'])
