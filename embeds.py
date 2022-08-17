import discord


def description(author, avatar):
    embed = discord.Embed(title="Tibia Idle", description="Simple Tibia Idle game where you fight against random Monsters, to play the game press Start Hunt!", color=discord.Colour.blurple())
    embed.set_author(name=author, icon_url=avatar)
    embed.set_thumbnail(url="https://media.istockphoto.com/vectors/simple-flat-pixel-art-illustration-of-cartoon-golden-inscription-up-vector-id1335529268?k=20&m=1335529268&s=612x612&w=0&h=DCGXjxQxXPDxgNoyRq7gC9-H0Yis6gloaMl-uag9760=")
    return embed


def game(author, avatar, game):
    embed = discord.Embed(title="Game", description="\u200b", color=discord.Colour.green())
    embed.set_author(name=author, icon_url=avatar)
    embed.set_thumbnail(url=game.get_action_pic())
    embed.add_field(name="action: \nstage:", value="\u200b", inline=True)
    embed.add_field(name=str(game.action) + "\n" +str(game.get_stage()), value="\u200b", inline=True)
    return embed


def player(player):

    if player.health <= 0:
        colour = discord.Colour.red()
    else:
        colour = discord.Colour.green()



    embed = discord.Embed(title="Player", color=colour)
    embed.set_thumbnail(url=player.get_outfit())

    embed.add_field(name="Name",
                    value=player.get_name(),
                    inline=False)

    embed.add_field(name="Status",
                    value=
                    "\nLv = "
                    "\nXp = "
                    "\nGP = "
                    "\nHP = ",
                    inline=True)

    embed.add_field(name="\u200b", value="\n"+player.get_level()+" "
                    "\n"+player.get_experience()+" "
                    "\n"+player.get_silver()+" "
                    "\n["+player.get_health()+"/"+player.get_max_health()+"]", inline=True)
    return embed


def monster(monster):
    embed = discord.Embed(title="Monster", color=discord.Colour.green())
    embed.set_thumbnail(url=monster.get_image())

    embed.add_field(name="Name",
                    value=monster.get_name(),
                    inline=False)

    embed.add_field(name="Status",
                    value=
                    "\nLv = "
                    "\nGP = "
                    "\nHP = ",
                    inline=True)

    embed.add_field(name="\u200b", value="\n"+monster.get_level()+" "
                    "\n"+monster.get_silver()+" "
                    "\n["+monster.get_health()+"/"+monster.get_max_health()+"]", inline=True)

    return embed


def level_up(level):
    if int(level) == 2:
        embed = discord.Embed(title="You've levelled up!",
                              description="After countless fight's you've accrued enough Gold Coins to stop using your old gloves as a weapon and have acquired a fine sword.",
                              color=discord.Colour.green())
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/tibia/images/4/42/Spike_Sword.gif/revision/latest?cb=20050808104049&path-prefix=en&format=original")
        return embed
    if int(level) == 3:
        embed = discord.Embed(title="You've levelled up!",
                              description="Given the last few fights, you got yourself some armour and implemented some spikes on it on the change of reflecting some damage",
                              color=discord.Colour.green())
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/tibia/images/2/2e/Plate_Armor.gif/revision/latest?cb=20171214210907&path-prefix=en&format=original")
        return embed
    else:
        embed = discord.Embed(title="You've levelled up!", color=discord.Colour.green())
        return embed


def resting(game):
    embed = discord.Embed(title="You have eaten a "+str(game.food[0])+"  and healed "+str(game.food[1])+"!", color=discord.Colour.green())
    embed.set_thumbnail(url=game.food[2])
    return embed

def final(ans):
    if ans:
        embed = discord.Embed(title="You survived till the end and won!!!", color=discord.Colour.green())
        return embed
    else:
        embed = discord.Embed(title="You died!", color=discord.Colour.red())
        embed.set_image(url="https://static.wikia.nocookie.net/tibia/images/6/61/Death_tibia.JPG/revision/latest/scale-to-width-down/639?cb=20110923133734&path-prefix=en")
        return embed
