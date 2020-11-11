import config

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

# Set bird color
u = yellowbird_upflap
m = yellowbird_midflap
d = yellowbird_downflap
if config.BIRD_COLOR == 'YELLOW':
	u = yellowbird_upflap
	m = yellowbird_midflap
	d = yellowbird_downflap
if config.BIRD_COLOR == 'RED':
	u = redbird_upflap
	m = redbird_midflap
	d = redbird_downflap
if config.BIRD_COLOR == 'BLUE':
	u = bluebird_upflap
	m = bluebird_midflap
	d = bluebird_downflap

# Set pipe color
pipe = green_pipe
if config.PIPE_COLOR == 'GREEN':
	pipe = green_pipe
if config.PIPE_COLOR == 'RED':
	pipe = red_pipe

# Set background time
bg = day
if config.TIME == 'DAY':
	bg = day
if config.TIME == 'NIGHT':
	bg = night