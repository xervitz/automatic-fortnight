class ParseMessages:
    @staticmethod
    def Parse(message):
        print(message)

    @staticmethod
    def int_from_bytes(xbytes: bytes) -> int:
        return int.from_bytes(xbytes, 'big')
