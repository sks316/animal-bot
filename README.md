# Animals!

[![love-badge][]][love] [![nextcord-badge][]][nextcord]

[![invite-badge][]][invite]

This is a simple, FOSS bot to post cute pics of animals on request. On top of being a simple project to pass the time and make people smile, this is also my first bot to use Slash Commands for all of its user-facing functions.

# How to run the bot
As with the rest of my bots, you simply clone the repo, set up Python, install dependencies, set up the config file, and run. First, clone the repo.

Then, install dependencies:
```
pip install -r requirements.txt
```
Now, let's set up the config file.
Go to the directory containing `animal.py` then make a new file called `animal_config.py`. This will be our config file.
Next, go to the [Discord Developer Portal](https://discordapp.com/developers/applications/) and create an application. Once done, go to `Bot` and hit the `Add Bot` button. Once done, you'll get your token. You probably know this already, but **DO NOT SHARE THIS TOKEN WITH ANYONE, IT WILL GIVE FULL ACCESS TO YOUR BOT.**

You'll also want to enable both the Presence Intent and Server Members Intent.

Now open `animal_config.py` in your favorite text editor and paste the following:
```
token = 'YOUR-TOKEN-HERE'
owner = YOUR-USER-ID-HERE
```
Replace `YOUR-TOKEN-HERE` with your bot's token and `YOUR-USER-ID-HERE` with ***your*** User ID, not your bot's.
Finally, we run the bot:
```
py animal.py
```
Or, if you're using Linux:
```
python3 animal.py
```

# APIs Used:
random.cat

dog.ceo

bunnies.io

random-d.uk

nekos.life

shibe.online

some-random-api.ml

[invite]: https://discord.com/api/oauth2/authorize?client_id=954166535818215454&permissions=137439340608&scope=bot%20applications.commands
[invite-badge]: https://img.shields.io/badge/invite%20me!-click%20here-black.svg?style=for-the-badge&colorB=7289DA

[love]: https://lillie2523.carrd.co
[love-badge]: https://custom-icon-badges.herokuapp.com/badge/-Made%20with%20love...-555555?style=for-the-badge&logo=heart

[nextcord]: https://github.com/nextcord/nextcord
[nextcord-badge]: https://custom-icon-badges.herokuapp.com/badge/-...and%20Nextcord-555555?style=for-the-badge&logo=nextcord
