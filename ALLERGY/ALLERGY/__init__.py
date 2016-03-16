# ALLERGY
# Jaekyoung Kim (rlakim5521@naver.com)

import copy

MAX_NUMBER = 20
TWO_POWER_TWENTY = 1048576

# Gets a minimum number of foods for everybody eating at least one food.
def getMinimumFoodNumber(table, servedFood, n, cache):
    # If we already checked this case, return MAX_VALUE.
    if cache[servedFood] != -1:
        return MAX_NUMBER
    
    # Checks everybody can eat all foods.
    length = len(table)
    allergyCheck = 0
    criterion = pow(2,n) - 1
    for foodNum in xrange(length):
        allergyCheck = allergyCheck | table[foodNum]
        if(allergyCheck == criterion):
            break
    # If someone can't eat all of foods, return a max number.
    if(allergyCheck != criterion):
        return MAX_NUMBER
    
    # The baseline is a current number of food.
    NeededFoodNum = [bin(servedFood).count("1")]
    # Try all possible case which delete one element(food) and append the result
    # to the NeededFoodNum list.
    for foodNum in xrange(length):
        assertTable = copy.deepcopy(table)
        del assertTable[foodNum]
        res = getMinimumFoodNumber(assertTable, servedFood, n, cache)
        if res != MAX_NUMBER:
            NeededFoodNum.append(res)
        
    return min(NeededFoodNum)

# Main function
if __name__ == "__main__":
    for _ in range(int(raw_input())):
        # Input
        n, m = map(int, raw_input().split())
        name = raw_input().split()
        table = [0] * m
        cache = [-1] * (TWO_POWER_TWENTY+1)
        # Fills the table with input values using bit operations.
        for iter in xrange(m):
            foodInfo = raw_input().split()
            foodInfo.append('\n')
            foodInfoNum = 1
            for friendNum in xrange(n):
                table[iter] = table[iter] << 1
                if(foodInfo[foodInfoNum] == name[friendNum]):
                    table[iter] = table[iter] | 1
                    foodInfoNum += 1
            
        # Filters the overlapped foods.
        sorted(table, reverse=True)
        for bigger in xrange(m):
            for smaller in xrange(bigger+1, m):
                if(table[bigger] | table[smaller] == table[bigger]):
                    table[smaller] = 0
        zeroNum = table.count(0)
        for iter in xrange(zeroNum):
            table.remove(0)
        
        # Makes a check list for served food. Default values are [1] * m.
        servedFood = TWO_POWER_TWENTY - 1
        servedFood >> zeroNum
        
        # Output
        print getMinimumFoodNumber(table, servedFood, n, cache)