import discord
import asyncio
from discord import client, guild, message, Guild
from discord.ext import commands
import discord.emoji
import random

print("Il bot si sta avviando")

token = ""


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(client.user, "E ora ONLINE ", " (ID ", client.user.name, ")")

zone = "Per essere aggiunti all' asta scrivere in privato a Resting3 su discord"






@client.command()
async def start(ctx):

    a2 = ctx.author.name
    datastart = open(f"{a2}.txt", "r")
    dera = datastart.read()
    dera = int(dera)
    if dera > 1:
        embed = discord.Embed(title="Attenzione :warning:", description="Hai gia iniziato un avventura", color=0x00bb2d)
        await ctx.send(embed=embed)
    else:
        datastart = open(f"{ctx.author.name}.txt", "w")
        embed = discord.Embed(title="Hai iniziato una nuova avventura!", description="La tua avventura ha inizio fai !helps per info", color=0x00bb2d)
        embed.set_footer(text="Una produzione di Resting#3366",icon_url="https://cdn.discordapp.com/attachments/716910669416497193/934771232581222440/Immagine_2022-01-23_122648.png")
        await ctx.send(embed=embed)
        dataserver = open(f"datacentral.txt", "w")
        dataserver.write(f"{ctx.author.name}.txt")
        datastart.write("0")
        datastartinv = open(f"{ctx.author.name}inv.txt", "w")
        datastartinv.write(" ")




@start.error
async def start_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        datastart = open(f"{ctx.author.name}.txt", "w")
        embed = discord.Embed(title="Hai iniziato una nuova avventura!", description="La tua avventura ha inizio fai !helps per info", color=0x00bb2d)
        await ctx.send(embed=embed)
        datastart.write("0")
        dataserver = open(f"datacentral.txt", "w")
        dataserver.write(f"{ctx.author.name}")
        datastartinv = open(f"{ctx.author.name}inv.txt", "w")
        datastartinv.write(" ")










@client.command()
async def price(ctx):
    embed = discord.Embed(title="Premi",description="Premi per chi vince la sfnamea", color=0x0000ff)
    embed.add_field(name="Primo premio",value='10 milioni')
    embed.add_field(name="Secondo premio",value='5 milioni')
    embed.add_field(name="Terzo premio",value='3 milioni')







@client.command()
async def helps(ctx):
    embed = discord.Embed(title="Help",description="La tua avventura ha inizio fai /help per info", color=0x0000ff)
    embed.add_field(name="Scopo",value='Lo scopo di questo mini-gioco e quello di farmare soldi')
    embed.add_field(name="!start",value='Inizia una nuova avventura')
    embed.add_field(name="!bal",value='Questo comando permette di controllare quanti soldi hai')
    embed.add_field(name="!farm", value='Questo comando permette di farmare soldi e scegliere opzionalmente il farmer')
    embed.add_field(name="!buy",value='Questo comando permette di comprare i farmers')
    embed.add_field(name="!farmers",value='Questo comando permette di vedere i farmers comprabili')
    embed.add_field(name="!scam", value='Questo comando permette di truffare gli starter :)')
    embed.add_field(name="!kaboom", value='Questo comando permette di truffare i competenti :)')
    embed.add_field(name="!inventario",value='Questo comando permette di vedere che farmer hai nell inventario / Creare un nuovo inventario')
    embed.add_field(name="!pay",value='Questo comando permette di pagare qualcun altro')








    await ctx.send(embed=embed)




















@client.command()
async def farm(ctx,io):








    if io == "domi99":



        ar = open(f"{ctx.author.name}.txt", "r")
        a = (ar.read())
        ar.close()
        a = int(a)



        ars = open(f"{ctx.author.name}inv.txt","r")



        arr = ars.read()

        if "domi99" in arr:
            ago = True
        else:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi domi99", color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
            ago = False




        if ago == True:

                embed = discord.Embed(title=" <:wheat:934103851093598268> Farm <:wheat:934103851093598268>",description="Stai farmando mele op  <:golden_apple:934097889200844830>   \n <:clock0:934105590127546439> **Durata: **10m \n <:steve1:934107480445829182> Farmer: **Domi99** ",color=0x00bb2d)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/930874409718259772/934106848225792070/download.png")
                await ctx.send(embed=embed)

                t = 0

                while True:


                    t = t + 1


                    await asyncio.sleep(1)
                    fr = fr + 2


                    a = int(a)

                    if t > 600:
                        eh = open(f"{ctx.author.name}.txt", "w")
                        embed = discord.Embed(title="Il farmer domi99 ha finito!", description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284>", color=0xd4af37)
                        await ctx.send(embed=embed)
                        frtot = a+ fr
                        frtot = str(frtot)
                        eh.write(frtot)

                        await asyncio.sleep(2)
                        await ctx.channel.purge(limit=1)
                        break
                    else:
                        pass








    elif io == "nonnaposseduta":

        ar = open(f"{ctx.author.name}.txt","r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)






        br = open(f"{ctx.author.name}inv.txt", "r")

        ba = br.read()



        b3 = False


        b4 = False

        hh = "nonnaposseduta"

        if hh in ba:
            b3 = True
        else:
            b4 = True











        if b3 == True:

            embed = discord.Embed(title=" <:wheat:934103851093598268> Farm <:wheat:934103851093598268>",
                                  description="Stai aprendo foodkey  :key:    \n <:clock0:934105590127546439> **Durata: **30m \n <:steve1:934107480445829182> Farmer: **NonnaPosseduta** ",
                                  color=0x00bb2d)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/882650629959483403/934396392644939776/2022-01-21_20.57.19.png")
            await ctx.send(embed=embed)

            t = 0
            fr = 0
            b4 = False

            while True:


                t = t + 1

                await asyncio.sleep(1)
                fr = fr + 2
                a = int(a)



                if t > 600:
                    eh = open(f"{ctx.author.name}.txt", "w")
                    embed = discord.Embed(title="La farmer NonnaPosseduta ha finito!", description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284> ",color=0xd4af37)
                    await ctx.send(embed=embed)
                    frtot = a + fr
                    frtot = str(frtot)
                    eh.write(frtot)
                    break


        if b4 == True:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi nonnaposseduta", color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)




    elif io == "skyppiexd":

        ar = open(f"{ctx.author.name}.txt", "r")

        aa = (ar.read())



        ar.close()

        a = int(aa)

        br = open(f"{ctx.author.name}inv.txt", "r")

        ba = br.read()



        b3 = False


        b4 = False

        hh = "skyppiexd"

        if hh in ba:
            b3 = True
            print("ya")
        else:
            b4 = True






        if b3 == True:
            embed = discord.Embed(title="<:wheat:934103851093598268> Farm <:wheat:934103851093598268>",description="Stai schiavizzando KappaMa <:kappa:934732320051699743> mentre farmi patate velenose <:poisonous_potato:934729648594645033>    \n <:clock0:934105590127546439> **Durata: **2h \n <:steve1:934107480445829182> Farmer: **Skyppiexd** ",color=0x00bb2d)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716910669416497193/934730910757175316/download_2.png")



            await ctx.send(embed=embed)

            t = 0

            fr = 0

            b4 = False

            while True:

                t = t + 1

                await asyncio.sleep(1)

                fr = fr + 6

                a = int(a)

                if t > 600:
                    eh = open(f"{ctx.author.name}.txt", "w")

                    embed = discord.Embed(title="Il farmer skyppiexd ha finito!",
                                          description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284> ",
                                          color=0xd4af37)

                    await ctx.send(embed=embed)

                    frtot = a + fr

                    frtot = str(frtot)

                    eh.write(frtot)

                    break

        if b4 == True:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi skyppiexd", color=0xff0000)

            await ctx.send(embed=embed)

            await asyncio.sleep(2)

            await ctx.channel.purge(limit=1)





    elif io == "iperster":

        ar = open(f"{ctx.author.name}.txt","r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)



        br = open(f"{ctx.author.name}inv.txt", "r")
        ba = br.read()

        b3 = False
        b4 = False


        if "iperster" in ba:
            b3 = True
        else:
            b4 = False













        if b3 == True:

            embed = discord.Embed(title="<:wheat:934103851093598268> Farm <:wheat:934103851093598268>",description="Stai farmando dischi <:disco:934744646737883168>    \n <:clock0:934105590127546439> **Durata: **3h \n <:steve1:934107480445829182> Farmer: **Iperster** ",color=0x00bb2d)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716910669416497193/934744987172753458/download_4.png")
            await ctx.send(embed=embed)

            t = 0
            fr = 0
            b4 = False

            while True:


                t = t + 1

                await asyncio.sleep(0.2)
                fr = fr + 6
                a = int(a)



                if t > 600:
                    eh = open(f"{ctx.author.name}.txt", "w")
                    embed = discord.Embed(title="Il farmer Iperster ha finito!", description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284> ",color=0xd4af37)
                    await ctx.send(embed=embed)
                    frtot = a + fr
                    frtot = str(frtot)
                    eh.write(frtot)
                    break

        if b4 == True:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi Iperster", color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)






    elif io == "st3pny":

        ar = open(f"{ctx.author.name}.txt","r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)



        br = open(f"{ctx.author.name}inv.txt", "r")
        ba = br.read()

        b3 = False
        b4 = False



        if "st3pny" in  ba:
            b3 = True
        else:
            b4 = True








        if b3 == True:

            embed = discord.Embed(title="<:wheat:934103851093598268> Farm <:wheat:934103851093598268>",description="Stai schiavizzando domi99 mentre vendi tear ghast    \n <:clock0:934105590127546439> **Durata: **3h \n <:steve1:934107480445829182> Farmer: **St3pny** ",color=0x00bb2d)
            embed.add_field(name="St3pny azione",value="St3pny ha percosso domi99 e ha trovato 3000 <:emerald:934109661932683284>")

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716910669416497193/934744987172753458/download_4.png")
            await ctx.send(embed=embed)

            t = 0
            fr = 0
            b4 = False

            while True:


                t = t + 1

                await asyncio.sleep(0.2)
                fr = fr + 10
                a = int(a)



                if t > 600:
                    eh = open(f"{ctx.author.name}.txt", "w")
                    embed = discord.Embed(title="Il farmer st3pny ha finito!", description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284> ",color=0xd4af37)
                    await ctx.send(embed=embed)
                    frtot = a + fr + 3000
                    frtot = str(frtot)
                    eh.write(frtot)
                    break












        if b4 == True:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi st3pny", color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)



    elif io == "stef135":

        ar = open(f"{ctx.author.name}.txt", "r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)

        br = open(f"{ctx.author.name}inv.txt", "r")
        ba = br.read()

        b3 = False
        b4 = False


        if "stef135" in ba:
            b3 = True
        else:
            b4 = True



        if b3 == True:

            embed = discord.Embed(title="<:wheat:934103851093598268> Farm <:wheat:934103851093598268>",
                                  description="Stai fottendo l' intera economia della skyblock \n <:clock0:934105590127546439> **Durata: **5h \n <:steve1:934107480445829182> Farmer: **stef135** ",
                                  color=0x00bb2d)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/716910669416497193/934844547337437234/download_5.png")
            await ctx.send(embed=embed)

            t = 0
            fr = 0
            b4 = False

            while True:

                t = t + 1

                await asyncio.sleep(0.1)
                fr = fr + 12
                a = int(a)

                if t > 1200:
                    eh = open(f"{ctx.author.name}.txt", "w")
                    embed = discord.Embed(title="Il farmer stef135 ha finito!",description=f"Hai guadagnato **{fr}**<:emerald:934109661932683284> ",color=0xd4af37)
                    embed.add_field(name="Nuovo scam",value="Stef e riuscito a truffare 10 player con un guadagno di **5000**<:emerald:934109661932683284> ",inline=True)



                    await ctx.send(embed=embed)
                    frtot = a + fr + 5000
                    frtot = str(frtot)
                    eh.write(frtot)
                    break

        if b4 == True:
            embed = discord.Embed(title=":warning: Errore", description="Non possiedi stef135", color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)










    else:
        embed = discord.Embed(title=" <:wheat:934103851093598268> Farm <:wheat:934103851093598268>",
                                      description="Farmer inesistente ", color=0x00bb2d)
        await ctx.send(embed=embed)






@farm.error
async def farm_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title=" <:wheat:934103851093598268> Farm <:wheat:934103851093598268>", description="Stai farmando mele op  <:golden_apple:934097889200844830>   \n <:clock0:934105590127546439> **Durata: **5m", color=0x00bb2d)
        await ctx.send(embed=embed)



@client.command()
async def bal(ctx,member:discord.Member):
    bala = open(f"{member.name}.txt","r")
    resobal = bala.readline()

    embed1 = discord.Embed(title=" <:diamond:934109715925987348> Bilancio <:diamond:934109715925987348>", description=f"Hai **{resobal}<:emerald:934109661932683284>**", color=0x00bb1d)
    await ctx.send(embed=embed1)



@bal.error
async def bal_error(ctx, error):
    bala = open(f"{ctx.author.name}.txt","r")
    resobal = bala.readline()
    embed1 = discord.Embed(title=" <:diamond:934109715925987348> Bilancio <:diamond:934109715925987348>", description=f"Hai **{resobal}<:emerald:934109661932683284>**", color=0x00bb1d)
    await ctx.send(embed=embed1)























@client.command()
async def farmers(ctx):
    embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="Compra i farmers", color=0xffff00    )
    embed.add_field(name=" <:wooden_hoe:934125433992147045> Farmer: **domi99**", value="**Costo: 12000<:emerald:934109661932683284>** \n <:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **2 volte** piu velocemente e dura **10 minuti**",inline=True)
    embed.add_field(name=" <:stone_hoe:934125446533099611> Farmer: **Nonnaposseduta**",value="**Costo: 28000<:emerald:934109661932683284>** \n <:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **2 volte** piu velocemente e la durata di farm e di **mezz' ora**",inline=True)
    embed.add_field(name=" <:iron_hoe:934125519912439818> Farmer: **Skyppiexd**",value="**Costo: 50000<:emerald:934109661932683284>** \n<:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **4 volte** piu velocemente e la durata di farm e di **2 ore** ",inline=True)
    embed.add_field(name=" <:golden_hoe:934125500656394371> Farmer: **Iperster**",value="**Costo: 70000<:emerald:934109661932683284>** \n<:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **6 volte** piu velocemente e la durata di farm e di **3 ore** ",inline=True)
    embed.add_field(name=" <:diamond_hoe:934125475134050354> Farmer: **St3pny**",value="**Costo: 90000<:emerald:934109661932683284>** \n<:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **10 volte** piu velocemente e la durata di farm e di **4  ore** ",inline=True)
    embed.add_field(name=" <:netherite_hoe:934125460584018000> Farmer: **stef135**",value="**Costo: 120000<:emerald:934109661932683284>** \n<:FrecciaVerde:934123701564211210>Boost: Si farmano soldi **12 volte** piu velocemente e la durata di farm e di **5  ore** ",inline=True)
    embed.add_field(name=":x:Altri farmer :x:",value=":x:Ci saranno altri farmer prossimamente...:x:",inline=True)
    embed.set_footer(text="Per comprare un farmer !buy {nome del farmer}")
    await ctx.send(embed=embed)




@client.command()
async def boost(ctx):
    embed = discord.Embed(title="Boost :shopping_cart: ",description="Compra i boosts", color=0xffff00    )
    embed.add_field(name="Biscotti di candies_f0rever", value="**Costo: 200000<:emerald:934109661932683284>** \n <:FrecciaVerde:934123701564211210>Ogni farmer farmera x10 volte ancora piu velocemente",inline=True)


















@client.command()
async def buy(ctx,farmerss):
    if farmerss == "domi99":

        sld = open(f"{ctx.author.name}.txt","r")
        sold = sld.readline()

        sold = int(sold)

        agv = open(f"{ctx.author.name}inv.txt","r")

        abrs = False

        agre = agv.read()

        if not "domi99" in agre:
            abrs = True


        else:
                embed = discord.Embed(title=":warning:Errore", description="Hai gia in possesso domi99", color=0xff0000)
                await ctx.send(embed=embed)
                await ctx.channel.purge(limit=1)
                abrs = False



        if abrs == True:
            if sold > 12000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 12000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "w")

                anv.write("\ndomi99")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ", description="**Hai acquistato domi99 con successo**",
                                      color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",
                                      description="** :warning: Non hai abbastanza soldi per poterlo comprare**", color=0xcb3234)
                await ctx.send(embed=embed)





    elif farmerss == "nonnaposseduta":
        sld = open(f"{ctx.author.name}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.name}inv.txt","r")










        abrs = False


        for i in agv:
            if not i.startswith('nonnaposseduta'):
                abrs = True

            else:
                embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso nonnaposseduta", color=0xff0000)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                abrs = False
                break




        if abrs == True:
            if sold > 28000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 28000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "a")

                anv.write("\nnonnaposseduta")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato nonnaposseduta con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)


    elif farmerss == "skyppiexd":
        sld = open(f"{ctx.author.name}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.name}inv.txt","r")










        abrs = False


        for i in agv:
            if not i.startswith('skyppiexd'):
                abrs = True

            else:
                embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso skyppiexd ", color=0xff0000)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                abrs = False
                break




        if abrs == True:
            if sold > 50000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 50000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "a")

                anv.write("\nskyppiexd")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato skyppiexd con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)

    elif farmerss == "iperster":
        sld = open(f"{ctx.author.name}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.name}inv.txt","r")








        ars = agv.read()

        if not "iperster" in ars:
            abrs = True

        else:
                embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso iperster ", color=0xff0000)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                abrs = False





        if abrs == True:
            if sold > 70000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 50000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "a")

                anv.write("\niperster")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato iperster con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)



    elif farmerss == "st3pny":
        sld = open(f"{ctx.author.name}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.name}inv.txt","r")

        ars = agv.read()

        if not "st3pny" in ars:
            abrs = True

        else:
            embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso st3pny ",
                                  color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
            abrs = False







        if abrs == True:
            if sold > 90000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 90000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "a")

                anv.write("\nst3pny")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato st3pny con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)




    elif farmerss == "stef135":
        sld = open(f"{ctx.author.name}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.name}inv.txt","r")

        ars = agv.read()

        if not "stef135" in ars:
            abrs = True

        else:
            embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso stef135 ",
                                  color=0xff0000)
            await ctx.send(embed=embed)
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
            abrs = False



        if abrs == True:
            if sold > 120000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 120000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "a")

                anv.write("\nstef135")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato stef135 con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)


    elif farmerss == "biscotto":

        sld = open(f"{ctx.author.name}.txt","r")
        sold = sld.readline()

        sold = int(sold)

        agv = open(f"{ctx.author.name}inv.txt","r")

        abrs = False

        agre = agv.read()

        if not "biscotto" in agre:
            abrs = True


        else:
                embed = discord.Embed(title=":warning:Errore", description="Hai gia in possesso biscotto", color=0xff0000)
                await ctx.send(embed=embed)
                await ctx.channel.purge(limit=1)
                abrs = False



        if abrs == True:
            if sold > 200000:
                sld.close()
                ard = open(f"{ctx.author.name}.txt", "w")
                tota = sold - 200000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.name}inv.txt", "w")

                anv.write("\nbiscotto")

                embed = discord.Embed(title="Boost :shopping_cart: ", description="**Hai acquistato biscotto con successo**",
                                      color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Boost :shopping_cart: ",
                                      description="** :warning: Non hai abbastanza soldi per poterlo comprare**", color=0xcb3234)
                await ctx.send(embed=embed)














    else:
        embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Quel farmer non esiste**",color=0xcb3234)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)









@client.command()
async def inv(ctx):
    derf = open(f"{ctx.author.name}inv.txt","r")
    derif = (derf.read())
    embed = discord.Embed(title="Inventario", description=" ", color=0x91672c)
    embed.add_field(name="Farmer:",value=f"**{derif}**",inline=False)
    embed.set_footer(text=f"Inventario di {ctx.author.name}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)





@inv.error
async def inv_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        dery = open(f"{ctx.author.name}inv.txt","w")
        dery.write(" ")
        embed = discord.Embed(title="Inventario", description="Hai creato un nuovo inventario!", color=0x91672c)
        ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)













@client.command()
async def pay(ctx,member:discord.Member,amount:int):

    if amount < 0:
        embed = discord.Embed(title="Pay", description=f"Non sono ammessi numeri negativi", color=0x01ffff)
        await ctx.send(embed=embed)
    else:
        hserver = open(f"{ctx.author.name}.txt", "r")

        hserve = (hserver.read())
        hserve = int(hserve)

        if hserve < amount:
            embed = discord.Embed(title="Attenzione",
                                  description="Non hai abbastanza <:emerald:934109661932683284> per effettuare la transizione",
                                  colour=discord.Colour.red())
            await ctx.send(embed=embed)
        else:

            hserve = str(hserve)

            hserver.close()
            hserve = int(hserve)

            hsertot = hserve - amount
            hsertot = str(hsertot)
            hserver1 = open(f"{ctx.author.name}.txt", "w")
            hserver1.write(hsertot)
            hserver1.close()

            hclient = open(f"{member.name}.txt", "r")
            hcread = (hclient.read())
            hclient.close()

            hcread = int(hcread)

            hsctot = hcread + amount

            hclient1 = open(f"{member.name}.txt", "w")
            hsctot = str(hsctot)
            hclient1.write(hsctot)
            hclient1.close()
            embed = discord.Embed(title="Pay",
                                  description=f"Hai pagato {member.mention} {amount}<:emerald:934109661932683284>  ",
                                  color=0x01ffff)
            await ctx.send(embed=embed)
















@client.command()
async def scam(ctx):
    rh = open(f"{ctx.author.name}.txt","r")
    ar = (rh.read())
    print(ar)
    aeh = int(ar)
    ae = random.randint(1,  1500)
    aeg = int(ae)
    embed = discord.Embed(title="Truffa :clown: ", description=f"Hai truffato uno starter  <:steve1:934107480445829182> e hai guadagnato {ae}<:emerald:934109661932683284>  ", color=0x00bb2d)
    await ctx.send(embed=embed)
    arre = aeg + int(ar)
    print(arre)
    arre = str(arre)
    ij = open(f"{ctx.author.name}.txt","w")
    ij.write(arre)


@client.command()
async def kaboom(ctx):

    ho = open(f"{ctx.author.name}inv.txt","r")
    he = ho.read()

    if "stef135" in he:
        rh = open(f"{ctx.author.name}.txt", "r")
        ar = (rh.read())
        print(ar)
        aeh = int(ar)
        ae = random.randint(1, 5500)
        aeg = int(ae)
        embed = discord.Embed(title="Truffa :clown: ",
                              description=f"Hai truffato 5 competenti  <:steve1:934107480445829182> e hai guadagnato {ae}<:emerald:934109661932683284>  ",
                              color=0xffff00)
        await ctx.send(embed=embed)
        arre = aeg + int(ar)
        print(arre)
        arre = str(arre)
        ij = open(f"{ctx.author.name}.txt", "w")
        ij.write(arre)
    else:
        embed = discord.Embed(title="Non hai il permesso ",
                              description=f"Non hai stef135 ",
                              color=0xffff00)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)



@client.command()
async def casino(ctx):
    ho = open(f"{ctx.author.name}inv.txt","r")
    he = ho.read()


    if "st3pny" in he:
        rh = open(f"{ctx.author.name}.txt", "r")
        ar = (rh.read())
        print(ar)
        aeh = int(ar)
        ae = random.randint(1, 40000)
        aeg = int(ae)
        embed = discord.Embed(title="Truffa :clown: ",
                              description=f"Hai vinto una scomessa <:steve1:934107480445829182> e hai guadagnato {ae}<:emerald:934109661932683284>  ",
                              color=0xffff00)
        await ctx.send(embed=embed)
        arre = aeg + int(ar)
        print(arre)
        arre = str(arre)
        ij = open(f"{ctx.author.name}.txt", "w")
        ij.write(arre)






































client.run(token)
