def strategy_round_2(opponent_id: int, my_history: dict[int, list[int]], 
                     opponents_history: dict[int, list[int]]) -> tuple[int, int]:
    my_moves = my_history.get(opponent_id, [])
    opponent_moves = opponents_history.get(opponent_id, [])
    
    current_move = original_strategy(my_moves, opponent_moves, None)
    
    next_opponent = choose_next_opponent(opponent_id, my_history, opponents_history)
    
    return (current_move, next_opponent)

def original_strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    if not opponent_history:
        return 1
    
    opponent_cooperation_rate = sum(opponent_history) / len(opponent_history)
    
    recent_window = min(5, len(opponent_history))
    recent_opponent_behavior = opponent_history[-recent_window:]
    recent_cooperation_rate = sum(recent_opponent_behavior) / len(recent_opponent_behavior)
    
    tit_for_tat_likelihood = 0
    for i in range(1, len(my_history)):
        if opponent_history[i] == my_history[i-1]:
            tit_for_tat_likelihood += 1
    
    if len(my_history) > 1:
        tit_for_tat_likelihood /= (len(my_history) - 1)
    
    last_move_defect = opponent_history[-1] == 0
    
    betrayal_pattern = False
    if len(opponent_history) >= 3:
        for i in range(len(opponent_history) - 2):
            if opponent_history[i:i+3] == [1, 1, 0] and my_history[i:i+2] == [1, 1]:
                betrayal_pattern = True
    
    consecutive_defections = 0
    for move in reversed(opponent_history):
        if move == 0:
            consecutive_defections += 1
        else:
            break
    
    endgame = False
    if rounds is not None:
        remaining = rounds - len(my_history)
        if remaining <= 3:
            endgame = True
    
    if endgame:
        return 0
    
    if opponent_cooperation_rate > 0.8:
        if len(my_history) % 10 == 0:
            return 0
        return 1
    
    if tit_for_tat_likelihood > 0.8:
        return 1
    
    if recent_cooperation_rate > opponent_cooperation_rate and recent_cooperation_rate > 0.6:
        return 1
    
    if last_move_defect:
        if consecutive_defections > 3:
            return 1
        return 0
    
    if betrayal_pattern:
        return 0
    
    if opponent_history[-1] == 1:
        return 1
    else:
        if len(my_history) % 5 == 0:
            return 1
        return 0

def choose_next_opponent(current_opponent: int, my_history: dict[int, list[int]], 
                        opponents_history: dict[int, list[int]]) -> int:
    opponent_stats = {}
    
    for opp_id in opponents_history.keys():
        if len(my_history.get(opp_id, [])) >= 200:
            continue
            
        opp_moves = opponents_history.get(opp_id, [])
        my_moves = my_history.get(opp_id, [])
        
        if not opp_moves:
            opponent_stats[opp_id] = {
                'cooperation_rate': 1.0,
                'rounds_played': 0
            }
            continue
            
        my_score = 0
        for i in range(len(my_moves)):
            if my_moves[i] == 1 and opp_moves[i] == 1:
                my_score += 3
            elif my_moves[i] == 0 and opp_moves[i] == 1:
                my_score += 5
            elif my_moves[i] == 0 and opp_moves[i] == 0:
                my_score += 1
        
        avg_score = my_score / len(my_moves)
        cooperation_rate = sum(opp_moves) / len(opp_moves)
        
        opponent_stats[opp_id] = {
            'avg_score': avg_score,
            'cooperation_rate': cooperation_rate,
            'rounds_played': len(my_moves)
        }
    
    if not opponent_stats:
        return current_opponent
    
    best_opponent = None
    best_value = -1
    
    for opp_id, stats in opponent_stats.items():
        if 'avg_score' in stats:
            value = stats['avg_score'] + (stats['cooperation_rate'] * 0.5)
        else:
            value = stats['cooperation_rate'] * 3
            
        if stats['rounds_played'] == 0:
            value += 0.3
            
        if value > best_value:
            best_value = value
            best_opponent = opp_id
    
    return best_opponent if best_opponent is not None else current_opponent