import nextcord
from nextcord.ext import commands
import animal_config as config
import aiohttp

botver = "Animals! v1.0"

async def get_dev(self):
    dev = self.bot.get_user(config.owner)

class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f":ping_pong: Ping! **{self.bot.latency * 1000:.0f}**ms")

    @nextcord.slash_command(name="cat", description="Get a picture of a kitty!")
    async def cat(self, interaction: nextcord.Interaction):
        #--Get image from random.cat API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://aws.random.cat/meow') as kitty:
                data = await kitty.json()
                image = data["file"]
                embed = nextcord.Embed(title=f"🐱 Here's your cute kitty!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="dog", description="Get a picture of a doggy!")
    async def dog(self, interaction: nextcord.Interaction):
        #--Get image from dog.ceo API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://dog.ceo/api/breeds/image/random') as doggy:
                data = await doggy.json()
                image = data["message"]
                embed = nextcord.Embed(title=f"🐶 Here's your cute doggy!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="dog", description="Get a picture of a doggy!")
    async def dog(self, interaction: nextcord.Interaction):
        #--Get image from dog.ceo API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://dog.ceo/api/breeds/image/random') as doggy:
                data = await doggy.json()
                image = data["message"]
                embed = nextcord.Embed(title=f"🐶 Here's your cute doggy!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="bunny", description="Get a picture of a bunny!")
    async def bunny(self, interaction: nextcord.Interaction):
        #--Get image from bunnies.io API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.bunnies.io/v2/loop/random/?media=gif,png') as bunny:
                data = await bunny.json()
                try:
                    image = data["media"]["gif"]
                except:
                    image = data["media"]["poster"]
                seen = data["thisServed"]
                total = data["totalServed"]
                id = data["id"]
                embed = nextcord.Embed(title=f"🐇 Here's your cute bunny!", description=f"🔢 ID: {id}\n👀 This bunny has been seen {seen} times.\n🐰 {total} bunnies have been seen.\n🔗 https://www.bunnies.io/#{id}", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="duck", description="Get a picture of a duck!")
    async def duck(self, interaction: nextcord.Interaction):
        #--Get image from random-d.uk API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://random-d.uk/api/random') as ducky:
                data = await ducky.json()
                image = data["url"]
                embed = nextcord.Embed(title=f"🦆 Here's your cute duck!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="lizard", description="Get a picture of a lizard!")
    async def lizard(self, interaction: nextcord.Interaction):
        #--Get image from nekos.life API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://nekos.life/api/v2/img/lizard') as lizard:
                data = await lizard.json()
                image = data["url"]
                embed = nextcord.Embed(title=f"🦎 Here's your cute lizard!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="shiba", description="Get a picture of a shiba inu!")
    async def shiba(self, interaction: nextcord.Interaction):
        #--Get image from shibe.online API--#
        async with aiohttp.ClientSession() as session:
            async with session.get('https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true') as shiba:
                data = await shiba.json()
                image = data[0]
                embed = nextcord.Embed(title=f"🐶 Here's your cute shiba inu!!", color=0x8253c3)
                embed.set_image(url=image)
                embed.set_footer(text="Requested by " + interaction.user.display_name + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.display_avatar.url)
                await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="help", description="Sends a full list of commands to your DMs.")
    async def help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title=botver, description="This bot uses slash commands! You can use / to run a command.", color=0x7289da)
        embed.add_field(name="Animals:", value="**/cat** - Get a picture of a kitty!\n**/dog** - Get a picture of a doggy!\n**/bunny** - Get a picture of a bunny!\n**/duck** - Get a picture of a duck!\n**/lizard** - Get a picture of a lizard!\n**/shiba** - Get a picture of a shiba inu!", inline=False)
        embed.add_field(name="Other:", value="**/info** - See information about the bot, such as its uptime.\n**/ping** - Returns the bot's latency.\n**/bug** - Submit a bug report if anything goes wrong. \n**/suggest** - Want to see something added to the bot? Suggest it!", inline=False)
        embed.add_field(name="APIs Used:", value="random.cat\ndog.ceo\nbunnies.io\nrandom-d.uk\nnekos.life\nshibe.online", inline=False)
        embed.set_footer(text=botver + " by PrincessLillie#2523", icon_url=self.bot.user.avatar.url)
        await interaction.user.send(embed=embed)
        await interaction.response.send_message("✅ Sent the command list to your DMs!")

def setup(bot):
    bot.add_cog(Animals(bot))
