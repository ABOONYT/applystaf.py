import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="S", intents=discord.Intents.all())

token = 'add your token'


@bot.event
async def on_ready():
  activity = discord.Activity(name='Sapply | Lucky ibo ',
                              type=discord.ActivityType.playing)
  await bot.change_presence(activity=activity)
  print(f'Logged in as {bot.user.name}')





class Application:

  def __init__(self, name, age, gender, activity):
    self.name = name
    self.age = age
    self.gender = gender
    self.activity = activity


applications = {}


@bot.command()
async def apply(ctx):
  await ctx.send("سلاو بەخێربێیت تکایە وەڵامی راستی ئەم پسیارانە بدەوە")
  await ctx.send("ناوی تەواوت چیە ؟")
  name = await bot.wait_for('message',
                            check=lambda message: message.author == ctx.author)

  await ctx.send("تەمەنت چەندە ؟")
  age = await bot.wait_for('message',
                           check=lambda message: message.author == ctx.author)

  await ctx.send("کچیەت یان کور ؟")
  gender = await bot.wait_for(
    'message', check=lambda message: message.author == ctx.author)

  await ctx.send("رۆژانە چەند کاتژمێر دەتوانی ئەکتیڤ بیت ؟")
  activity = await bot.wait_for(
    'message', check=lambda message: message.author == ctx.author)

  application = Application(name.content, age.content, gender.content,
                            activity.content)
  applications[ctx.author.id] = application

  embed = discord.Embed(title="بوون بە ستاف", color=discord.Color.blue())
  embed.add_field(name="Name", value=application.name, inline=False)
  embed.add_field(name="Age", value=application.age, inline=False)
  embed.add_field(name="Age", value=application.gender, inline=False)
  embed.add_field(name="Age", value=application.activity, inline=False)

  await ctx.send(
    "زۆر سوپاس بۆ پرکردنەوەی پسیارەکان تکایە چاوەروان بە بۆ وەڵام دانەوەت لەلایان رۆڵ بەدەستەوە"
  )


@bot.command()
async def accept(ctx, member: discord.Member):
  if member.id not in applications:
    await ctx.send("هیچ داواکاریەکی پێشکەش نەکردوە")
    BrokenPipeError
    return

  application = applications[member.id]

  embed = discord.Embed(title="وەرگیرا لە ستاف", color=discord.Color.blue())
  embed.add_field(name="ناوی تەواوت چیە ؟",
                  value=application.name,
                  inline=False)
  embed.add_field(name="تەمەنت چەندە ؟", value=application.age, inline=False)
  embed.add_field(name="کچیەت یان کور ؟",
                  value=application.gender,
                  inline=False)
  embed.add_field(name="رۆژانە چەند کاتژمێر دەتوانی ئەکتیڤ بیت ؟",
                  value=application.activity,
                  inline=False)
  embed.set_thumbnail(
    url="https://media2.giphy.com/media/YnZW20Aea27gDSMjNt/giphy.gif")

  await ctx.send(
    f"{member.mention}, پیرۆزە لە ستاف قبوڵ کرایت بەهیوای بەسەربردنی کاتێکی خۆش"
  )
  await ctx.send(embed=embed)


bot.run(token)
