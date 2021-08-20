import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

bot = commands.Bot(command_prefix="p!") 

@bot.event
async def on_ready():
    print("Bot is ready") 

@bot.command()
async def dababy(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/763807544040488960/878348220189790208/0ee.jpg") 

@bot.command()
async def devs(ctx):
  embed = discord.Embed(
    title = 'Developers:',
    description = "OhKyro\nm. (mason)",
    colour = discord.Color.from_rgb(255, 0, 0)
    )
  await ctx.send(embed=embed)

@bot.command()
async def rules(ctx):
  embed = discord.Embed(
    title = 'Rules',
    description = "https://discord.com/terms\nhttps://discord.com/guidelines",
    colour = discord.Color.from_rgb(255,0,0)
    )
  await ctx.send(embed=embed)


@bot.command(aliases=['cl']) 
@commands.has_permissions(manage_messages = True) 
async def clear(ctx,amount=2):
  await ctx.channel.purge(limit = amount+1)
  embed = discord.Embed(
  description = "**Messages Cleared!**",
  colour = discord.Color.from_rgb(255,0,0)
  )
  await ctx.send(embed=embed)

@bot.command(aliases=['k']) 
@commands.has_permissions(kick_members = True) 
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
  await member.send(f"You have been kicked from **" + str(ctx.guild) + "**, Reason: "+reason)  
  embed = discord.Embed(
    description = "Successfully Kicked Member!\nReason: "+reason,
    colour = discord.Color.from_rgb(255, 165, 0)
    )
  await ctx.send(embed=embed)
  await member.kick(reason=reason)
  

@bot.command(aliases=['b']) 
@commands.has_permissions(ban_members = True) 
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
  await member.send(f"You have been banned from **" + str(ctx.guild) + "**, Reason: "+reason)  
  embed = discord.Embed(
    description = "Successfully Banned Member!\nReason: "+reason, 
    colour = discord.Color.from_rgb(255,0,0)
    )
  await ctx.send(embed=embed)
  await member.ban(reason=reason)
  
bot.command(aliases=['ub']) 
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#') 

  for banned_entry in banned_users:
    user = banned_entry.user

    if(user.name, user.discriminator)==(member_name,member_disc):

      await ctx.guild.unban(user)
      embed = discord.Embed(
        description = member_name +" Has Been Unbanned!",
        colour = discord.Color.from_rgb(0,255,0)
        )
      
      await ctx.send(embed=embed) 
      return
  await ctx.send(member+" was not found") 


bot.run("ODc3NjQ1Njk5NTk5MjA0NDYz.YR1pQA.8iuvEQmw_o3Lul5lI8WbeK_t8a4") 