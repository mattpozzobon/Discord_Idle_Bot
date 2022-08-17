from configparser import ConfigParser

data = {"default_channel_id": "1008460903022350440",}


class Parser:
    def __init__(self):
        self.write()

    def write(self):
        config = ConfigParser()
        config['settings'] = data

        with open("./settings.ini", "w") as f:
            config.write(f)

    def get(self, topic, info):
        config = ConfigParser()
        config.read("settings.ini")
        return config.get(topic, info)