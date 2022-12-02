# the score per action (and a unique ID)
rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6


def day_2_1_scoring(opponent_move: str, my_move: str) -> int:
    move_dict = {"A": rock,
                 "B": paper,
                 "C": scissors,
                 "X": rock,
                 "Y": paper,
                 "Z": scissors
                 }

    action_action_to_result_dict = {(rock, rock): draw,
                                    (rock, paper): win,
                                    (rock, scissors): lose,
                                    (paper, rock): lose,
                                    (paper, paper): draw,
                                    (paper, scissors): win,
                                    (scissors, rock): win,
                                    (scissors, paper): lose,
                                    (scissors, scissors): draw}
    opponent_move = move_dict[opponent_move]
    my_move = move_dict[my_move]
    return my_move + action_action_to_result_dict[(opponent_move, my_move)]


def day_2_2_scoring(opponent_move: str, my_goal: str) -> int:
    move_dict = {"A": rock,
                 "B": paper,
                 "C": scissors,
                 }
    goal_dict = {"X": lose,
                 "Y": draw,
                 "Z": win}
    action_goal_to_action_dict = {(rock, lose): scissors,
                                  (rock, win): paper,
                                  (rock, draw): rock,
                                  (paper, lose): rock,
                                  (paper, win): scissors,
                                  (paper, draw): paper,
                                  (scissors, lose): paper,
                                  (scissors, win): rock,
                                  (scissors, draw): scissors}
    opponent_move = move_dict[opponent_move]
    my_goal = goal_dict[my_goal]
    return my_goal + action_goal_to_action_dict[(opponent_move, my_goal)]
