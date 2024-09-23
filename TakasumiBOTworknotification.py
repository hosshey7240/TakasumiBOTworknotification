import discord
import asyncio

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("起動完了")

@client.event
async def on_message(message):
    if message.author.id == 981314695543783484 and len(message.embeds) = 1 and "コイン手に入れました" in message.embeds[0].author.name:
        embed = discord.Embed(title="TakasumiBOT work通知",description="workを受信しました。\n20分後に通知します。",color=discord.Color.brand_green())
        await message.reply(embed=embed)
        await asyncio.sleep(1200)
        embed2 = discord.Embed(title="TakasumiBOT work通知",description="workの時間です\n</work:1132868147519692871>でお金を得ましょう",color=discord.Color.brand_green())
        await message.channel.send(embed=embed2)
            
client.run(TOKEN)
