import pyorc


class IO:
    def write(self, path: str, rows) -> bool:
        with open(path, mode='wb') as file:
            with pyorc.Writer(file, "struct<track_id:string>") as writer:
                writer.write(rows)

    def read(self, path: str):
        with open(path, mode='rb') as file:
            with pyorc.Reader(file) as reader:
                return reader.read()
