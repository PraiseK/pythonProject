# places = []
# place = input("Place: ").title()
#
# while place != "":
#     places.append(place)
#     place = input("Place: ").title()
# if len(places) > 0:
#     print("On my holiday I went to: ")
#     longest_place = ""
#     for place in places:
#         print(place)
#         if len(place) > len(longest_place):
#             longest_place = place
#     print(f"The place with the longest name was {longest_place}")
# else:
#     print("I went nowhere :(")
#
#     for place in places:
#         print(place)

def main():
    balance = get_balance()
    print(f"Your bank balance is ${balance}")


def get_balance():
    balance = float(input("Bank Balance: $"))
    return balance
