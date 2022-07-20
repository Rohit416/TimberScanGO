import logging


class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)  # to get the testcase name captures testcase name in runtime

        filehandler = logging.FileHandler(filename=".\\logs\\automation.log")  # Defining a file for the logs
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # Format of the logs
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # knowledge of the filehandler to looger object
        logger.setLevel(logging.INFO)
        return logger

