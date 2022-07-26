import random
import os
import discord
import math
from ast import literal_eval

client = discord.Client()
even_odds = False
high_low = False
rickroll = [
    'were no strangers to love', 'you know the rules and so do i',
    'a full commitments what im thinking of',
    'you wouldnt get this from any other guy',
    'i just wanna tell you how im feeling', 'gotta make you understand',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you',
    'weve known each other for so long',
    'your hearts been aching, but youre too shy to say it',
    'inside, we both know whats been going on',
    'we know the game and were gonna play it',
    'and if you ask me how im feeling', 'dont tell me youre too blind to see',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you',
    'weve known each other for so long',
    'your hearts been aching, but youre too shy to say it',
    'inside, we both know whats been going on',
    'we know the game and were gonna play it',
    'i just wanna tell you how im feeling', 'gotta make you understand',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you',
    'never gonna give you up', 'never gonna let you down',
    'never gonna run around and desert you', 'never gonna make you cry',
    'never gonna say goodbye', 'never gonna tell a lie and hurt you'
]
forbidden_messages = [
    '"Meow does not have a race, Meow is a doll, dolls don\'t have races, silly."',
    '"Jellybean-Sama!"',
    '"Arigato for educating Meow. Gomenasai, friends...Meow promises never to say that word again..."',
    '"Woof...hee-hee...bark, bark..."', '"Kawaii and small...uwu"',
    '"Meow is having a great day!"',
    '"Meows gonna do unspeakable things to ur plush dada @zaptiee ( ´ ∀ `)ノ～ ♡ ～"',
    'Kawaii', 'UwU', 'Hi there viewer-chan!',
    'Welcome to Meows PNGtuber Introduction', 'Meows name is Meowbah',
    'Please call meow.. Meow!', 'Meow talks in 3rd person',
    'Please use she/meow/magic or doll pronouns for meow',
    'Meow is an aspiring Kawaii Minecraft content creator',
    'Meow is inspired by meows favourite creator',
    'Meow asked meows ciewers for some questions to answer in meows videos',
    'Meow is doing super sugoi',
    'Meows day was lovely! Thank you for asking Frog-chan',
    'Meows favourite DSMP ship is Dream x George',
    'Meow feels a deep connection to meow/doll and magic',
    'Meow for meows love for meows' , 
    'Doll because meow is a doll', 
    'And magic because Meow is a magical girl',
    'Reading Meows tiktok comments!!', 
    'Meow likes all genders',
    'Wow! Meowbah fanpage', 
    'Arigato little Meowling!', 
    'Woof',
    'kawaii giggle', 
    'bark bark', 
    'U  I  U', 'Meow is.. CATGENDER!!',
    'Meows favourite snack is kawaii poki and ramune!!','are you cringing yet?(UwU)','I AM DESINGED TO CREATE PAIN,SUFFERING,AND CRINGE'
]
#sj code:may be destructive
secrets=['https://www.youtube.com/watch?v=m6OCJxOsiyw&list=PLpd5iyNqlzHTyiabKDQMK_m--PfEzOZBx&index=20','https://www.youtube.com/watch?v=bIXm-Q-Xa4s&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=26','https://www.youtube.com/watch?v=UtPZcwPnvkw&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=37','https://www.youtube.com/watch?v=8F9jXYOH2c0','https://www.youtube.com/watch?v=oY2nVQNlUB8','https://www.youtube.com/watch?v=9E3nxoFjt4o','https://www.youtube.com/watch?v=W12vb_Crf00']
id = {
    '759221652231290881': 0,
    '822223581034971168': 1,
    '837077256450736129': 2,
    '786252335008972813': 3,
    '450125045054963714': 4,
    '766817083312046101': 5
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


def score(add, msg_id):
    r = open('data.txt', 'r')
    r = r.readlines()
    for i in range(len(r)):
        r[i] = r[i].replace("\n", "")

    r[id[str(msg_id)]] = str(int(r[id[str(msg_id)]]) + add)
    w = open('data.txt', 'w')
    for i in range(5):
        w.write(r[i] + "\n")
    w.write(r[i])
    w.close()

@client.event
async def on_message(message):
    global even_odds, high_low

    if message.author == client.user:
        return

    if message.content == "/view_rules":
        await message.channel.send("1. No botting or cheating to get coins.")
        await message.channel.send(
            "2. Don't curse, cyber-bully, or put any NSFW content.")
        await message.channel.send("3. Have fun (pain).")
    if message.content.startswith('/help'):
        await message.channel.send(
            "/why_tiktok (makes you cringe), spoon  (simple counting game), lets play (even or odds, higher or lwoer) & i say (even/odd, i say the number is ____), hey fork repellent"
        )
    if message.content.startswith('/why_tiktok'):
        await message.channel.send(forbidden_messages[random.randint(
            0,
            len(forbidden_messages) - 1)])
#SJ CODE BELOW:REMOVE IF FAULTY
    if message.content.startswith('/secret_47'):
        await message.channel.send(secrets[random.randint(
            0,
            len(secrets) - 1)])
    if ("fork" in message.content.lower()
        ) and not ("fork repellent" in message.content
                   or "forkrepellent" in message.content):
        await message.channel.send("NO TALK ABOUT FORK")
    
    if "fork repellent" in message.content or "forkrepellent" in message.content:
        await message.channel.send("https://tenor.com/view/no-gif-21880202")

    if message.content.lower() == "uprooting everything":
      await message.channel.send("i wonder what that reference is from")
      
    for i in range(len(rickroll)):
        if rickroll[i] in message.content:
            await message.channel.send(rickroll[i + 1])
            break

    if message.content == "spoon":
        if (message.author.id != int(os.getenv('USER_ID'))):
            os.environ['SCORE'] = str(int(os.getenv('SCORE')) + 1)
            os.environ['USER_ID'] = str(message.author.id)
            if (int(os.getenv('HIGHSCORE')) < int(os.getenv('SCORE'))):
                await message.channel.send("(New High Score!) Score: " +
                                           os.getenv('SCORE'))
            else:
                await message.channel.send("Score: " + os.getenv('SCORE'))
        else:
            if (int(os.getenv('HIGHSCORE')) < int(os.getenv('SCORE'))):
                os.environ['HIGHSCORE'] = str(int(os.getenv('SCORE')))
                await message.channel.send(
                    message.author.name +
                    " has broke the chain! New Highscore is: " +
                    os.getenv('HIGHSCORE'))
            else:
                await message.channel.send(
                    message.author.name +
                    " has broke the chain! Current score is: " +
                    os.getenv('SCORE') + ". High score is " +
                    os.getenv('HIGHSCORE'))
            os.environ['USER_ID'] = "0"
            os.environ['SCORE'] = "0"

    if message.content == "view coin amount":
        r = open("data.txt", "r")
        r = r.readlines()
        for i in range(5):
            r[i] = r[i].replace("\n", "")
        await message.channel.send(message.author.name + " has " +
                                   r[id[str(message.author.id)]] +
                                   " coins in their piggy bank.")

    if "lets play" in message.content:  # Input
        if "even or odds" in message.content:
            await message.channel.send(
                "I am thinking of a number. Is it even or odds?")
            even_odds = True
        if "higher or lower" in message.content and int(os.getenv('HIGH_LOW_ID')) == 0:
            await message.channel.send("I am thinking of  a number (1 - 100). Try to guess what it is (7 attempts remaining.)")
            high_low = True
            os.environ['HIGH_LOW_ID'] = str(message.author.id)
            os.environ['HIGH_LOW_NUM'] = str(random.randint(1, 100))

    if "i say" in message.content:  # Output
        lost_even_odds = "None"
        if ("even" in message.content
                or "odd" in message.content) and even_odds:
            a = random.randint(0, 1)
            if ("even" in message.content) and not ("odd" in message.content):
                if a == 0:
                    await message.channel.send("Correct!")
                    lost_even_odds = False
                else:
                    await message.channel.send("Incorrect!")
                    lost_even_odds = True
            elif ("odd"
                  in message.content) and not ("even" in message.content):
                if a == 0:
                    await message.channel.send("Incorrect!")
                    lost_even_odds = True
                else:
                    await message.channel.send("Correct!")
                    lost_even_odds = False

            if (lost_even_odds):
                if ("even" in message.content and "odd" in message.content):
                    await message.channel.send(
                        message.author.name +
                        " has tried to cheat! 20 coins is deducted as a penalty!"
                    )
                    score(-20, message.author.id)
                else:
                    await message.channel.send(message.author.name +
                                               " has lost 10 coins!")
                    score(-10, message.author.id)
            elif lost_even_odds != "None" and not lost_even_odds:
                await message.channel.send(message.author.name +
                                           " has gained 10 coins!")
                score(10, message.author.id)
        even_odds = False
        
        if "the number is" in message.content and int(os.getenv('HIGH_LOW_ID')) != 0 and message.author.id == int(os.getenv('HIGH_LOW_ID')) and high_low:
            num = message.content.split(" ")
            num = int(num[5])
            n = int(os.getenv('HIGH_LOW_NUM'))
            if int(os.getenv('HIGH_LOW_COUNT')) != 7:
                if n == num:
                    s = (8 -int(os.getenv('HIGH_LOW_COUNT'))) * 5
                    await message.channel.send(f"{message.author.name} has guessed the number correctly in {os.getenv('HIGH_LOW_COUNT')} attempts. {message.author.name} has earned {str(s)} coins.")
                    os.environ['HIGH_LOW_NUM'], os.environ['HIGH_LOW_COUNT'], os.environ['HIGH_LOW_ID'] = "0", "0", "0"
                    score(s, message.author.id)
                    high_low = False
                else:
                    os.environ['HIGH_LOW_COUNT'] = str(int(os.getenv('HIGH_LOW_COUNT'))+1)
                    if (num < n):
                        await message.channel.send("Higher :thumbsup:. (Attempt #" + os.getenv("HIGH_LOW_COUNT") + ")")
                    else:
                        await message.channel.send("Lower :thumbsdown:. (Attempt #" + os.getenv("HIGH_LOW_COUNT") + ")")
                    
            else:
                if n == num:
                    await message.channel.send("{} has guessed the number correctly in 7 attempts. {} has earned 5 coins.".format('message.author.name'))
                    score(5, message.author.id)
                else:
                    await message.channel.send(f"The number I was thinking of was {n}. You have lost 20 coins.")
                    score(-20, message.author.id)
                os.environ['HIGH_LOW_NUM'], os.environ['HIGH_LOW_COUNT'], os.environ['HIGH_LOW_ID'] = "0", "0", "0"
                high_low = False

client.run(os.getenv('TOKEN'))
