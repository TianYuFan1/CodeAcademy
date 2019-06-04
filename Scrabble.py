letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words = {"player1": ["blue", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


def score_word(word):
    point_total = 0
    for char in word:
        point_total += letter_to_points.get(char, 0)
    return point_total


def play_word(player, word):
    player_to_words[player] = player_to_words.get(player) + [word]


def update_point_totals():
    player_to_points = {}
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
    return player_to_points


def convert_upper():
    for player, words in player_to_words.items():
        new_words = []
        for word in words:
            word_upper = word.upper()
            new_words.append(word_upper)
        player_to_words[player] = new_words


def letter_to_points():
    return {letter: point for letter, point in zip(letters, points)}


# TESTING LETTER_TO_POINTS
letter_to_points = letter_to_points()
print("Mapping each letter to point: {LOG}".format(LOG=letter_to_points))
# TESTING CONVERT_UPPER
convert_upper()
print("Words converted to all uppercase: {LOG}".format(LOG=player_to_words))
# TESTING PLAY_WORD FUNCTION
play_word("player1", "TEST")
print("Words for each player: {LOG}".format(LOG=player_to_words))

# TESTING UPDATE_POINT_TOTALS
print("Total score for each player: {LOG}".format(LOG=update_point_totals()))
