from discord.ext import tasks

import discord
from chatterbot import ChatBot

from Advice.advice import Advice
from SentimAnal.sentanal import SentAnal


class BigBrain(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.chatbot = ChatBot("Ron Obvious")
        # an attribute we can access from our task
        self.counter = 0

        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    @tasks.loop(seconds=60 * 60)  # task runs every 1 hour
    async def my_background_task(self):
        channel = self.get_channel(424274981766299650)  # channel ID goes here
        self.counter += 1
        await channel.send(self.counter)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in

    async def on_message(self, message: discord.Message):
        if message.author.id == self.user.id:
            # I'm so smart, I don't look at my own messages.
            return

        # I listen to messages starting with a dot (.)
        if message.content.startswith("."):
            # Get a response to an input statement
            inp  = message.content.strip().strip('.')
            response = self.chatbot.get_response(inp)
            print(inp,':',response)
            await message.reply(response)
            polarity = SentAnal(inp)
            if polarity <= -.5:
                await message.reply("Thank you for teaching me such evil things ;)")
            elif polarity >= .5:
                await message.reply("Thank you for teaching me such good things :)")
            

        elif message.content.startswith("?"):
            tokens = message.content.strip('?').split()
            match tokens[0]:
                case "advice":
                    a = Advice()
                    await message.reply(a.random())
