import pyorc


class IO:
    def write(self, path: str, rows) -> bool:
        with open(path, mode='wb') as file:
            with pyorc.Writer(file, "struct<track_id:string>") as writer:
                writer.writerows(rows)

    def read(self, path: str):
        with open(path, mode='rb') as file:
            reader = pyorc.Reader(file)
            return reader.read()
