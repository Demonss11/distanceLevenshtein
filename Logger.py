import logging
import sys
from logging.handlers import TimedRotatingFileHandler


class Logger:

    def __init__(self):
        self.FORMATTER = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
        self.LOG_FILE = "my_app.log"
        self.logger = None

    def set_loggers(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        logger.propagate = False
        logger.setLevel(logging.INFO)
        self.logger = logger

    def get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        return console_handler

    def get_file_handler(self):
        file_handler = TimedRotatingFileHandler(self.LOG_FILE, when='midnight')
        file_handler.setFormatter(self.FORMATTER)
        return file_handler

    def log(self, func):

        def wrap_log(*args, **kwargs):
            self.set_loggers(func.__name__)
            self.logger.info("Вызов функции %s"% func.__name__)
            try:
                result = func(*args, **kwargs)
                self.logger.info("Вызов функции %s успешно завершен"% func.__name__)
            except Exception as e:
                self.logger.error("Error %s"%repr(e))

            return func

        return wrap_log

    def cls_log(self, klass):

        class WrapClass(object):

            def __init__(self, *args, **kwargs):
                self.oInstance = klass(*args, **kwargs)
                self.logger = Logger()

            def __getattribute__(self, s):
                try:
                    x = super(WrapClass, self).__getattribute__(s)
                except AttributeError:
                    pass
                else:
                    return x
                x = self.oInstance.__getattribute__(s)
                if type(x) == type(self.__init__):
                    return self.logger.log(x)
                else:
                    return x

        return WrapClass




if __name__ == "__main__":
    logger = Logger()
    def func():
        print("Hello")
    @logger.log
    def double_function(a):
        func()
        return a /0

    @logger.log
    def func2():
        print("10")

    #value = double_function(2)
    #print(value(7))
    double_function(2)
    func2()







