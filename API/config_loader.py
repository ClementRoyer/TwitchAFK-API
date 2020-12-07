from configparser import SafeConfigParser

def load(path):
    parser = SafeConfigParser()
    parser.read(path)

    obj = {
        "debug": False
    }

    obj["debug"] = parser.getboolean("my-config", "debug")
    obj["chrome_path"] = parser.get("my-config", "chrome_path")

    return obj