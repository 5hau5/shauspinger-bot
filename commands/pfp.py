from discord.ext import commands
import discord

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
        await ctx.send('https://media.discordapp.net/attachments/738831293864738975/1230642032523870319/hoshino_pre_deth.png?ex=66340fb4&is=66219ab4&hm=805b6b869d18177e9b7a026a40b6152258bbfd2f80b697f36e872af07113fa7c&=&format=webp&quality=lossless&width=479&height=479 \nhttps://media.discordapp.net/attachments/738831293864738975/1230642045584933024/hoshino_deth.png?ex=66340fb7&is=66219ab7&hm=332c263568fe00eaa30b643196564b03253f960aa480f053c70076ea36542720&=&format=webp&quality=lossless&width=385&height=385')
        await ctx.send("Source: https://www.pixiv.net/en/artworks/111099494")
        return

    embed = discord.Embed(title=member).set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(pfp)