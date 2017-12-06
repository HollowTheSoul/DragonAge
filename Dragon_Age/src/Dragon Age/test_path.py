from path import inPlay, onBoard, upgradeBound, onRoute
import gameData

##  @brief Test inPlay is working
#   Tested edge cases
def test_inPlay():
    assert inPlay(46,396) == True
    assert inPlay(45,105) == False
    assert inPlay(0,600) == False


##  @brief Test onBoard is working
#   Tested edge cases
def test_onBoard():
    assert onBoard(400,500) == True
    assert onBoard(100,300) == True
    
##  @brief Test upgradeBound is working
#   Tested edge cases for the module
def test_upgradeBound():
    assert upgradeBound(700,340) == False
    assert upgradeBound(760,400) == False
    assert upgradeBound(710,350) == True

##  @brief Test onRoute is working
#   Tested edge cases for the module
def test_onRoute():
    assert onRoute((400,401,400,401)) == False
    assert onRoute((240,100,245,105)) == True
    assert onRoute((200,200,200,400)) == False

