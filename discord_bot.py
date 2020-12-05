import discord
import asyncio
import discord.guild
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is Ready!')

@client.command()
async def ping(ctx):
    latency = str(int(client.latency * 1000))
    await ctx.send(f'Pong :)\t{latency}ms')

@client.command()
async def Im_hackur(ctx):
    await quesfun(ctx)


async def quesfun(ctx):
    await ctx.send('Hi there! you wanna be a hackurman?')
    await asyncio.sleep(1)
    await ctx.send('Decode THIS >>>> Zmw0Z3sxX1c0bm40X0IzX2g0Y2t1cn0=')
    await ctx.send('FACT: Bases turn red litmus paper blue!')

    while True:
        answer1 = await client.wait_for("message", check=None)
        if str(answer1.content) == 'fl4g{1_W4nn4_B3_h4ckur}':
            break
    await ctx.send('Paste this Code in Server, then continue: !noob B8vgjUz0WT]_b[9q$&Hl\n')
    if str(answer1.content) == 'fl4g{1_W4nn4_B3_h4ckur}':
        await ctx.send('Congrats!! But this is not the end.... Keep trying!\nHere is your next challenge.')
        await asyncio.sleep(1)
        await ctx.send('Decode THIS >>>> sy4t{Gu15_sy4t_e0gng3f}')
        await ctx.send('FACT: The Earth rotates on its axis.')
        
        while True:
            answer2 = await client.wait_for("message", check=None)
            if str(answer2.content) == 'fl4g{Th15_fl4g_r0tat3s}':
                break
        await ctx.send('Paste this Code in Server, then Continue: !moderator Pn|@McPk695`Xa{QJLCO+m-D^\n')
        if str(answer2.content) == 'fl4g{Th15_fl4g_r0tat3s}':
            await ctx.send('Hmm..Managed to solve that too? I think i have to throw something more salty!\nOkay. Solve this!    (͠≖ ͜ʖ͠≖)')
            await asyncio.sleep(1)
            await ctx.send('Decode THIS >>>> xl4r{L0mr_4d_o!f3g4c}')
            await ctx.send('FACT: Vinegar is better with "salt"')

            while True:
                answer3 = await client.wait_for("message", check=None)
                if str(answer3.content) == 'fl4g{S0ur_4s_v!n3g4r}':
                    break

            if str(answer3.content) == 'fl4g{S0ur_4s_v!n3g4r}':
                await ctx.send('Paste this Code in Server: !admin $z3Pf($JIKju8bI3M^G2VkZ`E$MP-\n')
                await ctx.send('Mine Journey has ended here, but you need to Go a long way....😀')
            else:
                print('Wrong2')

        else:
            print('Wrong1')

    else:
        print('Wrong')

@client.command()
async def noob(ctx, message):
    if message=='B8vgjUz0WT]_b[9q$&Hl':
        role = ctx.guild.get_role(773590805956132885)
        await ctx.author.add_roles(role)
        await ctx.send(f"Successfully created and assigned {role.mention}!")

@client.command()
async def moderator(ctx, message):
    if message=='Pn|@McPk695`Xa{QJLCO+m-D^':
        role = ctx.guild.get_role(773590805956132885)
        await ctx.author.remove_roles(role)
        role = ctx.guild.get_role(773596355582623754)
        await ctx.author.add_roles(role)
        await ctx.send(f"Successfully created and assigned {role.mention}!")

@client.command()
async def admin(ctx, message):
    if message=='$z3Pf($JIKju8bI3M^G2VkZ`E$MP-':
        role = ctx.guild.get_role(773596355582623754)
        await ctx.author.remove_roles(role)
        role = ctx.guild.get_role(773592142018510899)
        await ctx.author.add_roles(role)
        await ctx.send(f"Successfully created and assigned {role.mention}!")

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount+1)


client.run('token')