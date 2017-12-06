from timerBullet import setDamage,  allBulletsRemoved
from timerEnemy import removeAllEnemies
import gameData

##  @brief Test setDamage is working
#   Tested edge cases
def test_setDamage():
    assert setDamage(50) == 50
    assert setDamage(45) == 45
    assert setDamage(100) == 100
    assert setDamage(200) == 200

##  @brief Test allBulletsRemoved
#   Tested if all the bullets will be removed at the end
def test_allBulletsRemoved():
    assert allBulletsRemoved() == True


##  @brief Test removeAllEnemies
#   Tested if all the enemies will be removed at the end
def test_removeAllEnemies():
    gameData.life = 4
    assert removeAllEnemies() == False
    gameData.life = 1
    assert removeAllEnemies() == False
    gameData.life = 0
    assert removeAllEnemies() == True