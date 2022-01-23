import discord
import asyncio
from discord import client, guild, message, Guild
from discord.ext import commands
import discord.emoji
import random

print("Il bot si sta avviando")

token = "OTM0NzU5NjQyNjE2MTkzMTI1.Ye0wwQ.srD53upveeNMze_2gQ9xjWZiPvM"


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print(client.user, "E ora ONLINE ", " (ID ", client.user.id, ")")

zone = "Per essere aggiunti all' asta scrivere in privato a Resting3 su discord"





@client.command()
async def start(ctx):

    a2 = ctx.author.id
    datastart = open(f"{a2}.txt", "r")
    dera = datastart.read()
    dera = int(dera)
    if dera > 1:
        embed = discord.Embed(title="Attenzione :warning:", description="Hai gia iniziato un avventura", color=0x00bb2d)
        await ctx.send(embed=embed)
    else:
        datastart = open(f"{ctx.author.id}.txt", "w")
        embed = discord.Embed(title="Hai iniziato una nuova avventura!", description="La tua avventura ha inizio fai !helps per info", color=0x00bb2d)
        embed.set_footer(text="Una produzione di Resting#3366",icon_url="https://cdn.discordapp.com/attachments/716910669416497193/934771232581222440/Immagine_2022-01-23_122648.png")
        await ctx.send(embed=embed)
        datastart.write("0")
        datastartinv = open(f"{ctx.author.id}inv.txt", "w")
        datastartinv.write(" ")




@start.error
async def start_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        datastart = open(f"{ctx.author.id}.txt", "w")
        embed = discord.Embed(title="Hai iniziato una nuova avventura!", description="La tua avventura ha inizio fai !helps per info", color=0x00bb2d)
        await ctx.send(embed=embed)
        datastart.write("0")
        datastartinv = open(f"{ctx.author.id}inv.txt", "w")
        datastartinv.write(" ")
































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
    embed.add_field(name="!inventario",value='Questo comando permette di vedere che farmer hai nell inventario / Creare un nuovo inventario')
    embed.add_field(name="!pay",value='Questo comando permette di pagare qualcun altro')








    await ctx.send(embed=embed)




















@client.command()
async def farm(ctx,io):








    if io == "domi99":



        ar = open(f"{ctx.author.id}.txt", "r")
        a = (ar.read())
        ar.close()
        a = int(a)



        ars = open(f"{ctx.author.id}inv.txt","r")
        arr = (ars.read())



        if not arr.startswith('domi99'):
                print("ciao")
                embed = discord.Embed(title=":warning: Errore", description="Non possiedi domi99", color=0xff0000)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                ago = False



        else:
                print("a")
                ago = True


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
                        eh = open(f"{ctx.author.id}.txt", "w")
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

        ar = open(f"{ctx.author.id}.txt","r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)






        br = open(f"{ctx.author.id}inv.txt", "r")

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



                if t > 1800:
                    eh = open(f"{ctx.author.id}.txt", "w")
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

        ar = open(f"{ctx.author.id}.txt", "r")

        aa = (ar.read())



        ar.close()

        a = int(aa)

        br = open(f"{ctx.author.id}inv.txt", "r")

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

                if t > 10800:
                    eh = open(f"{ctx.author.id}.txt", "w")

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

        ar = open(f"{ctx.author.id}.txt","r")
        aa = (ar.read())
        print(aa)
        ar.close()
        a = int(aa)



        br = open(f"{ctx.author.id}inv.txt", "r")
        ba = br.readlines()

        b3 = False
        b4 = False

        for line in ba:
            if line == "iperster":
                b3 = True
            else:
                b4 = True









        if b3 == True:

            embed = discord.Embed(title="<:wheat:934103851093598268> Farm <:wheat:934103851093598268>",description="Stai farmando dischi <:disco:934744646737883168>    \n <:clock0:934105590127546439> **Durata: **3h \n <:steve1:934107480445829182> Farmer: **Iperster** ",color=0x00bb2d)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/716910669416497193/934744987172753458/download_4.png")
            await ctx.send(embed=embed)

            t = 0
            fr = 0
            b4 = False

            while True:


                t = t + 1

                await asyncio.sleep(1)
                fr = fr + 6
                a = int(a)



                if t > 10800:
                    eh = open(f"{ctx.author.id}.txt", "w")
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
async def bal(ctx):
    bala = open(f"{ctx.author.id}.txt","r")
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
    embed.add_field(name=":x:Altri farmer :x:",value=":x:Ci saranno altri farmer prossimamente...:x:",inline=True)
    embed.set_footer(text="Per comprare un farmer !buy {nome del farmer}")
    await ctx.send(embed=embed)



@client.command()
async def buy(ctx,farmerss):
    if farmerss == "domi99":

        sld = open(f"{ctx.author.id}.txt","r")
        sold = sld.readline()

        sold = int(sold)

        agv = open(f"{ctx.author.id}inv.txt","r")

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
                ard = open(f"{ctx.author.id}.txt", "w")
                tota = sold - 12000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.id}inv.txt", "w")

                anv.write("\ndomi99")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ", description="**Hai acquistato domi99 con successo**",
                                      color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",
                                      description="** :warning: Non hai abbastanza soldi per poterlo comprare**", color=0xcb3234)
                await ctx.send(embed=embed)





    elif farmerss == "nonnaposseduta":
        sld = open(f"{ctx.author.id}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.id}inv.txt","r")










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
                ard = open(f"{ctx.author.id}.txt", "w")
                tota = sold - 28000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.id}inv.txt", "a")

                anv.write("\nnonnaposseduta")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato nonnaposseduta con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)


    elif farmerss == "skyppiexd":
        sld = open(f"{ctx.author.id}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.id}inv.txt","r")










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
                ard = open(f"{ctx.author.id}.txt", "w")
                tota = sold - 50000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.id}inv.txt", "a")

                anv.write("\nskyppiexd")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato skyppiexd con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)

    elif farmerss == "iperster":
        sld = open(f"{ctx.author.id}.txt", "r")
        sold = sld.readline()

        sold = int(sold)


        agv = open(f"{ctx.author.id}inv.txt","r")










        abrs = False


        for i in agv:
            if not i.startswith('iperster'):
                abrs = True

            else:
                embed = discord.Embed(title=" :warning: Errore", description="Hai gia in possesso iperster ", color=0xff0000)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)
                abrs = False
                break




        if abrs == True:
            if sold > 70000:
                sld.close()
                ard = open(f"{ctx.author.id}.txt", "w")
                tota = sold - 50000
                tota = str(tota)
                ard.write(tota)
                ard.close()

                anv = open(f"{ctx.author.id}inv.txt", "a")

                anv.write("\niperster")

                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description="**Hai acquistato iperster con successo**",color=0x00bb2d)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Non hai abbastanza soldi per poterlo comprare**",color=0xcb3234)
                await ctx.send(embed=embed)
                await asyncio.sleep(2)
                await ctx.channel.purge(limit=1)





















    else:
        embed = discord.Embed(title="Negozio Farmers :shopping_cart: ",description=" **:warning: Quel farmer non esiste**",color=0xcb3234)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)









@client.command()
async def inventario(ctx):
    derf = open(f"{ctx.author.id}inv.txt","r")
    derif = (derf.read())
    embed = discord.Embed(title="Inventario", description=" ", color=0x91672c)
    embed.add_field(name="Farmer:",value=f"**{derif}**",inline=False)
    await ctx.send(embed=embed)





@inventario.error
async def inventario_error(ctx, error):
    if isinstance(error, commands.errors.CommandInvokeError):
        dery = open(f"{ctx.author.id}inv.txt","w")
        dery.write(" ")
        embed = discord.Embed(title="Inventario", description="Hai creato un nuovo inventario!", color=0x91672c)
        ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)













@client.command()
async def pay(ctx,member:discord.Member,amount:int):





    hserver = open(f"{ctx.author.id}.txt","r")

    hserve = (hserver.read())
    hserve = int(hserve)


    if hserve < amount:
        embed = discord.Embed(title="Attenzione",description="Non hai abbastanza <:emerald:934109661932683284> per effettuare la transizione",colour=discord.Colour.red())
        await ctx.send(embed=embed)
    else:

        hserve = str(hserve)

        hserver.close()
        hserve = int(hserve)

        hsertot = hserve - amount
        hsertot = str(hsertot)
        hserver1 = open(f"{ctx.author.id}.txt", "w")
        hserver1.write(hsertot)
        hserver1.close()

        hclient = open(f"{member.id}.txt", "r")
        hcread = (hclient.read())
        hclient.close()

        hcread = int(hcread)

        hsctot = hcread + amount

        hclient1 = open(f"{member.id}.txt", "w")
        hsctot = str(hsctot)
        hclient1.write(hsctot)
        hclient1.close()
        embed = discord.Embed(title="Pay", description=f"Hai pagato {member.mention} {amount}<:emerald:934109661932683284>  ", color=0x01ffff)
        await ctx.send(embed=embed)







@client.command()
async def scam(ctx):
    rh = open(f"{ctx.author.id}.txt","r")
    ar = (rh.read())
    ae = random.randint(1,1000)
    embed = discord.Embed(title="Truffa :clown: ", description=f"Hai truffato uno starter  <:steve1:934107480445829182> e hai guadagnato {ae}<:emerald:934109661932683284>  ", color=0x00bb2d)
    await ctx.send(embed=embed)
    arre = ar + ae
    rh.close()
    arre = str(arre)
    ij = open(f"{ctx.author.id}.txt","w")
    ij.write(arre)




















































client.run(token)