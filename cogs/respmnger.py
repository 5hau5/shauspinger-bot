from discord.ext import commands
import discord
import response_config_handler as rch
import difflib
import settings

class ResponseManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = rch.get_config(main=False)

    @commands.command(name="addres", help="add a response: //addres <category> <response> [weight] [comment]", hidden=True)
    async def addres(
        self,
        ctx, 
        category: str=commands.parameter(default=None, description='the category to add the response to'),
        response: str=commands.parameter(default=None, description='the response to add'),
        weight: int=commands.parameter(default=10, description='weightage of the probability'), 
        comment: str=commands.parameter(default=None, description='a comment on the response')):

        if ctx.author.id != settings.THE_SHAUS_ID:
            return await ctx.send("no")
        
        if not all([category, response]):
            return await ctx.send("used it wrong: `//addres <category> <response> [weight] [comment]`")
        
        section = category.lower()
        if section not in self.config:
            return await ctx.send(f"category `{section}` does not exist.")
            
        # if not comment:
        #     comment = "---"

        comment = comment or "---"

        rch.add_response(section, response, weight, comment)
        await ctx.send(f"added response to `{section}`: {response} (weight: {weight}, comment: {comment})")

    @commands.command(name="delres", help="delete response by index: //delres <category> <index>", hidden=True)
    async def delres(
        self,
        ctx, 
        category: str=commands.parameter(default=None, description='the category to delete the response of'),
        index: int=commands.parameter(default=None, description='the index of the response to delete')):
        if ctx.author.id != settings.THE_SHAUS_ID:
            await ctx.send("no")
            return
        
        if category is None or index is None:
            await ctx.send("nope, its like: `//delres <category> <index>`")
            return
        
        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        try:
            del self.config[section]["responses"][index]
            del self.config[section]["weights"][index]
            del self.config[section]["comments"][index]
            rch.save_config()
            await ctx.send(f"deleted response at index {index} in `{section}`.")
        except Exception as e:
            await ctx.send(f"error: {e}")

    @commands.command(name="editres", help="edit response: //editres <category> <index> [response] [weight] [comment]", hidden=True)
    async def editres(
        self,
        ctx,
        category: str = commands.parameter(default=None, description='the category to edit the response of'),
        index: int = commands.parameter(default=None, description='the index of the response'),
        response: str = commands.parameter(default=None, description='the new response (optional)'),
        weight: str = commands.parameter(default=None, description='the new weight (optional)'),
        comment: str = commands.parameter(default=None, description='the new comment (optional)')
    ):
        if ctx.author.id != settings.THE_SHAUS_ID:
            await ctx.send("no")
            return

        if category is None or index is None:
            await ctx.send("usage: `//editres <category> <index> [response] [weight] [comment]`")
            return

        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        try:
            responses = self.config[section]["responses"]
            weights = self.config[section]["weights"]
            comments = self.config[section]["comments"]

            if not (0 <= index < len(responses)):
                await ctx.send(f"invalid index `{index}` for `{section}`.")
                return

            # update fields that are provided
            if response not in [None, "''", '""', ""]:
                responses[index] = response

            if weight not in [None, "''", '""', ""]:
                try:
                    weights[index] = int(weight)
                except ValueError:
                    await ctx.send(f"`{weight}` is not a proper integer.")
                    return

            if comment not in [None, "''", '""', ""]:
                comments[index] = comment

            rch.save_config()
            await ctx.send(f"edited response at index {index} in `{section}`.")

        except Exception as e:
            await ctx.send(f"error: {e}")

    @commands.command(name="addtrig", help="add a trigger: //addtrig <category> <trigger>", hidden=True)
    async def addtrig(
        self,
        ctx, 
        category: str=commands.parameter(default=None, description='the category to add the trigger word of'), 
        trigger: str=commands.parameter(default=None, description='the word to add')):

        if ctx.author.id != settings.THE_SHAUS_ID:
            return await ctx.send("no")
            
        
        if not all([category, trigger]):
            return await ctx.send("its like: `//addtrig <category> <trigger>`")
            
        
        section = category.lower()
        if section not in self.config:
            return await ctx.send(f"category `{section}` does not exist.")
            

        rch.add_trigger(section, trigger)
        await ctx.send(f"added trigger `{trigger}` to `{section}`.")


    @commands.command(name="deltrig", help="delete trigger: //deltrig <category> <trigger>", hidden=True)
    async def deltrig(
        ctx, 
        category: str=commands.parameter(default=None, description='the category to delete the trigger word of'), 
        trigger: str=commands.parameter(default=None, description='the word to delete')):

        if ctx.author.id != settings.THE_SHAUS_ID:
            await ctx.send("no")
            return
        
        if not all([category, trigger]):
            await ctx.send("use it like: `//deltrig <category> <trigger>`")
            return
    
        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        try:
            self.config[section]["triggers"].remove(trigger)
            rch.save_config()
            await ctx.send(f"trigger `{trigger}` deleted from `{section}`.")
        except ValueError:
            await ctx.send(f"trigger `{trigger}` not found in `{section}`.")


    @commands.command(name="edittrig", help="edit trigger: //edittrig <category> <old_trigger> <new_trigger>", hidden=True)
    async def edittrig(
        ctx, 
        category: str=commands.parameter(default=None, description='the category to list'), 
        old_trigger: str=commands.parameter(default=None, description='the trigger word to change'), 
        new_trigger: str=commands.parameter(default=None, description='the word to change to')):

        if not all([category, old_trigger, new_trigger]) :
            ctx.send("`//edittrig <category> <old_trigger> <new_trigger>`")

        if ctx.author.id != settings.THE_SHAUS_ID:
            await ctx.send("no")
            return
    
        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        triggers = self.config[section].get("triggers", [])
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

    @commands.command(name="lsres", help="list responses: //lsres <category>")
    async def lsres(
        ctx, 
        category: str=commands.parameter(default=None, description='The category to list')):

        if not category:
            await ctx.send("u need a category to list out `//lsres <category>`")
            return

        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        data = self.config[section]
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

    @commands.command(name="lstrig", help="list triggers: //lstrig <category>")
    async def lstrig(ctx, category: str):

        if not category:
            await ctx.send("u need a category to list out `//lstrig <category>`")
            return
        
        section = category.lower()
        if section not in self.config:
            await ctx.send(f"category `{section}` does not exist.")
            return

        triggers = self.config[section].get("triggers", [])
        if not triggers:
            await ctx.send(f"no triggers found in `{section}`.")
            return

        embed = discord.Embed(
            title=f"triggers in `{section}`",
            description="\n".join(f"`{t}`" for t in triggers),
            color=discord.Color.orange()
        )

        await ctx.send(embed=embed)