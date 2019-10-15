class ParserLists:
    __slots__ = ('_dataParts', '_rows')

    _statusApp = 'Hold'

    def __init__(self):
        self._dataParts = ['part1',
                          [
                              {'data11': '11'},
                              {'data12': '12'},
                              {'data12': '13'},
                            ],
                          'part1',
                          [
                              {'data11': '11'},
                              {'data12': '12'},
                          ],
                          'part2',
                          [
                              {'data11': '11'},
                              {'data12': '12'},
                          ]
                          ]
        self._rows = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ParserLists, cls).__new__(cls)
        return cls.instance

    def run(self):
        try:
           self._mainLoop()
        except Exception as e:
            self._logReport(repr(e))

    def _mainLoop(self):
        self._runApp()

    def _runApp(self):
        self._runParser(self._dataParts)
        self._logReport()

    def _runParser(self, dParts=[], row=[]):
        for part in dParts:
            row = row if str(part).find('part') != 0 else []
            result = self._getElementFromRow(part, row)
            self._appendResultToRow(result)
        #print(self.h)
        self._printList()

    def _getElementFromRow(self, dataPart, row):
        if isinstance(dataPart, str):
            return self._getStrPart(dataPart)
        if isinstance(dataPart, list):
            return self._parserFromList(dataPart, row)
        if isinstance(dataPart, dict):
            return self._parserFromDict(dataPart)
        else:
            return self._errorFunc()

    def _getStrPart(self, part):
        return part

    def _parserFromList(self, part, row):
        return self._runParser(part, row)

    def _parserFromDict(self, part):
        *k, = part
        return part[k[0]]

    def _errorFunc(self):
        return 'error'

    def _appendResultToRow(self, result):
        if result != None:
            self._rows.append(result)

    def _printList(self):
        print(self._rows)

    @classmethod
    def _logReport(cls, message="DONE"):
        cls._statusApp = message

    @classmethod
    def getStatusApp(cls):
        return "ParserLists: " + cls._statusApp


if __name__ == '__main__':
    ParserLists().run()
    print(ParserLists().getStatusApp())