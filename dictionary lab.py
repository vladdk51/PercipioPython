letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 2, 2, 2, 1, 3, 3, 3, 1, 4, 3, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 3, 3, 4, 3, 5]
zipped_letters_points = zip(letters,points)
letter_to_points = {letters:points for letters, points in zipped_letters_points}
#print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point_total+=letter_to_points.get(letter,0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"BLUE":["EARTH","ERASER","ZAP"],"TENNIS":["EYES","BELLY","COMA"],"EXIT":["MACHINE",
"HUSKY","PERIOD"]}
player_to_points = {}

for player,words in player_to_words.items():
  player_points=0
  for word in words:
    player_points+=score_word(word)
  player_to_points[player]=player_points

print(player_to_points)