import sys, os, signal, time

debug = True

## Settings
log_directory = "logs/"
## End settings

## Variables
token = sys.argv[1]
stream = sys.argv[2]
log = "file"
log_long = "file"
## end variables

def signal_handler(sig, frame):
    end()


def cout(str):
    if debug:
        print(str)


def create_file(filename):
    cout("Creating file '" + filename + "'")
    return open(filename, "a")


def create_folder(folder):
    cout("Creating folder '" + folder + "'")
    if not os.path.exists(folder):
        os.mkdir(folder)


def write(f, content):
    f.write(content + '\n')
    f.flush()


def writeTrunc(f, content):
    f.truncate(0)
    f.write(content)
    f.flush()


def end():
    # End bot
    # Close file log
    # Close file log long
    cout("Ending viewing for '" + stream + "'")
    try:
        log.close()
        log_long.close()
    except Exception:
        pass


def bot():
    global log, log_long, stream
    for i in range(1, 10):
        cout("adding in file")
        writeTrunc(log, stream + ": refresh " + str(i))
        write(log_long, stream + ": refresh " + str(i))
        time.sleep(10)


def main():
    # Create file with $1_$2.log
    # Create file with $1_$2_long.log
    # Start bot
    global log, log_long, log_directory
    create_folder(log_directory)
    log = create_file(log_directory + token + "_" + stream + ".log")
    log_long = create_file(log_directory + token + "_" + stream + "_long.log")
    bot()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGSEGV, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)