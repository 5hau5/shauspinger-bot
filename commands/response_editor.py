from discord.ext import commands
import discord
import response_config_handler as rch
import difflib
import settings

@commands.command(name="addres", help="add a response: //addres [category] [response] [comment] [weight]")
async def addres(ctx, category: str, response: str, comment: str, weight: int):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
    
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    rch.add_response(section, response, weight, comment)
    await ctx.send(f"added response to `{section}`: {response} (weight: {weight}, comment: {comment})")

@commands.command(name="addtrig", help="add a trigger: //addtrig [category] [trigger]")
async def addtrig(ctx, category: str, trigger: str):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
     
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    rch.add_trigger(section, trigger)
    await ctx.send(f"added trigger `{trigger}` to `{section}`.")


@commands.command(name="delres", help="delete response by index: //delres [category] [index]")
async def delres(ctx, category: str, index: int):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
     
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    try:
        del rch.config[section]["responses"][index]
        del rch.config[section]["weights"][index]
        del rch.config[section]["comments"][index]
        rch.save_config()
        await ctx.send(f"deleted response at index {index} in `{section}`.")
    except Exception as e:
        await ctx.send(f"error: {e}")


@commands.command(name="deltrig", help="delete trigger: //deltrig [category] [trigger]")
async def deltrig(ctx, category: str, trigger: str):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
 
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    try:
        rch.config[section]["triggers"].remove(trigger)
        rch.save_config()
        await ctx.send(f"trigger `{trigger}` deleted from `{section}`.")
    except ValueError:
        await ctx.send(f"trigger `{trigger}` not found in `{section}`.")

@commands.command(name="editres", help="edit response: //editres [category] [index] [response] [comment] [weight]")
async def editres(ctx, category: str, index: int, response: str, comment: str, weight: int):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
 
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    try:
        rch.config[section]["responses"][index] = response
        rch.config[section]["weights"][index] = weight
        rch.config[section]["comments"][index] = comment
        rch.save_config()
        await ctx.send(f"edited response at index {index} in `{section}`.")
    except Exception as e:
        await ctx.send(f"error: {e}")

@commands.command(name="edittrig", help="edit trigger: //edittrig [category] [old_trigger] [new_trigger]")
async def edittrig(ctx, category: str, old_trigger: str, new_trigger: str):
    if ctx.author.id != settings.THE_SHAUS_ID:
        await ctx.send("no")
        return
 
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    triggers = rch.config[section].get("triggers", [])
    if old_trigger in triggers:
        if new_trigger in triggers:
            await ctx.send(f"trigger `{new_trigger}` already exists.")
            return
        idx = triggers.index(old_trigger)
        triggers[idx] = new_trigger
        rch.save_config()
        await ctx.send(f"replaced `{old_trigger}` with `{new_trigger}` in `{section}`.")
        return

    # fuzzy match
    closest = difflib.get_close_matches(old_trigger, triggers, n=1, cutoff=0.6)
    if closest:
        await ctx.send(f"`{old_trigger}` not found. did you mean `{closest[0]}`?")
    else:
        await ctx.send(f"`{old_trigger}` not found and no similar triggers in `{section}`.")

@commands.command(name="listres", help="list responses: //listres [category]")
async def listres(ctx, category: str):
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    data = rch.config[section]
    responses = data.get("responses", [])
    weights = data.get("weights", [])
    comments = data.get("comments", [])

    if not responses:
        await ctx.send(f"no responses found in `{section}`.")
        return

    embed = discord.Embed(
        title=f"responses in `{section}`",
        color=discord.Color.blurple()
    )

    for i, (resp, weight) in enumerate(zip(responses, weights)):
        comment = comments[i] if i < len(comments) else "—"
        embed.add_field(
            name=f"#{i} • weight: {weight}",
            value=f"`{resp}`\n*{comment}*",
            inline=False
        )

    await ctx.send(embed=embed)

@commands.command(name="listtrig", help="list triggers: //listtrig [category]")
async def listtrig(ctx, category: str):
    section = category.lower()
    if section not in rch.config:
        await ctx.send(f"category `{section}` does not exist.")
        return

    triggers = rch.config[section].get("triggers", [])
    if not triggers:
        await ctx.send(f"no triggers found in `{section}`.")
        return

    embed = discord.Embed(
        title=f"triggers in `{section}`",
        description="\n".join(f"`{t}`" for t in triggers),
        color=discord.Color.orange()
    )

    await ctx.send(embed=embed)



async def setup(bot):
    bot.add_command(addres)
    bot.add_command(addtrig)
    bot.add_command(delres)
    bot.add_command(deltrig)
    bot.add_command(editres)
    bot.add_command(listres)
    bot.add_command(listtrig)
    bot.add_command(edittrig)

