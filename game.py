import time
from random import randrange


class Game:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.stage = 1
        self.is_finished = False
        self.win = None
        self.food = 0
        self.action = "Hunting"

    def get_stage(self):
        return self.stage

    def add_stage(self):
        self.stage = self.stage + 1

    def get_action(self):
        if int(self.player.experience) == 100:
            self.player.experience = 0
            self.player.level += 1
            if self.player.level >= 4:
                self.player.level = 3
                self.is_finished = True
                self.win = True
            self.action = "Level UP!"
        elif self.stage % 4 == 0:
            self.get_food()
            self.action = "Resting"
        else:
            self.action = "Hunting"

    def get_action_pic(self):
        if self.action == "Resting":
            return "https://static.wikia.nocookie.net/tibia/images/c/c9/Oven_%28Lit%29.gif/revision/latest?cb=20150531123527&path-prefix=en&format=original"
        if self.action == "Level UP!":
            return "https://static.wikia.nocookie.net/tibia/images/7/7d/Cake.gif/revision/latest?cb=20061220152013&path-prefix=en&format=original"
        else:
            if self.player.level == 1:
                return "https://static.wikia.nocookie.net/tibia/images/b/b9/Sniper_Gloves.gif/revision/latest?cb=20171004034304&path-prefix=en&format=original"
            else:
                return "https://static.wikia.nocookie.net/tibia/images/4/42/Spike_Sword.gif/revision/latest?cb=20050808104049&path-prefix=en&format=original"

    def battle(self):
        if self.monster.name is None:
            self.monster.generate(self.player.level)

        if self.action == "Hunting":
            self.player.set_health(int(self.player.get_health())-(2*int(self.monster.level)))
            self.monster.set_health(int(self.monster.get_health())-(5*int(self.player.level)))

            if int(self.monster.get_health()) <= 0:
                self.player.silver += int(self.monster.silver)
                self.player.experience += 10
                self.monster.generate(int(self.player.get_level()))
                self.add_stage()

            if int(self.player.get_health()) <= 0:
                self.is_finished = True
                self.win = False

            if int(self.player.get_level()) == 4:
                self.is_finished = True
                self.win = True

        elif self.action == "Resting":
            self.player.set_health(int(self.player.get_health())+int(self.food[1]))
            self.add_stage()
        else:
            pass



    def get_food(self):
        r = randrange(4)
        thisdict = {
            "0": ["Apple", "7", "https://www.tibiawiki.com.br/images/d/d6/Red_Apple.gif"],
            "1": ["Bread", "12", "https://www.tibiawiki.com.br/images/2/22/Bread.gif"],
            "2": ["Meat", "16", "https://www.tibiawiki.com.br/images/5/58/Meat.gif"],
            "3": ["Dragon Ham", "20", "https://www.tibiawiki.com.br/images/d/d9/Dragon_Ham.gif"],
        }
        self.food = thisdict[str(r)]

