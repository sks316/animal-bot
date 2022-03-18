import nextcord
from nextcord.ext import commands
import animal_config as config

botver = "Animals! v1.0"

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="bug", description="Send in a bug report if anything goes wrong.")
    async def bug(self, interaction: nextcord.Interaction, bug: str = nextcord.SlashOption(description="Your bug report.")):
        dev = self.bot.get_user(config.owner)
        embed = nextcord.Embed(title="⚠ Bug Report", description=bug, color=0xff0000)
        embed.set_footer(text="Submitted by " + interaction.user.name + "#" + interaction.user.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.avatar.url)
        await dev.send(embed=embed)
        await interaction.response.send_message("✅ Successfully sent in your bug report! Thank you for helping to make this bot better. \nIf you want to provide further details, send a DM to **" + dev.name + "#" + dev.discriminator + "**.")

    @nextcord.slash_command(name="ping", description="Pong! Returns the bot's latency.")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @nextcord.slash_command(name="suggest", description="Suggest a new feature for the bot, like a new animal command!")
    async def suggest(self, interaction: nextcord.Interaction, suggestion: str = nextcord.SlashOption(description="Your suggestion for the bot.")):
        dev = self.bot.get_user(config.owner)
        embed = nextcord.Embed(title="💭 Suggestion", description=suggestion, color=0x7289da)
        embed.set_footer(text="Submitted by " + interaction.user.name + "#" + interaction.user.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=interaction.user.avatar.url)
        await dev.send(embed=embed)
        await interaction.response.send_message("✅ Successfully sent in your suggestion! Thank you for helping to make this bot better. \nIf you want to provide further details, send a DM to **" + dev.name + "#" + dev.discriminator + "**.")

def setup(bot):
    bot.add_cog(Other(bot))
