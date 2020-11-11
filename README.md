# flappy-bird
###### A pygame rewrite of the once popular game, flappy bird.

## Installing
#### The easier way (manual updates)
* Click "Download as ZIP"
* If you don't have python installed, install python from python.org
	* The version which is confirmed working is python 3.7
	* Please don't forget to add python to PATH
* On a terminal window which is run as administrator, type the following: _pip install pygame==1.9.6_
* You can now start the game by clicking run.bat on windows, or by typing _python flappy.py_ on a terminal window.

#### The easy way (auto updates)
* If you don't have git installed, install it.
* CD into the directory which you want to install the game to.
* Run the following command: _git clone https://github.com/ErenTD/flappy-bird.git_
* If you don't have python installed, install python from python.org
	* The version which is confirmed working is python 3.7
	* Please don't forget to add python to PATH
* On a terminal window which is run as administrator, type the following: _pip install pygame==1.9.6_
* You can now start the game by clicking run.bat on windows, or by typing _python flappy.py_ on a terminal window.

## Configuration
* In the config.py file, you can change the game configurations.
	* Bird color is changed by changing the BIRD_COLOR. Available options: 'YELLOW', 'RED', 'BLUE'. Defaults to yellow.
	* Pipe color is changed by changing the PIPE_COLOR. Available options: 'GREEN', 'RED'. Defaults to green.
	* Background time is changed by changing TIME. Available options: 'DAY', 'NIGHT'. Defaults to day.
	* The other variables in the config are about difficulty and physics. Their name is pretty self-explanatory. It is recommended you don't touch them.

## Updating
* If you installed the manual updates way, you need to delete the game folder and go through the installation process again.
* If you installed the auto updates way, cd into the game folder via a terminal window and type: _git pull_