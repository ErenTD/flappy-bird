# Appearance settings
#
# Read the README.md file for detailed instructions
PIPE_COLOR = 'GREEN'
BIRD_COLOR = 'YELLOW'
TIME = 'DAY'

# Bird physics
#
# Don't touch if you don't know what you're doing!
# You can cause the game to be very difficult
# ultimately making it unplayable.
BIRD_JUMP_STRENGTH = 4
GRAVITY = 0.125
BIRD_ROTATION_MULTIPLIER = 3

# Pipe rules
#
# Can be changed to make the game easier/harder without messing
# with the physics.
#
# Please be careful with the syntax.
PIPE_SPAWN_INTERVAL = 1200
PIPE_SPAWN_LOCATIONS = [x for x in range(200,401)]
PIPE_SPEED = 2