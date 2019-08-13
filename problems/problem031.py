'''
Catherine Turner
8/12/19
https://projecteuler.net/ Problem 31
'''

# Provided a target (in pence), find the number of coin combinations that sum to that target
def coinCombo(target):
    count = 0
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    # a = # of 200p coins
    for a in range(int(target/coins[0]) + 1):
        # b = # of 100p coins
        for b in range(int((target-a*coins[0])/coins[1]) + 1):
            # c = # of 50p coins
            for c in range(int((target-a*coins[0]-b*coins[1])/coins[2]) + 1):
                # d = # of 20p coins
                for d in range(int((target-a*coins[0]-b*coins[1]-c*coins[2])/coins[3]) + 1):
                    # e = # of 10p coins
                    for e in range(int((target-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3])/coins[4]) + 1):
                        # f = # of 5p coins
                        for f in range(int((target-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3]-e*coins[4])/coins[5])+ 1):
                            # g = # of 2p coins
                            for g in range(int((target-a*coins[0]-b*coins[1]-c*coins[2]-d*coins[3]-e*coins[4]-
                                                f*coins[5])/coins[6]) + 1):
                                # However many 1p coins must be added to reach the target is unimportant
                                count += 1

    return count

print(coinCombo(200))
