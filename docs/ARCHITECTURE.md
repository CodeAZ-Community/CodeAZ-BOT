# CodeAZ-BOT
Written by CodeAZ Community

### Notable features:
- XP system
- Limiting commands to one channel
- Welcome and farewell messages
- a role given to new users
- Reaction Roles
- Meme command via meme-api

### Configuration

We have tried to keep the bot as modular as possible, making sure most things can be disabled/enabled through the config file. Despite this, there are still a few imperfections. There are 2 files of configs, one being the active one on our discord sever, and the other being a blank. I believe the config files are relatively intuitive, so please inform us of any confusing parts.

### Overview of commands

`xp` - lists the top 10 users with the most xp points.

`xp [member]` - gives xp data about [member]

`xp-give [amount] [member]` - sends [amount] many xp points to member [member] and subtracts that amount from the commands user.

`xp-send [amount] [member]` - sends [amount] many xp points to member [member] WITHOUT subtracting that amount from the commands user.

`xp-bet [amount]` - bets [amount] many xp points with a 90/10 chance of losing and winning that much points

`xp-daily` - gives xp to the user, giving them a random amount from the minimum-maximum range. currently this is 10 and 50 in the server (as of 12/28/2025).

`meme` - send a random meme from meme-api.com to the user.
