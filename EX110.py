
Solução em 2021 (tenho feito em inglês para treinar a língua também):

#Module of currency.

def summary(number, perc_increase, perc_decrease):
    double = number * 2
    half = number / 2
    increased = number + (number * perc_increase / 100)
    decreased = number - (number * perc_decrease / 100)
    print("-" * 40)
    print("SUMMARY".center(40))
    print("-" * 40)
    print(f"Price analysed: \tR${number:<10.2f}")
    print(f"Double of the price \tR${double:<10.2f}")
    print(f"Half of the price: \tR${half:<10.2f}")
    print(f"{perc_increase}% of increase: \tR${increased:<10.2f}")
    print(f"{perc_decrease}% of decrease: \tR${decreased:<10.2f}")
    print("-" * 40)