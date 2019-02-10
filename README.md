# ConnerBot
Conner Bot for Discord. Python version.
**This project requires Linux, preferrably Ubuntu. If you are not running Linux, STOP! Conner Bot WILL NOT run.**
*Note: the main bot and the quote module can be run on Windows using the Ubuntu subsystem. The Leaderboard module must be hosted on a 64-bit Ubuntu server (not including Ubuntu subsystem).*

## Setup:

### Part 1- Installing Python and tools
**user@example:/$  is just to show the terminal, copy/paste the stuff after that**
```
user@example:/$ sudo add-apt-repository ppa:jonathonf/python-3.6
user@example:/$ sudo apt-get update
user@example:/$ sudo apt-get install python3.6
user@example:/$ wget https://bootstrap.pypa.io/get-pip.py
user@example:/$ sudo python3.6 get-pip.py
user@example:/$ sudo pip3.6 install virtualenv
user@example:/$ virtualenv -p python3.6 venv
user@example:/$ source venv/bin/activate
user@example:/$ pip install discord uvloop
```

Note that you will need to run source venv/bin/activate every time you want to run Conner Bot if venv isn't already loaded
You could also use python3.6 but why would you do that?

### Part 2- Clone the repository
```
user@example:/$ git clone https://github.com/THEWHITEBOY503/ConnerBot.git
user@example:/$ cd ConnerBot
```

### Part 3- Setting up Conner Bot
**make sure you are in the ConnerBot directory**
```
user@example:/$ nano main.py
```
at the bottom of the file, you will find a token section. Put your bots token there. Save and exit

### Part 4- Getting the weather module updater
**make sure you are in the ConnerBot directory**
```
user@example:/$ nano weatherupdate
```
once in, type this
```
cd ~
cd ConnerBot
watch -n 1800 wget wttr.in/plano.png -O weather.png
```
Note: where plano.png is replace plano with your city name. Save and exit.
```
user@example:/$ chmod 755 weatherupdate
```

### (Optional) Part 5- Fun Fact quote module
```
user@example:/quotemod/$ cd quotemod
user@example:/quotemod/$ sudo apt-get install node.js
user@example:/quotemod/$ sudo apt-get install npm
user@example:/quotemod/$ npm install discord.js
user@example:/quotemod/$ npm install infinite-loop
user@example:/quotemod/$ nano config.json
```
edit accordingly


### Part 6- Running Conner Bot
In one window:
```
user@example:/$ python main.py
```
If all goes according to plan, you should see "Starting Conner Bot" on your terminal.
In another window:
```
user@example:/$ ./weatherupdate
```
this is for the weather updater

If you are going to run the quote/fun fact module, run this in another window:
```
user@example:/$ cd quotemod
user@example:/quotemod/$ node quote.js
```
This is for the fun fact module

[Great! You've gotten your very own ConnerBot clone up and running! Cool! BUT WAIT, THERES MORE! You need to set up leveling. Click here for a guide on how to do so](https://github.com/THEWHITEBOY503/ConnerBot/blob/master/Levels/README.md)
