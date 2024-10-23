letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = dict(zip(letters, points))
letters_to_points.update({" ": 0})

brownie_points = "BROWNIE"

# def get_word():
#     text = input("Please enter a word: ").upper()
#     return text

def score_word(word):
    '''This function calculates the score of each letter for every

     word played'''
    point_total = 0
    for i in word:
        point = letters_to_points.get(i, 0)
        point_total += point
    return point_total

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con":
    ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, word in player_to_words.items():
    player_points = 0
    for n in word:
        player_points += score_word(n)
    player_to_points.update({player: player_points})

print(player_to_points)







