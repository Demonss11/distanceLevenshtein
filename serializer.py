import json

class Serializer:

    def __init__(self):
        pass

    def _serializeApp(self):
        cls._setLastDatetime()
        with open(cls._fileForSerializing, "w") as write_file:
            json.dump(cls._lastDatetime, write_file)

    def _setLastDatetime(self):
        cls._lastDatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _deserializeApp(self):
        with open(cls._fileForSerializing, "r") as read_file:
            cls._lastDatetime = json.load(read_file)