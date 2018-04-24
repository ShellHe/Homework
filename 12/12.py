import random

rng = random.Random()

dice_throw = rng.randrange(1,7)
delay_in_seconds = rng.randoms() * 5.0

print(dice_throw,delay_in_seconds)