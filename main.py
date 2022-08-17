import time

import discord
import asyncio
from parser import Parser
from player import Player
from monster import Monster
from game import Game
import embeds

parser = Parser()


# Client attributes https://discordpy.readthedocs.io/en/stable/api.html#client
intents = discord.Intents.all()
guilds = ["1008460903022350437"]
client = discord.Client(guilds=guilds, intents=intents)


class MyView(discord.ui.View):
    def __int__(self):
        super().__init__()
        self.author = None
        self.player = None
        self.monster = None
        self.game = None

    async def on_timeout(self):
        print("timeout")
        await self.message.edit(content="Time Out", embed=None, view=None)

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.author.id

    @discord.ui.button(label="Start Hunt!", style=discord.ButtonStyle.primary, custom_id="btn_start")
    async def button_callback1(self, button, interaction):
        self.clear_items()
        client.loop.create_task(self.actions())

    async def actions(self):
        await client.wait_until_ready()

        while not self.is_finished():
            self.game.get_action()
            self.game.battle()
            custom = []
            if self.game.action == "Level UP!":
                custom = embeds.level_up(self.player.level)
            elif self.game.action == "Resting":
                custom = embeds.resting(self.game)
            elif self.game.action == "Hunting":
                custom = embeds.monster(self.monster)
            else:
                pass

            if self.game.is_finished:
                await self.message.edit(embeds=[
                    embeds.game(self.author, self.author.avatar, self.game),
                    embeds.player(self.player), embeds.final(self.game.win)], view=self)
                self.stop()
            else:
                await self.message.edit(embeds=[
                    embeds.game(self.author, self.author.avatar, self.game),
                    embeds.player(self.player),
                    custom], view=self)

                if self.game.action == "Resting":
                    time.sleep(4)

                if self.game.action == "Level UP!":
                    time.sleep(10)

            await asyncio.sleep(1)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.content.lower() == "!":
        if int(message.channel.id) == int(parser.get("settings", "default_channel_id")):
            view = MyView(timeout=None)
            view.author = message.author
            view.player = Player(message.author)
            view.monster = Monster()
            view.game = Game(view.player, view.monster)

            embed = embeds.description(message.author, message.author.avatar)
            await message.channel.send(embed=embed, view=view)

client.run("MTAwOTA3Njc0MTUyNjAxNjAyMA.GQU-zk._0tNv1umr8X_d3n0V-jbgoangAwe31cK25bQfM")

