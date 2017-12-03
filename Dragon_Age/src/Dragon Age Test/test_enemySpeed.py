def speedAtWave(x):
    speed = 4 # speed of enemy
    wave = x # wave that is testing

    for i in range(wave-1): # rule of speed increment
        if wave % 2 == 0:
            speed += 1

    return speed

def test_speed_at_wave4():
    assert speedAtWave(4) == 7
