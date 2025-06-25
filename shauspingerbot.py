import discord
from discord.ext import commands
import settings
import asyncio

logger = settings.logging.getLogger("bot")


def shauspinger():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents) 

    #bot.remove_command('help')

    @bot.event
    async def on_ready():
        try:
            logger.info(f"User: {bot.user}(ID: {bot.user.id}) Guild ID: {bot.guilds[0].id}")
            for cmd_file in settings.CMDS_DIR.glob("*.py"):
                if cmd_file.name != "__init__.py":
                    await bot.load_extension(f"commands.{cmd_file.name[:-3]}")

            for cog_file in settings.COGS_DIR.glob("*.py"):
                if cog_file.name != "__init__.py":
                    await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

            main_channel = bot.get_channel(settings.MAIN_CHANNEL_ID)
            if main_channel:
                await main_channel.send(':3')
            else:
                print("where channel")
                await bot.close()  
                return

            #bot.text_input_task = asyncio.create_task(start_text_input_loop())

            print("rediii")

        except Exception as e:
            print(e)

    # async def start_text_input_loop():
    #     while not bot.is_closed():
    #         message = await asyncio.to_thread(input, "enter mesag: ")
    #         channel = bot.get_channel(settings.MAIN_CHANNEL_ID)
    #         if channel:
    #             await channel.send(message)
    #         else:
    #             print("Main channel not found!")

    async def close_bot():
        if bot.text_input_task and not bot.text_input_task.done():
            bot.text_input_task.cancel()  
            try:
                await bot.text_input_task
            except asyncio.CancelledError:
                pass  

        await bot.close()

    @bot.event
    async def command_error(ctx, error):
       print(f"Command error: {error}")


    bot.close_bot = close_bot
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


shauspinger()