import discord
from discord.ext import commands

class pickems(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        ## SET YOUR TEAM NAMES AND THE EMOJIS YOU WANT HERE, IT'S JUST A
        self.teams = {
            "Team 1": "<:Team1:0>",
            "Team 2": "<:Team2:1>",
            "Team 3": "<:Team3:2>",
            "Team 4": "<:Team4:3>"
        }

        ## PUT THE SCHEDULE FOR THE WEEK IN HERE, THE NAMES ARE TAB SEPARATED (\t)
        l = '''Team 1\tTeam 2
Team 3\tTeam 4
'''

        # just a bit of reformatting don't mind this
        l = l.split("\n")
        for i in range(len(l)):
            l[i] = l[i].split("\t")
        self.schedule: list[list[str, str]] = l

        # not sure this actually does anything anymore
        self.colours = [
            discord.Colour.red(),
            discord.Colour.gold(),
            discord.Colour.green()
        ]

        # THIS IS THE ID OF THE CHANNEL YOU ARE DOING PICKEMS IN SET THIS
        self.pickemsID = 0

    # this is from the team tour but left as an example
    async def send_messages(self, ctx):

        channel = ctx.guild.get_channel(self.pickemsID)

        for i in range(0, 5):
            matchup = self.schedule[i]

            emojiA = self.teams[matchup[0]]
            emojiB = self.teams[matchup[1]]

            colour = discord.Colour.from_rgb(155, 200, 228)

            txt = emojiA + " " + matchup[0] + " vs " + emojiB + " " + matchup[1]
            embed = discord.Embed(
                title="",
                description=txt,
                colour=colour)
            # embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/922846525007204413/922846730423259176/Shuffle433.png")

            msg = await channel.send(embed=embed)
            print(msg.id)
            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)

        for i in range(5, 10):
            matchup = self.schedule[i]

            emojiA = self.teams[matchup[0]]
            emojiB = self.teams[matchup[1]]

            colour = discord.Colour.from_rgb(236, 169, 169)

            txt = emojiA + " " + matchup[0] + " vs " + emojiB + " " + matchup[1]
            embed = discord.Embed(
                title="",
                description=txt,
                colour=colour)
            # embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/922846525007204413/922846730423259176/Shuffle433.png")

            msg = await channel.send(embed=embed)
            print(msg.id)
            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)

        for i in range(10, 15):
            matchup = self.schedule[i]

            emojiA = self.teams[matchup[0]]
            emojiB = self.teams[matchup[1]]

            colour = discord.Colour.from_str("#98dd99")

            txt = emojiA + " " + matchup[0] + " vs " + emojiB + " " + matchup[1]
            embed = discord.Embed(
                title="",
                description=txt,
                colour=colour)
            # embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/922846525007204413/922846730423259176/Shuffle433.png")

            msg = await channel.send(embed=embed)
            print(msg.id)
            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)

    async def send_messages2(self, ctx):
        """
        Time to construct all the embeds and send emojis to them
        """
        channel: discord.TextChannel = ctx.guild.get_channel(self.pickemsID)

        for i in range(len(self.schedule)):
            matchup: list[str, str] = self.schedule[i]

            emojiA: str = self.teams[matchup[0]]
            emojiB: str = self.teams[matchup[1]]

            colour: discord.Colour = discord.Colour.gold()

            txt: str = emojiA + " " + matchup[0] + " vs " + emojiB + " " + matchup[1]
            embed: discord.Embed = discord.Embed(
                title="",
                description=txt,
                colour=colour)

            msg: discord.Message = await channel.send(embed=embed)

            await msg.add_reaction(emojiA)
            await msg.add_reaction(emojiB)

    @commands.command()
    async def send_week(self, ctx):
        try:
            channel: discord.TextChannel = ctx.guild.get_channel(self.pickemsID)
            embed: discord.Embed = discord.Embed(
                title="__Week 1__",
                description='''The matches this week are as follows:''',
                colour=discord.Colour.gold())

            ## TO SET THE CHINGLING IMAGE TO SOMETHING ELSE USE THIS
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/922846525007204413/922846730423259176/Shuffle433.png")
            msg: discord.Message = await channel.send(embed=embed)

            await self.send_messages2(ctx)

            embed: discord.Embed = discord.Embed(
                title="",
                description='''React to my messages above and I'll read though all your blind faith at __**00:00 on Tuesday**__''',
                colour=discord.Colour.gold())

            class DocLink(discord.ui.View):
                """this is for the  pickems doc on the post"""
                def __init__(self, timeout=None):
                    super().__init__(timeout=timeout)
                    # YOU CAN ADD MORE/LESS BUTTONS BY JUST REMOVING PAIRS OF LINES
                    url = "https://docs.google.com/spreadsheets/d/1OdirPC40s0ZoWv60QEUTpjyzpw_qysS_DFIldm9O4TU/edit#gid=568866385"
                    self.add_item(discord.ui.Button(label='Rules', url=url))

                    url = "https://docs.google.com/spreadsheets/d/1OdirPC40s0ZoWv60QEUTpjyzpw_qysS_DFIldm9O4TU/edit#gid=1803777399"
                    self.add_item(discord.ui.Button(label='Individual Standings', url=url))

                    url = "https://docs.google.com/spreadsheets/d/1OdirPC40s0ZoWv60QEUTpjyzpw_qysS_DFIldm9O4TU/edit#gid=1974805370"
                    self.add_item(discord.ui.Button(label='Team Standings', url=url))

            ## IF YOU WANT RID OF THE BUTTONS, SET view=None INSTEAD
            msg: discord.Message = await channel.send(embed=embed, view=DocLink())

        except Exception as e:
            print(e)

async def setup(client):
    """Leave this alone, it's used by the library"""
    await client.add_cog(pickems(client))
