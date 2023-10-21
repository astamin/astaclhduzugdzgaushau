import discord
from discord.ext import commands
import requests
from time import sleep
from datetime import datetime
import time 
import random
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
def login(user , passw):
  time = int(datetime.now().timestamp())
  url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
  payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{passw}',
  'optIntoOneTap': 'false',
  'queryParams': {},
  'username': user}
  files=[

]
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
  session = requests.Session()
  session.headers.update(headers)
  getcsrf = session.post(url, data=payload , files=files)

  global csrf
  csrf=getcsrf.cookies["csrftoken"]
  global sid
  headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'X-Csrftoken': f'{csrf}',
  'Cookie': f"csrftoken={csrf}; mid=ZIrEtgALAAE7GrCUwQ9wcQbbrefW; ig_did=80445D30-C9F9-4D3F-8BF0-78B39275775C; ig_nrcb=1; datr=tcSKZFMeDkyjVKNghYr_9-WI"
}

  session = requests.Session()

  session.headers.update(headers)
  getsid = session.post(url , payload )
  global x
  x = getsid.json()

  if x["status"]=="ok" and x["authenticated"]!=None and x["authenticated"]==True:
        sid = getsid.cookies['sessionid']
        return True
  else :
        return False
def swapuser(csrf , sid , email , claim ,username ) :
  url = 'https://www.instagram.com/api/v1/web/accounts/edit/'
  urljj = f'https://www.instagram.com/{username}/?__a=1&__d=dis'
  jss = requests.get(urljj ).json()
  data = jss["graphql"]["user"]
  full_name=data["full_name"]
  headers = {
                  'X-Csrftoken': f'{csrf}',
                  'Cookie': f"ig_did=29F806F6-618B-4AEE-AB10-3135FEFC0ADF; ig_nrcb=1; mid=ZKiWsQALAAHpZUSVh1zhvRB_rjKw; datr=r5aoZPJ_i4dQ4KOxwb85x848; oo=v1; csrftoken={csrf}; dpr=1.25; sessionid={sid};"
              }
  dat  = {
              'first_name': full_name ,
          " chaining_enabled": "on",
              "email" : email,
              "biography": 'close ur tool baby , Asta here ' ,
              "username" : claim

          }
  global start
  session = requests.Session()

  session.headers.update(headers)
  start = session.post(url, data=dat).json()
  if start['status']=="ok":
        return True
  else :
        return False
def checker(claim):
  urlcheck = f'https://www.instagram.com/{claim}/?__a=1&__d=dis'
  session = requests.session()
  checker = session.get(urlcheck).status_code
  if checker == 404 :
      return True
  else :
      return False
@bot.event
async def on_ready():
    print("Bot connected")
@bot.command()
async def ping(ctx):
    lat = round(bot.latency * 1000)
    await ctx.send(f'Pong ! {lat} ms.')
@bot.command()
async def check(ctx , * ,question) :
    url = f'https://www.instagram.com/{question}/?__a=1&__d=dis'
    r = requests.get(url).status_code
    if r ==404 :
        await ctx.send(f'@{question} is available ')
    else :
        await ctx.send(f'@{question} is taken')

@bot.command()
async def log(ctx , * , crede) :
    first = time.time()
    parts = crede.split(":")
    if len(parts) == 4 :
        user =parts[0]
        password = parts[1]
        email =parts[2]
        newuser = parts[3]
        checkuser1 = checker(newuser)
        attempts = 0
        if checkuser1 :
            await ctx.send(f'@{newuser} is available')
            if login(user , password) :
                await ctx.send(f"Log in to @{user} was succesful")
                claimuser = swapuser(csrf  ,sid , email , newuser , user)
                attempts +=1
                if claimuser :
                    finish = time.time()
                    username1 = checker(newuser)
                    if username1 :
                        await ctx.send(f'Username was not taken due to a problem check and lmao')
                    else :
                        await ctx.send(f'- Username : @{newuser}\n-Attempts : {attempts} \n Time : {finish - first} Sec  \n > Dev tg : https://t.me//TELLLONYM ')
                else :
                    while not claimuser :
                        attempts +=1
                        claimuser1 = swapuser(csrf  ,sid , email , newuser , user)
                        if claimuser1 :
                            finish = time.time()
                            username = checker(newuser)
                            if username :
                                await ctx.send(f'Username was not taken due to a problem check and lmao')
                            else :
                                await ctx.send(f'- Username : @{newuser}\n-Attempts : {attempts} \n Time : {finish - first} Sec \n > Dev tg : https://t.me//TELLLONYM ')

            else :
                await ctx.send(f"Credentiels of @{user} is failed ")
        else :
            
            checkuser2 = checker(newuser)
            attempts += 1
            now = time.time()
            st = await ctx.send(f'@{newuser} Is taken \n-Attempts : {attempts} \n Time : {now - first} \n > Dev tg : https://t.me//TELLLONYM')
            while not checkuser2 :
                now = time.time()
                attempts += 1
                await st.edit(content=f'@{newuser} Is taken \n-Attempts : {attempts} \n Time : {now - first} \n > Dev tg : https://t.me//TELLLONYM')
                checkuser3 = checker(newuser)
                if checkuser3 :
                    checklogin2 = login(user , password)
                    if checklogin2 :
                        await ctx.send(f"Log in to @{user} was succesful")
                        claimuser3 = swapuser(csrf , sid ,email ,newuser , user)
                        if claimuser3 :
                            finish = time.time()
                            username2 = checker(newuser)
                            if username2 :
                                await ctx.send(f'Username was not taken due to a problem check and lmao')
                            else :
                                await ctx.send(f'- Username : @{newuser}\n-Attempts : {attempts} \n Time : {finish - first} Sec  \n > Dev tg : https://t.me//TELLLONYM ')
                        else :
                            while not claimuser3 :
                                attempts +=1
                                claimuser4 = swapuser(csrf  ,sid , email , newuser , user)
                                if claimuser4 :
                                    finish = time.time()
                                    username3 = checker(newuser)
                                    if username3 :
                                        await ctx.send(f'Username was not taken due to a problem check and lmao')
                                    else :
                                        await ctx.send(f'- Username : @{newuser}\n-Attempts : {attempts} \n Time : {finish - first} Sec  \n > Dev tg : https://t.me//TELLLONYM')
                    else :
                        await ctx.send(f'Credentiels of @{user} are incorrect ')
                else :
                    attempts +=1


bot.run("MTE2NTM4Mjk2NDMxMDQ1NDMyNQ.G0DXpg.OXIQBlk1OBmw4YKmZG1vM2FRKVsB3OiehAXyyU")