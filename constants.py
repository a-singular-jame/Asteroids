SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3
PLAYER_LIVES = 3
INVULN_TIME = 3 # seconds
SCORE_MULTIPLIER = 5

# ---------- RANKS ---------- #
def SCORE_TO_RANK(score):
    if score >= 5000:
        return "S"
    elif score >= 2500:
        return "A+"
    elif score >= 1000:
        return "A"
    elif score >= 500:
        return "B"
    elif score >= 250:
        return "C"
    elif score >= 100:
        return "D"
    elif score >= 0:
        return "F"
    