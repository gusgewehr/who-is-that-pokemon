# bot.py
# coding=utf-8
import os # for importing env vars for the bot to use
import json
with open('pokemons.json', encoding="utf8") as pkmns:
    data = json.load(pkmns)
from twitchio.ext import commands
from twitchio.ext import routines
from random import randint
import time

@routines.routine(seconds=60.0)
async def hello(ctx: commands.Context):    
    n = randint(0,1)
    var = data['pokemons'][n]['sillhuette']
    acertos.start(n, ctx)
    await ctx.send(f'Quem é esse Pokémon? \n {var}')
    
@routines.routine(seconds=30, iterations=1)
async def acertos(n:int, ctx:commands.Context):
    name = data['pokemons'][n]['name']
    @bot.event()
    async def event_message(message):
        print(message)        
        #await ctx.send(f'{certo}')
        resposta.start(n, ctx) 
        time.sleep(30)     

@routines.routine(seconds=1, iterations=1)
async def resposta(n: int, ctx: commands.Context):
    name = data['pokemons'][n]['name']
    await ctx.send(f'{name}')

  



class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=os.environ['TMI_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
    
    @commands.command()
    async def start(self, ctx: commands.Context):
        await hello.start(ctx)
    





bot = Bot()

bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.