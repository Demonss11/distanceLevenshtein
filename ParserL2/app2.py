from datetime import datetime
import json

from ParserL2.ParserLists import ParserLists


class ParserApp2:

    _statusApp = []
    _fileForSerializing = r"C:\Users\Demonss\PycharmProjects\parserLists\ParserL2\ParserAppMemory.json"
    _lastDatetime = None

    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ParserApp2, cls).__new__(cls)
        return cls.instance

    def run(self):
        try:
            self._main()
        except Exception as e:
            self._logReport(repr(e))

    def _main(self):
        self._deserializeApp()
        if self._isReadyToRun():
            ParserLists().run()
            self._serializeApp()
        self._chainReports()

    def _chainReports(self):
        self._logReport(ParserLists().getStatusApp())

    @classmethod
    def _logReport(cls, report="Hold"):
        cls._statusApp.append(report)

    @classmethod
    def getStatusApp(cls):

        return "parserApp: " + str(cls._statusApp)

    @classmethod
    def _isReadyToRun(cls):
        if cls._isEligibleDate():
            return True
        return False

    @classmethod
    def _isEligibleDate(cls):
        if cls._lastDatetime is not None:
            timeFromLastRunning = datetime.today() - datetime.strptime(cls._lastDatetime, '%Y-%m-%d %H:%M:%S')
            isMinutePassed = (timeFromLastRunning.seconds / 60) > 1
            return isMinutePassed
        return True

    @classmethod
    def _serializeApp(cls):
        cls._setLastDatetime()
        with open(cls._fileForSerializing, "w") as write_file:
            json.dump(cls._lastDatetime, write_file)

    @classmethod
    def _setLastDatetime(cls):
        cls._lastDatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def _deserializeApp(cls):
        with open(cls._fileForSerializing, "r") as read_file:
            cls._lastDatetime = json.load(read_file)


if __name__ == '__main__':
    ParserApp2().run()
    print(ParserApp2().getStatusApp())
