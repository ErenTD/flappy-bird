import config

# Register assets
yellowbird_downflap = 'assets/sprites/yellowbird-downflap.png'
yellowbird_midflap = 'assets/sprites/yellowbird-midflap.png'
yellowbird_upflap = 'assets/sprites/yellowbird-upflap.png'
redbird_downflap = 'assets/sprites/redbird-downflap.png'
redbird_midflap = 'assets/sprites/redbird-midflap.png'
redbird_upflap = 'assets/sprites/redbird-upflap.png'
bluebird_downflap = 'assets/sprites/bluebird-downflap.png'
bluebird_midflap = 'assets/sprites/bluebird-midflap.png'
bluebird_upflap = 'assets/sprites/bluebird-upflap.png'

red_pipe = 'assets/sprites/pipe-red.png'
green_pipe = 'assets/sprites/pipe-green.png'

day = 'assets/sprites/background-day.png'
night = 'assets/sprites/background-night.png'

message = 'assets/sprites/message.png'
base = 'assets/sprites/base.png'
gameover = 'assets/sprites/gameover.png'
newbest = 'assets/sprites/new.png'

favicon = 'assets/favicon.ico'

medals = {	'none': 'assets/sprites/medalscreen-none.png',
			'bronze': 'assets/sprites/medalscreen-bronze.png',
			'silver': 'assets/sprites/medalscreen-silver.png',
			'gold': 'assets/sprites/medalscreen-gold.png',
			'plat': 'assets/sprites/medalscreen-plat.png'}

font = 'assets/04B_19.ttf'

sounds = {	'hit': 'assets/audio/hit.wav',
			'die': 'assets/audio/die.wav',
			'point': 'assets/audio/point.wav',
			'swoosh': 'assets/audio/swoosh.wav',
			'wing': 'assets/audio/wing.wav'}

# Set bird color
upflap = yellowbird_upflap
midflap = yellowbird_midflap
downflap = yellowbird_downflap
if config.BIRD_COLOR == 'YELLOW':
	upflap = yellowbird_upflap
	midflap = yellowbird_midflap
	downflap = yellowbird_downflap
if config.BIRD_COLOR == 'RED':
	upflap = redbird_upflap
	midflap = redbird_midflap
	downflap = redbird_downflap
if config.BIRD_COLOR == 'BLUE':
	upflap = bluebird_upflap
	midflap = bluebird_midflap
	downflap = bluebird_downflap

# Set pipe color
pipe = green_pipe
if config.PIPE_COLOR == 'GREEN':
	pipe = green_pipe
if config.PIPE_COLOR == 'RED':
	pipe = red_pipe

# Set background time
background = day
if config.TIME == 'DAY':
	background = day
if config.TIME == 'NIGHT':
	background = night