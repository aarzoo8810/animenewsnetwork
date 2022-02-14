from discord.ext import commands
import requests
import requests
from bs4 import BeautifulSoup
import asyncio
import discord
from datetime import date

bot = commands.Bot(command_prefix="!")


async def timer():
    await bot.wait_until_ready()
    channel = bot.get_channel(941015985438216243)
    msg_sent = False
    
    while True:
        base_link = 'https://www.animenewsnetwork.com/'
        # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
        req = requests.get(base_link)
        soup = BeautifulSoup(req.text, 'lxml')

        news_cards = soup.find_all('div', class_="herald box news")
        review_cards = soup.find_all('div', class_="herald box reviews")
        interest_cards = soup.find_all('div', class_="herald box interest")

        for news_card in news_cards:
            # find heading
            news_heading = news_card.find('h3')
            news_heading_text = news_heading.text.strip()
            print(news_heading_text)


            # Find link of the news
            half_link = news_heading.a['href']
            links = base_link + half_link

            # find image link
            thumbnail = news_card.find('div', class_="thumbnail")
            img_link = base_link + thumbnail.attrs['data-src']

            # find time
            time_tag = news_card.find('time')
            time = time_tag.attrs['datetime'].split('T')[0]

            # scrape preview
            preview = news_card.find('div', class_="preview").text.strip()

            with open('/home/rzoo/vs code/practice/animenews.txt', 'r') as f:
                      if links not in f.read() and time == str(date.today()):
                        embed = discord.Embed(title=news_heading_text, url=links, description=preview)
                        embed.set_image(url=img_link)
                        with open('animenews.txt', 'a') as f:
                           f.write(links + '\n')
                           await channel.send(embed=embed)
                      else:
                          msg_sent=False



        for review_card in review_cards:
            # find heading
            review_heading = review_card.find('h3')
            review_heading_text = review_heading.text.strip()
            print(review_heading_text)

            # Find link of the news
            review_half_link = review_heading.a['href']
            review_links = base_link + review_half_link

            # find image link
            review_thumbnail = review_card.find('div', class_="thumbnail")
            review_img_link = base_link + review_thumbnail.attrs['data-src']

            # find time
            review_time_tag = review_card.find('time')
            review_time = review_time_tag.attrs['datetime'].split('T')[0]

            # scrape preview
            review_preview = review_card.find('div', class_="preview").text.strip()

            with open('/home/rzoo/vs code/practice/animereviews.txt', 'r') as f:
                      if review_links not in f.read() and review_time == str(date.today()):
                        review_embed = discord.Embed(title=review_heading_text, url=review_links, description=review_preview)
                        review_embed.set_image(url=review_img_link)
                        with open('animereviews.txt', 'a') as f:
                           f.write(review_links + '\n')
                           await channel.send(embed=review_embed)
                      else:
                          msg_sent=False


        for interest_card in interest_cards:
            # find heading
            interest_heading = interest_card.find('h3')
            interest_heading_text = interest_heading.text.strip()

            # Find link of the news
            interest_half_link = interest_heading.a['href']
            interest_links = base_link + interest_half_link

            # find image link
            interest_thumbnail = interest_card.find('div', class_="thumbnail")
            interest_img_link = base_link + interest_thumbnail.attrs['data-src']

            # find time
            interest_time_tag = interest_card.find('time')
            interest_time = interest_time_tag.attrs['datetime'].split('T')[0]

            # scrape preview
            interest_preview = interest_card.find('div', class_="preview").text.strip()

            with open('/home/rzoo/vs code/practice/animeinterest.txt', 'r') as f:
                      if interest_links not in f.read() and interest_time == str(date.today()):
                        interest_embed = discord.Embed(title=interest_heading_text, url=interest_links, description=interest_preview + '\n' + 'tag: interest')
                        interest_embed.set_image(url=interest_img_link)
                        with open('animeinterest.txt', 'a') as f:
                           f.write(interest_links + '\n')
                           await channel.send(embed=interest_embed)
                      else:
                          msg_sent=False

          

              

    await asyncio.sleep(2)
                    
bot.loop.create_task(timer())
bot.run('OTQxMDA1ODE1MzQ1NzQxODI0.YgPp9Q.9C4vdbDxj9sr7mc6Kds6pJHkpIY')