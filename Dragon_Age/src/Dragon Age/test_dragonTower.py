from dragonTower import DragonTower
import gameData

fireDragon =DragonTower(1,gameData.dragonDatabase)
fireDragon.x = 400
fireDragon.y = 400
fireDragon.range = 50
fireDragon.upgrade = 1


##  @brief Test isInRangeEquation is working
#   Tested edge cases
def test_isInRangeEquation():
    assert fireDragon.isInRangeEquation(500,500) == False
    assert fireDragon.isInRangeEquation(450,450) == False
    assert fireDragon.isInRangeEquation(410,410) == True


##  @brief Test isInRange is working
#   Tested edge cases
def test_isInRange():
    assert fireDragon.isInRange((500,500,500,500)) == False
    assert fireDragon.isInRange((450,450,450,450)) == False
    assert fireDragon.isInRange((410,410,410,410)) == True


##  @brief Test canUpgrade is working
#   Tested edge cases
def test_canUpgrade():
    gameData.playerCoins = 300
    assert fireDragon.canUpgrade() == True

    gameData.playerCoins = 200
    assert fireDragon.canUpgrade() == False

    gameData.playerCoins = 250
    assert fireDragon.canUpgrade() == True
    
    