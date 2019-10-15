from ParserL.app import ParserApp
from ParserL2.app2 import ParserApp2
from Logger import Logger

logger = Logger()

@logger.cls_log
class MainApp(object):
    __slots__ = ('_logs', '_applications')


    def __init__(self):
        self._logs = []
        self._applications = [ParserApp, ParserApp2]


    def run(self):
        try:
            self._mainLoop()
        except Exception as e:
            self._appendStatusToLog(repr(e))


    def _mainLoop(self):
        for app in self._applications:
            self._runNextApp(app)
            self._appendStatusToLog(app.getStatusApp())

    @staticmethod
    def _runNextApp(app):
        app().run()


    def _appendStatusToLog(self, report="DONE"):
        self._logs.append(report)

    def printStatusApps(self):
        print(self._logs)




if __name__ == '__main__':

    application = MainApp()
    application.run()
    application.printStatusApps()