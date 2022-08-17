class Player:
    def __init__(self, author):
        self.discord_id = author.id
        self.name = author
        self.level = 1
        self.experience = 0
        self.silver = 0
        self.health = 250
        self.max_health = 250

    def set_health(self, x):
        self.health = x

    def get_name(self):
        return str(self.name).split("#")[0]

    def get_level(self):
        return str(self.level)

    def get_experience(self):
        return str(self.experience)

    def get_silver(self):
        return str(self.silver)

    def get_health(self):
        return str(self.health)

    def get_max_health(self):
        return str(self.max_health)

    def get_outfit(self):
        if self.health <= 0:
            return "https://static.wikia.nocookie.net/tibia/images/4/47/Dead_Human1.gif/revision/latest?cb=20141122152925&path-prefix=en&format=original"
        if self.level == 1:
            x = "https://static.wikia.nocookie.net/tibia/images/6/6b/Outfit_Warrior_Male.gif/revision/latest?cb=20060829022854&path-prefix=en&format=original"
        elif self.level == 2:
            x = "https://static.wikia.nocookie.net/tibia/images/7/76/Outfit_Warrior_Male_Addon_2.gif/revision/latest?cb=20060829022858&path-prefix=en&format=original"
        else:
            x = "https://static.wikia.nocookie.net/tibia/images/5/5e/Outfit_Warrior_Male_Addon_3.gif/revision/latest?cb=20080623221001&path-prefix=en&format=original"
        return x
