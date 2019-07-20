# -*- coding: utf-8 -*- 

import os
import sys
import asyncio
import discord
import datetime
import random
import math
from discord.ext import commands
from gtts import gTTS
from github import Github
import base64

if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

basicSetting = []
bossData = []
fixed_bossData = []

bossNum = 0
fixed_bossNum = 0
chkvoicechannel = 0
chkrelogin = 0
chflg = 0
LoadChk = 0

bossTime = []
tmp_bossTime = []

fixed_bossTime = []

bossTimeString = []
bossDateString = []
tmp_bossTimeString = []
tmp_bossDateString = []

bossFlag = []
bossFlag0 = []
bossMungFlag = []
bossMungCnt = []

channel_info = []
channel_name = []
channel_id = []
channel_voice_name = []
channel_voice_id = []
channel_type = []

client = discord.Client()

access_token = os.environ["BOT_TOKEN"]			
git_access_token = os.environ["GIT_TOKEN"]			
git_access_repo = os.environ["GIT_REPO"]			
git_access_repo_restart = os.environ["GIT_REPO_RESTART"]			

g = Github(git_access_token)
repo = g.get_repo(git_access_repo)
repo_restart = g.get_repo(git_access_repo_restart)




@client.event
async def on_reday():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("마슈 출근했어"):
        await message.channel.send("오늘 하루도 힘내요, 선배!")

    if message.content.startswith("마슈 안녕"):
        await message.channel.send("안녕하세요, 선배!")

    if message.content.startswith("마슈 귀여워"):
        await message.channel.send("감, 감사합니다......")

    if message.content.startswith("마슈 고마워"):
        await message.channel.send("좀 더 선배의 도움이 될 수 있도록, 노력하겠습니다.")

    if message.content.startswith("마슈 퇴근했어"):
        await message.channel.send("수고하셨어요, 선배.")

    if message.content.startswith("마슈 생일축하해줘"):
        await message.channel.send("생일 축하해요. 매우 경사스러우니, 국가적 기념일로 삼아야 하지 않을까요?")

    if message.content.startswith("마슈 도와줘"):
            await message.channel.send("전력으로 응원하겠습니다, 선배!")

    if message.content.startswith("마슈 잘자"):
            await message.channel.send("좋은 꿈 꾸세요, 선배.")

    if message.content.startswith("성정편"):
        await message.channel.send("캇킹~, 팟~칭.... 앗, 괜찮습니다. 귀중한 자원을 가지고 놀았던 게 아닙니다...아니에요?")



    if message.content.startswith('골라줘'):
        choice = message.content.split(" ")
        choiceNum = random.randint(1, len(choice) - 1)
        choiceResult = choice[choiceNum]
        await message.channel.send("저는 " + choiceResult + " 이(가) 좋다고 생각해요, 선배.")

    if message.content.startswith('메뉴 추천'):
        # category = "중식, 일식, 분식, 치킨, 피자, 햄버거"
        food = "피자 햄버거 치킨 라면 백반 돈까스 제육 우동 김치찌개 된장찌개 순두부찌개 부대찌개 육개장 쫄면 콩국수 냉면 김밥 메밀소바 짜장면 짬뽕 볶음밥 짬뽕밥 오므라이스 잡채밥 삼겹살 곱창 족발 보쌈 찜닭 회 떡볶이 비빔밥 설렁탕 순대국 굶는게"
        foodChoice = food.split(" ")
        foodNum = random.randint(0, len(foodChoice) - 1)
        foodResult = foodChoice[foodNum]
        await message.channel.send("오늘은 " + foodResult + " 어떠세요, 선배?")



    if message.content.startswith("프로필"):
        if not message.mentions:
            await message.channel.send(message.author.mention + " 프로필 [유저언급] 의 형태로 입력해주세요")
        else:
            embed = discord.Embed(title="프로필 사진.", color=0xD358F7)
            embed.set_image(url=message.mentions[0].avatar_url)
            await message.channel.send(embed=embed)


client.run(access_token)
