class Game(object):
    def __init__(self, game_pairs=0):
        self.throws = []
        self.game_pairs = game_pairs

    def __call__(self, game_pairs=0):
        self.game_pairs = game_pairs

    def add_throw(self, throw):
        self.throws.append(throw)

    def check_value_range(self, value):
        if value < 0 or value > 10:
            print('Exception Scenario')
            raise Exception('Values not in range')
                
    def get_total(self):
        # initializing total score , throw index to 0
        total_score = 0
        throw_ind = 0
        for pair in range(self.game_pairs):
            #print('ind ', throw_ind, ' val ', self.throws[throw_ind], ' game pair ', self.game_pairs)
            self.check_value_range(self.throws[throw_ind])
            # Checking for strike
            if self.throws[throw_ind] == 10:
                # if it is last but one
                if pair == self.game_pairs - 2:
                    self.check_value_range(self.throws[throw_ind] + 1)
                    if self.throws[throw_ind+1] == 10:
                        total_score += 30
                    else:
                        self.check_value_range(self.throws[throw_ind + 2])
                        total_score += 10 + self.throws[throw_ind+1] + self.throws[throw_ind + 2]
                # checking for last one
                elif pair == self.game_pairs - 1:
                    total_score += 30
                else:
                    self.check_value_range(self.throws[throw_ind + 1])
                    self.check_value_range(self.throws[throw_ind + 2])
                    total_score += 10 + self.throws[throw_ind+1] + self.throws[throw_ind + 2]
                throw_ind += 1
            # checking for sparse
            else:
                self.check_value_range(self.throws[throw_ind + 1])
                if self.throws[throw_ind] + self.throws[throw_ind + 1] == 10:
                    # if it is last one
                    #print('--- pair', pair)
                    if pair == self.game_pairs -1:
                        total_score += 10 + self.throws[throw_ind]
                    else:
                        self.check_value_range(self.throws[throw_ind + 2])
                        total_score += 10 + self.throws[throw_ind + 2]    
                    throw_ind += 2
                else:
                    total_score += self.throws[throw_ind] + self.throws[throw_ind + 1]
                    throw_ind += 2

            print('Pair ', pair,'Score till now', total_score)
        return total_score

def __main__():
    pass