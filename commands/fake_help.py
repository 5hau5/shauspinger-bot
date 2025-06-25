from discord.ext import commands
import discord

@commands.command(
    name="h",
    help="help but just h caus i cant figure out how ot have an alias to the default help command",
    enabled=True,
    hidden=True
)
async def fake_help(ctx,*args):
    help_text = f"help {' '.join(args)}"

    fake_message =  ctx.message
    fake_message.content = ctx.prefix + help_text

    #reprhase into a context
    new_ctx = await ctx.bot.get_context(fake_message, cls=type(ctx))
    await ctx.bot.invoke(new_ctx)

async def setup(bot):
    bot.add_command(fake_help)