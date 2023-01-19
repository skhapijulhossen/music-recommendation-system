import pyorc


class IO:
    def write(self, path: str, rows, schema) -> bool:
        with open(path, mode='wb') as file:
            with pyorc.Writer(file, schema=schema,
                              struct_repr=pyorc.StructRepr.DICT, compression=pyorc.CompressionKind.SNAPPY) as writer:
                writer.writerows(
                    rows
                )

    def read(self, path: str):
        with open(path, mode='rb') as file:
            reader = pyorc.Reader(file)
            return reader.read()
