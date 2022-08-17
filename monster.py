from random import randrange

class Monster:
    def __init__(self):
        self.name = None
        self.level = None
        self.health = 100
        self.max_health = 100
        self.silver = 0

    def set_health(self, x):
        self.health = x

    def get_name(self):
        return str(self.name).split("#")[0]

    def get_level(self):
        return str(self.level)

    def get_silver(self):
        return str(self.silver)

    def get_health(self):
        return str(self.health)

    def get_max_health(self):
        return str(self.max_health)

    def generate(self, level):
        r = randrange(3)

        thisdict = {
            "1": ["Rat", "Cave Rat", "Snake"],
            "2": ["Troll", "Swamp Troll", "Troll Champion"],
            "3": ["Goblin", "Goblin Scavenger", "Goblin Assassin"],
        }

        self.name = thisdict[str(level)][r]
        self.level = level
        self.health = 20*level
        self.max_health = 20*level
        self.silver = round(self.level/2 * randrange(4)+1)
        return self.name

    def get_image(self):
        if self.name == "Rat":
            return "https://static.wikia.nocookie.net/tibia/images/a/af/Rat.gif/revision/latest?cb=20141110204448&path-prefix=en&format=original"
        elif self.name == "Cave Rat":
            return "https://static.wikia.nocookie.net/tibia/images/f/fb/Cave_Rat.gif/revision/latest?cb=20140823213706&path-prefix=en&format=original"
        elif self.name == "Snake":
            return "https://static.wikia.nocookie.net/tibia/images/3/32/Snake.gif/revision/latest?cb=20150416141150&path-prefix=en&format=original"
        elif self.name == "Troll":
            return "https://static.wikia.nocookie.net/tibia/images/f/f8/Mountain_Troll.gif/revision/latest?cb=20140823210135&path-prefix=en&format=original"
        elif self.name == "Swamp Troll":
            return "https://static.wikia.nocookie.net/tibia/images/b/bf/Swamp_Troll.gif/revision/latest?cb=20150418080038&path-prefix=en&format=original"
        elif self.name == "Troll Champion":
            return "https://static.wikia.nocookie.net/tibia/images/c/cc/Troll_Champion.gif/revision/latest?cb=20150418124701&path-prefix=en&format=original"
        elif self.name == "Goblin":
            return "https://static.wikia.nocookie.net/tibia/images/4/45/Goblin.gif/revision/latest?cb=20150418105027&path-prefix=en&format=original"
        elif self.name == "Goblin Scavenger":
            return "https://static.wikia.nocookie.net/tibia/images/c/c4/Goblin_Scavenger.gif/revision/latest?cb=20150418075655&path-prefix=en&format=original"
        else:
            return "https://static.wikia.nocookie.net/tibia/images/2/20/Muglex_Clan_Assassin.gif/revision/latest?cb=20171219235250&path-prefix=en&format=original"
