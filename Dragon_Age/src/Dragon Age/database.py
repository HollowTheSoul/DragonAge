##  @brief The database of Dragon_Age
#   @return dragon from the database
#   This database constains all the dragons for building towers and also
#   the enemy dragons with different attributes
def setDragonData():
    dragon = dict()
    #dragon = (name, element, baseAttack, hp, upgrade, range, attack speed, cost)
    dragon[1] = ("FireDragon", "fire", 10, 20, 1, 50, 5, 180)
    dragon[2] = ("FireDragon2", "fire", 12, 20, 2, 100, 4, 400)
    dragon[3] = ("FireDragon3", "fire", 17, 20, 3, 150, 3, "MAX")

    dragon[4] = ("IceDragon", "ice", 3, 20, 1, 100, 10)
    dragon[5] = ("IceDragon2", "ice", 5, 20, 2, 150, 9, 400)
    dragon[6] = ("IceDragon3", "ice", 10, 20, 3, 1750, 7, "MAX")

    dragon[7] = ("PoisonDragon", "poison", 5, 20, 1, 75, 8)
    dragon[8] = ("PoisonDragon2", "poison", 7, 20, 2, 125, 6, 400)
    dragon[9] = ("PoisonDragon3", "poison", 12, 20, 3, 150, 5, "MAX")

    dragon[10] = ("EnemyDragon", "normal", 1, 20, 1, 0, 0)
    dragon[11] = ("EnemyDragon2", "normal", 1, 25, 1, 0, 0)
    dragon[12] = ("EnemyDragon3", "normal", 1, 20, 1, 0, 0)
    dragon[13] = ("EnemyDragon4", "normal", 1, 25, 1, 0, 0)
    dragon[14] = ("FlyingDragon", "normal", 1, 30, 1, 0, 0)
    return dragon
