import discord
import time
import json
from pathlib import Path
from discord.ext import commands

Discord_Bot_Dir = Path("./")
linksPath = Path(Discord_Bot_Dir / "resources/")

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.script_start = time.time()
        with open("./data/settings.json", "r") as settings:
            self.settings = json.load(settings)
        self.prefix = self.settings['prefix']

    @commands.command()
    async def help(self,ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                    title="Dux-Bot Command List",
                    colour = discord.Colour.red()
                )
            categories = ['info', 'gifs', 'fun', 'daydeal', 'duel', 'owner']
            embed.add_field(name='Available categories:', value=await self.help_string(categories))
            await ctx.channel.send(embed=embed)

    async def help_string(self, categories):
        mainString = ''
        for c in categories:
            mainString += f'`{c}`'
            if c != categories[-1]:
                mainString += f', '
        return mainString

    @commands.command()
    async def gifs(self,ctx):
        embed = discord.Embed(
                title="Gifs",
                description=f"Use any of the available gif commands and tag a person in order to send a GIF of that action",
                colour = discord.Colour.greyple()
            )
        embed.add_field(name="**Possible categories:** ",value="`slap`, `hug`, `cuddle`, `kiss`, `bite`")
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def fun(self,ctx):
        embed = discord.Embed(
                title="Gifs",
                description=f"Some fun command to play around.",
                colour = discord.Colour.greyple()
            )
        embed.add_field(name="`pp`",value="Tells how long is your pp :)", inline=False)
        embed.add_field(name="`pickup`",value="Wanna hit on someone? Let me be your wingman! Most of them are inappropriate so please use it on people you know well!", inline=False)
        embed.add_field(name="`roast`",value="Insult someone until they cry", inline=False)
        embed.add_field(name="`8ball`",value="Ask the bot a question that you dont want the answer to.", inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def daydeal(self,ctx):
        embed = discord.Embed(
                title="Daydeal",
                description=f"Super duper cool https://daydeal.ch integration in discord",
                colour = discord.Colour.green()
            )
        embed.add_field(name="`deal`",value="Sends current daydeal", inline=False)
        embed.add_field(name="`setupDaydeal`",value=f"Setups the daydeal to send it whenever a new one is available. us it like `{self.prefix}setupDaydeal [channel] [roleToPing]`. You need 'manage_channels' permission to use this command.", inline=False)
        embed.add_field(name="`stopDaydeal`",value="Stops automatic sending od daydeals", inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def duel(self,ctx):
        embed = discord.Embed(
                title="Duel",
                description=f"To start a duel use command `{self.prefix}fight userOfYourChoice` and ping a person you want to fight. There are 3 classes and each one has different stats. There is Berserker, Tank and Wizard. ",
                colour = discord.Colour.greyple()
            )
        embed.add_field(name='Stats', value="```Statistics: Berserker  Tank  Wizard\n"+
                                            "Health:       1000     1200    700\n"+
                                            "Max Attack:   140      100     200\n"+
                                            "Max Defense:  30       60      20\n"+
                                            "Max Mana:     30       20      50```", inline=False)
        embed.add_field(name='Description', value="When the duel starts you will be able to choose action you want to do. `punch`, `defend` and `end`. `punch` boosts your attack and `defend` boosts your defense. After you choose an action, you will hit the opponent and he will counter attack. If the defense is higher than the attack damage of the opponent you will block the attack. `end` makes you surrender.", inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def owner(self,ctx):
        embed = discord.Embed(
                title="Owner",
                description=f"Some commands for the bot owner.",
                colour = discord.Colour.greyple()
            )
        embed.add_field(name="`run_command`",value="Run console commands remotely", inline=False)
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
