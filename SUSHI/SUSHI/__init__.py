# SUSHI
# Jaekyoung Kim (rlakim5521@naver.com)

# Sorts the array of price, preference, costEffectiveness
# according to costEffectiveness by an insertion sort algorithm.
def sortByCostEffectiveness(n, price, preference, costEffectiveness):
    for iter1 in xrange(0, n-1):
        for iter2 in xrange(iter1, n):
            if(costEffectiveness[iter1] < costEffectiveness[iter2]):
                tmp_price = price[iter2]
                tmp_preference = preference[iter2]
                tmp_costEffectiveness = costEffectiveness[iter2]
                price[iter2] = price[iter1]
                preference[iter2] = preference[iter1]
                costEffectiveness[iter2] = costEffectiveness[iter1]
                price[iter1] = tmp_price
                preference[iter1] = tmp_preference
                costEffectiveness[iter1] = tmp_costEffectiveness

# Returns a maximum preference by recursive functions.
# For time efficiency, calculates only more than median costEffectiveness value.
# When meets base case(start == n), calculates all possible values.
def getMaximumPreference(start, n, m, price, preference, costEffectiveness):
    
    if(start == n):
        ret = 0
        for iter in xrange(0, n):
            ret = max(ret, preference[iter] * (m/price[iter]))
        return ret
    
    ret = 0
    for iter in xrange(start, n/2+1):
        ret = max(ret, preference[iter] * (m/price[iter])\
            + getMaximumPreference(iter+1, n, (m%price[iter]), price, preference, costEffectiveness))
    return ret

# Main function
if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        # Input
        n, m = map(int, raw_input().split())
        m = m / 100
        price = [0] * n
        preference = [0] * n
        costEffectiveness = [0.0] * n
        for _ in xrange(n):
            price[_], preference[_] = map(int, raw_input().split())
            price[_] = price[_] / 100
            costEffectiveness[_] = float(preference[_]) / float(price[_])
            
        sortByCostEffectiveness(n, price, preference, costEffectiveness)
        
        print getMaximumPreference(0, n, m, price, preference, costEffectiveness)