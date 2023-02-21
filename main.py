import glob
import os

#https://stackoverflow.com/questions/42407976/how-to-load-multiple-text-files-from-a-folder-into-a-python-list-variable
file_list = glob.glob(os.path.join(os.getcwd(), "/Users/student/Desktop/Ghost", "*.txt"))
corpus = []
for file_path in file_list:
    with open(file_path) as f_input:
        corpus.append(f_input.readlines())

word_list = []
for txt_file in corpus:
    for word in txt_file:
        word_list.append([word[:-1], 0])

class Dictionary:
    def __init__(self):
        self.word_dict = dict(word_list)

    def set_value(self, check_word):
        self.word_dict[check_word] = 1

    def is_used(self, check_word):
        check_word_value = self.word_dict.get(check_word)
        if check_word_value == -1:
            return True
        else:
            return False

    def print_dictionary(self):
        print(self.word_dict)

    def get_neighbors(self, check_string):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        neighbors = []

        check_string_length = len(check_string)

        # https://www.geeksforgeeks.org/python-find-the-list-elements-starting-with-specific-letter/
        for element in self.word_dict:
            if check_string_length < len(element):
                element_start = element[check_string_length]
                if element.startswith(check_string) and element_start not in neighbors and element_start in alphabet:
                    neighbors.append(element[check_string_length])
                else:
                    continue
        return sorted(neighbors)


class GhostGame:
    cutoff_depth = 2
    human = 1
    computer = -1
    max = 1
    min = -1

    def __init__(self):
        self.dictionary = Dictionary()
        self.game_over = False
        self.play_word = ""
        self.depth = 0
        self.whose_turn = 1
        self.last_move = -1
        self.new_move = []

    def minmax(self, play_word, depth, whose_turn, last_move):

        if len(self.play_word) >= 4 and word in self.dictionary():
            self.new_move = [last_move, self.whose_turn * 100]
            return self.new_move
        elif depth == 0:
            num_neighbors = len(self.dictionary.get_neighbors(self.play_word))
            self.new_move = [last_move, self.whose_turn * num_neighbors]
            return self.new_move

        best_score = whose_turn * 1000 * -1
        best_move = ""
        neighbors = self.dictionary.get_neighbors(self.play_word)
        for neighbor in neighbors:
            word_copy = str(play_word)
            word_copy += neighbor

            best_neighbor = GhostGame.minmax(word_copy, -1, self.whose_turn * -1, neighbor, last_move)
            if (best_neighbor > best_score and self.whose_turn == GhostGame.max) or (best_neighbor < best_score and self.whose_turn == GhostGame.min):
                best_score = best_neighbor
                best_move = neighbor
                self.newMove = (best_move, best_score)

    def run(self):
        while not self.game_over:
            if self.whose_turn == GhostGame.human:
                self.last_move = input("Human player, enter letter: ")
                self.play_word += self.last_move
                print("Player made " + self.play_word)
            else:
                self.play_word += "e"
                print("Computer made " + self.play_word)

            if len(self.play_word) >= 4 and not self.dictionary.is_used(self.play_word):
                self.game_over = True
            else:
                self.whose_turn = self.whose_turn * -1

            self.minmax(self.play_word, self.cutoff_depth, self.whose_turn, self.last_move)

        print("Final word: " + self.play_word)
        if self.whose_turn == GhostGame.human:
            print("Sorry, you lose!")
        else:
            print("Congrats, you win!")

ghost = GhostGame()
ghost.run()
