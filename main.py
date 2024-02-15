import discord
from discord.ext import commands
import asyncio

import os
from dotenv import load_dotenv
load_dotenv()  #just pulling the environment vars into memory so they can be grabbed

import logging

class MyClient(commands.Bot):  # discord.Client):
    #web_client: ClientSession
    def __init__(self, *, command_prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        # This is subclassed cause there used to be more complicated stuff here and I don't want to have to fix that


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = MyClient(command_prefix='--', intents=intents)

@client.check ## checks all messages are not dms
async def globally_block_dms(ctx):
    return ctx.guild is not None

async def main():
    async with client:

        for filename in os.listdir('./_cogs'):
            if filename.endswith('.py'):
                await client.load_extension('_cogs.' + filename[:-3])

        await client.start(os.environ.get("discord-token"))

asyncio.run(main())