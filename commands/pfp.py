from discord.ext import commands
import discord
import settings

@commands.command(
    name="pfp",
    aliases=["av", "avatar"],
    help="shows a larger embed of a users profile picture",
    enabled=True
)
async def pfp(
    ctx,
    member: discord.Member = commands.parameter(default=None, description="The user of the profile picutre")
):
    if not member:
        member = ctx.author

    if member.id == ctx.bot.user.id:
        await ctx.send(settings.BOT_PFP)
        await ctx.send(f"Source: {settings.BOT_PFP_SOURCE}")
        return

    embed = discord.Embed(title=member).set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(pfp)