import sys
import logging

# Custom imports
from utils.check_input_format import check_input_format

def setup_logging():
    # Create logger
    logger = logging.getLogger("mylogger")
    logger.setLevel(logging.DEBUG)  # capture all debug messages

    # Create file handler
    file_handler = logging.FileHandler("debug.log", mode="w")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)

    # Create stderr handler
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.DEBUG)
    stderr_handler.setFormatter(file_formatter)

    # Add both handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stderr_handler)

    return logger

def main():
    logger = setup_logging()
    logger.debug("Starting the program")
    file_content = sys.stdin.read()
    logger.debug("Read input from stdin")
    if not check_input_format(file_content, logger):
        logger.error("Invalid input format detected, printing NO and exiting")
        print("NO")
        exit(-1)
    logger.debug("Input format is valid, proceeding with further processing")

    print("YES")

if __name__ == "__main__":
    main()


