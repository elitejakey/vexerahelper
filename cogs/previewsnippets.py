from discord.ext import commands
import discord

class previewsnippets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_role("Staff")
    async def pdocs(self, ctx):
        await ctx.send(f"Hey <User Mention>, \n\nPlease visit https://vexera.io/docs/ to read all of our documentation which contains all the information you need to learn about vexera!")

    @commands.command()
    @commands.has_role("Staff")
    async def ptest(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nYou are looking fine by me :)")

    @commands.command()
    @commands.has_role("Staff")
    async def paccessrole(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nHave you checked if you don't have an accessrole set? Commands may also be disabled in the channel you attempted to use.")
    
    @commands.command()
    @commands.has_role("Staff")
    async def pcommandperms(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nYou can disallow specific commands by using `​+perms deny <role> nodeHere`​ and replacing `​nodeHere`​ with anything from `​+perms nodes`​. You'll have to use this command for every category you want to disable. Examples: `​+perms deny <role> meme.*`​ and `​+perms deny <role> image.*`​ to disable the meme and image commands. Note that admins always bypass this.")
  
    @commands.command()
    @commands.has_role("Staff")
    async def pcommands(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nIf you want to have a full list of commands displayed, use `​​​+help`​​​ in <#273855440096329728>, or a channel Vexera is in! After this, you will be sent a DM!")
    
    @commands.command()
    @commands.has_role("Staff")
    async def pdetails(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nPlease give us more details about your problem, such as which command you tried, etc.")
    
    @commands.command()
    @commands.has_role("Staff")
    async def phigherup(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nA higher up staff member has been alerted about your concern and will look into the issue when they can! Thanks for your patience.")

    @commands.command()
    @commands.has_role("Staff")
    async def pinvite(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nYou can invite Vexera to your server here: <https://vexera.io/invite>")

    @commands.command()
    @commands.has_role("Staff")
    async def pinvitepro(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nYou can invite Vexera Pro to your server here: <https://vexera.pro/invite>")

    @commands.command()
    @commands.has_role("Staff")
    async def pmaintenance(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nPlease see <#393510653421420545> for more information about the ongoing maintenance.")
    
    
    @commands.command()
    @commands.has_role("Staff")
    async def pmusic(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nThis is a step-by-step guide to resolve most music issues:\n1. Try changing your server region to something other than Europe.\n2. Use `​+stop`​, then `​+join de-voice-1`\n​3. Use `​+stop`​, then `​+join de-voice-2`\n​4. Try changing your server region again. After this, repeat step 2 or 3.\n5. Clear your queue with `​+clear`​. After you have cleared the queue, repeat steps 1 to 3.")


    @commands.command()
    @commands.has_role("Staff")
    async def pmusicpremium(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nThis is a step-by-step guide to resolve most music issues:\n1. Try changing your server region to something other than Europe. Go to step 2/3.\2. Use `​+stop`​, then `​+join de-voice-1-1`\n​3. Use `​+stop`​, then `​+join de-voice-2-1`\n​4. Try changing your server region again. After this, repeat step 2 or 3.\n5. Clear your queue with `​+clear`​. You can save it first by using `​+dump all`​ before clearing, I'd advise doing this only if the queue content is important. After you have cleared the queue, repeat steps 1 to 3. Copy the link from the dump command and use `​+play`​ with it to get all songs back in the queue.")

    @commands.command()
    @commands.has_role("Staff")
    async def pmusicpro(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nThis is a step-by-step guide to resolve most music issues:\n1. Try changing your server region to something other than Europe. Go to step 2/3.\n2. Use `​+stop`​, then `​+join de-voice-1-1`\n​3. Use `​+stop`​, then `​+join de-voice-2-1`\n​4. Try changing your server region again. After this, repeat step 2 or 3.\n5. Clear your queue with `​+clear`​. You can save it first by using `​+dump all`​ before clearing, I'd advise doing this only if the queue content is important. After you have cleared the queue, repeat steps 1 to 3. Copy the link from the dump command and use `​+play`​ with it to get all songs back in the queue.")

    @commands.command()
    @commands.has_role("Staff")
    async def ppremium(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nVexera Premium/Pro is activated on all servers **you own**. If you do **not** own a server there is unfortunately no easy way you can use Vexera Premium/Pro on that server. The owner is able to either purchase Vexera Premium/Pro **OR** you can transfer your subscription to the server owner. Keep in mind though that once you transfer your subscription, the Vexera Pro bot will leave and Vexera Premium features will no longer work on servers **you own**.")
    
    @commands.command()
    @commands.has_role("Staff")
    async def ppurchasepremium(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nIf you want to purchase premium, you can find out more Info here: https://vexera.io/premium")

    @commands.command()
    @commands.has_role("Staff")
    async def pstatus(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nPlease see <#393510653421420545> for more information about the current issue and further updates.")


    @commands.command()
    @commands.has_role("Staff")
    async def pstatuses(self, ctx):
        await ctx.send(f"Hey <User Mention>,\n\nPlease see <#393510653421420545> for more information about the current issue and further updates.")
    


def setup(bot):
    bot.add_cog(previewsnippets(bot))