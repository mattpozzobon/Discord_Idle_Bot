import discord
import asyncio


class MyView(discord.ui.View):
    def __int__(self):
        super().__init__()

    async def on_timeout(self):
        print("timeout")
        await self.message.edit(content="Time Out", embed=None, view=None)

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.author.id

    @discord.ui.button(label="Work!", style=discord.ButtonStyle.green, custom_id="work")
    async def button_callback1(self, button, interaction):
        button.label = "Working"
        button.disabled = True
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name="Working", value="0")
        await interaction.response.edit_message(embed=embed, view=self)
        client.loop.create_task(self.test())


    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def button_callback2(self, button, interaction):
        self.stop()
        btn_work = [x for x in self.children if x.custom_id == "work"][0]
        btn_work.disabled = True
        button.disabled = True
        embed = discord.Embed(color=discord.Color.red())
        embed.add_field(name="Relaxing", value="goodbye")
        await interaction.response.edit_message(embed=embed, view=self)


    async def test(self):
        await client.wait_until_ready()
        count = 0
        while not self.is_finished():
            embed = discord.Embed(color=discord.Color.green())
            embed.add_field(name="Counter", value=str(count))
            await self.message.edit(embed=embed, view=self)
            await asyncio.sleep(1)
            count += 1