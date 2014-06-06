#!/usr/bin/env python3

adjacent_digits = 13
pattern = "73167176531330624919225119674426574742355349194934"
pattern = pattern + "96983520312774506326239578318016984801869478851843"
pattern = pattern + "85861560789112949495459501737958331952853208805511"
pattern = pattern + "12540698747158523863050715693290963295227443043557"
pattern = pattern + "66896648950445244523161731856403098711121722383113"
pattern = pattern + "62229893423380308135336276614282806444486645238749"
pattern = pattern + "30358907296290491560440772390713810515859307960866"
pattern = pattern + "70172427121883998797908792274921901699720888093776"
pattern = pattern + "65727333001053367881220235421809751254540594752243"
pattern = pattern + "52584907711670556013604839586446706324415722155397"
pattern = pattern + "53697817977846174064955149290862569321978468622482"
pattern = pattern + "83972241375657056057490261407972968652414535100474"
pattern = pattern + "82166370484403199890008895243450658541227588666881"
pattern = pattern + "16427171479924442928230863465674813919123162824586"
pattern = pattern + "17866458359124566529476545682848912883142607690042"
pattern = pattern + "24219022671055626321111109370544217506941658960408"
pattern = pattern + "07198403850962455444362981230987879927244284909188"
pattern = pattern + "84580156166097919133875499200524063689912560717606"
pattern = pattern + "05886116467109405077541002256983155200055935729725"
pattern = pattern + "71636269561882670428252483600823257530420752963450"

def product_from_position(position, places):
    product = 1
    for i in range(position, position+places):
        product *= int(pattern[i])
    return product

def main():
    products = []
    for i in range(0, len(pattern)-adjacent_digits-1):
        products.append(product_from_position(i, adjacent_digits));
    print(max(products))


if __name__ == '__main__':
    main()