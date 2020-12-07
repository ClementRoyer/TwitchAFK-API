import sys, os, signal, time, atexit

from core import initialize, loadTwitch, collectAndBet
from config_loader import load
from utils import writeInFile, writeTrunc, cout, create_file, create_folder, enableDebug

# enableDebug()

## Settings
log_directory = "logs/"
## End settings

## Variables
username = sys.argv[1]
stream = sys.argv[2]
token = sys.argv[3]
log = "file"
log_long = "file"
## end variables

def signal_handler(sig, frame):
    end()


def end():
    global log, log_long, chrome
    # End bot
    # Close file log
    # Close file log long
    cout("Ending viewing for '" + stream + "'")
    try:
        log.close()
        log_long.close()
    except Exception:
        pass
    try:
        chrome.close()
    except Exception:
        pass


def bot():
    global log, log_long, stream, chrome, token
    chrome = initialize(load(os.path.abspath(os.getcwd()) + '\\config.txt'), stream, token, log, log_long)
    loadTwitch(chrome)
    collectAndBet(chrome, 'https://www.twitch.tv/' + stream)


def main():
    # Create file with $1_$2.log
    # Create file with $1_$2_long.log
    # Start bot
    global log, log_long, log_directory
    create_folder(log_directory)
    log = create_file(log_directory + username + "_" + stream + ".log")
    log_long = create_file(log_directory + username + "_" + stream + "_long.log")
    bot()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGSEGV, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
atexit.register(end)