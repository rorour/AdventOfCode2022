from main import get_input_data, results


def _score_game_first(game):
    _SHAPE_SCORE = {'X': 1, 'Y': 2, 'Z': 3}
    _OUTCOME_SCORE = {
        ('A', 'X'): 3,
        ('A', 'Y'): 6,
        ('A', 'Z'): 0,
        ('B', 'X'): 0,
        ('B', 'Y'): 3,
        ('B', 'Z'): 6,
        ('C', 'X'): 6,
        ('C', 'Y'): 0,
        ('C', 'Z'): 3,
        }

    return _SHAPE_SCORE[game[-1]] + _OUTCOME_SCORE[(game[0], game[-1])]


def _score_game_second(game):
    _SHAPE_SCORE = {
        ('A', 'X'): 3,
        ('A', 'Y'): 1,
        ('A', 'Z'): 2,
        ('B', 'X'): 1,
        ('B', 'Y'): 2,
        ('B', 'Z'): 3,
        ('C', 'X'): 2,
        ('C', 'Y'): 3,
        ('C', 'Z'): 1,
    }
    _OUTCOME_SCORE = {'X': 0, 'Y': 3, 'Z': 6}
    return _SHAPE_SCORE[(game[0], game[-1])] + _OUTCOME_SCORE[game[-1]]


def first():
    return sum([_score_game_first(g) for g in data])


def second():
    return sum([_score_game_second(g) for g in data])


data = get_input_data()
results(first, second)
