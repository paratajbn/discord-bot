import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

IMAGE_FOLDER = 'path/to'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Playing a Game"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.reply('Hello!')

    if message.content.startswith('$meme'):
        image_files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
        if image_files:
            random_image = random.choice(image_files)
            image_path = os.path.join(IMAGE_FOLDER, random_image)
            try:
                with open(image_path, 'rb') as f:
                    picture = discord.File(f)
                    await message.reply(file=picture)
            except FileNotFoundError:
                await message.reply("Sorry, the image file was not found.")
        else:
            await message.reply("No images found in the specified folder.")

client.run('PUT_YOUR_TOKEN_HERE')
