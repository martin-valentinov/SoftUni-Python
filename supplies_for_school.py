number_of_pens = int(input())
number_of_markers = int(input())
litres_detergent = int(input())
discount = int(input())

pen = 5.80
marker = 7.20
detergent_per_litre = 1.20


price = number_of_pens * pen + number_of_markers * marker + \
        litres_detergent * detergent_per_litre

discount = price * discount / 100

price = price - discount

print (price)

