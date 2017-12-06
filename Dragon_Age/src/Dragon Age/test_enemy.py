import gameData, random, enemy
from dragon import Dragon

tempSpeed = gameData.enemySpeed

def speedAtWave(x):
    gameData.enemySpeed = tempSpeed # set the original speed back every time
                                    # this function runs
    wave = x # wave that is testing
    for i in range(wave-1): # rule of speed increment
        if wave % 2 == 0:
            gameData.enemySpeed += 1
    return gameData.enemySpeed

def test_enemy_party_not_empty():
    enemy.setWave()
    assert gameData.waveEnemies != []

def test_speed_at_wave4():
    assert speedAtWave(4) == 6

def test_speed_increases_as_wave_increases():
    assert speedAtWave(4) > speedAtWave(1)
