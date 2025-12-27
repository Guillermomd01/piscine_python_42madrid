print("=== Game Analytics Dashboard ===\n")

data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements_count': 2
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements_count': 7
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements_count': 7
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements_count': 1
        }
    },
    'sessions': [
        {
            'player': 'bob',
            'duration_minutes': 94,
            'score': 1831,
            'mode': 'competitive',
            'completed': False,
            'achievements': 'speed_runner',
            'region': 'east'
        },
        {
            'player': 'charlie',
            'duration_minutes': 18,
            'score': 479,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'pixel_perfect',
            'region': 'central'
        },
        {
            'player': 'eve',
            'duration_minutes': 38,
            'score': 277,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'level_master',
            'region': 'south'
        },
        {
            'player': 'alice',
            'duration_minutes': 75,
            'score': 1300,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'treasure_seeker',
            'region': 'north'
        },
        {
            'player': 'alice',
            'duration_minutes': 89,
            'score': 1033,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'treasure_seeker',
            'region': 'north'
        },
        {
            'player': 'diana',
            'duration_minutes': 40,
            'score': 1957,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'speed_runner',
            'region': 'central'
        },
        {
            'player': 'charlie',
            'duration_minutes': 31,
            'score': 2845,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'speed_runner',
            'region': 'west'
        },
        {
            'player': 'frank',
            'duration_minutes': 36,
            'score': 769,
            'mode': 'competitive',
            'completed': False,
            'achievements': 'boss_hunter',
            'region': 'west'
        },
        {
            'player': 'bob',
            'duration_minutes': 92,
            'score': 1428,
            'mode': 'casual',
            'completed': True,
            'achievements': 'first_blood',
            'region': 'central'
        },
        {
            'player': 'diana',
            'duration_minutes': 39,
            'score': 371,
            'mode': 'casual',
            'completed': False,
            'achievements': 'treasure_seeker',
            'region': 'south'
        },
        {
            'player': 'diana',
            'duration_minutes': 118,
            'score': 2733,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'boss_hunter',
            'region': 'east'
        },
        {
            'player': 'bob',
            'duration_minutes': 100,
            'score': 2399,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'combo_king',
            'region': 'west'
        },
        {
            'player': 'diana',
            'duration_minutes': 51,
            'score': 998,
            'mode': 'casual',
            'completed': False,
            'achievements': 'level_master',
            'region': 'north'
        },
        {
            'player': 'alice',
            'duration_minutes': 24,
            'score': 2670,
            'mode': 'casual',
            'completed': False,
            'achievements': 'level_master',
            'region': 'south'
        },
        {
            'player': 'diana',
            'duration_minutes': 81,
            'score': 2017,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'first_blood',
            'region': 'north'
        },
        {
            'player': 'frank',
            'duration_minutes': 118,
            'score': 2299,
            'mode': 'competitive',
            'completed': False,
            'achievements': 'level_master',
            'region': 'central'
        },
        {
            'player': 'diana',
            'duration_minutes': 25,
            'score': 1958,
            'mode': 'casual',
            'completed': False,
            'achievements': 'speed_runner',
            'region': 'west'
        },
        {
            'player': 'alice',
            'duration_minutes': 116,
            'score': 2661,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'speed_runner',
            'region': 'central'
        },
        {
            'player': 'bob',
            'duration_minutes': 74,
            'score': 2272,
            'mode': 'casual',
            'completed': False,
            'achievements': 'explorer',
            'region': 'north'
        },
        {
            'player': 'alice',
            'duration_minutes': 51,
            'score': 1359,
            'mode': 'casual',
            'completed': True,
            'achievements': 'treasure_seeker',
            'region': 'west'
        },
        {
            'player': 'alice',
            'duration_minutes': 15,
            'score': 2090,
            'mode': 'casual',
            'completed': True,
            'achievements': 'speed_runner',
            'region': 'south'
        },
        {
            'player': 'eve',
            'duration_minutes': 26,
            'score': 1185,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'treasure_seeker',
            'region': 'west'
        },
        {
            'player': 'frank',
            'duration_minutes': 93,
            'score': 923,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'combo_king',
            'region': 'central'
        },
        {
            'player': 'diana',
            'duration_minutes': 120,
            'score': 2219,
            'mode': 'competitive',
            'completed': True,
            'achievements': 'treasure_seeker',
            'region': 'east'
        },
        {
            'player': 'alice',
            'duration_minutes': 48,
            'score': 186,
            'mode': 'ranked',
            'completed': True,
            'achievements': 'treasure_seeker',
            'region': 'north'
        },
        {
            'player': 'alice',
            'duration_minutes': 95,
            'score': 2684,
            'mode': 'casual',
            'completed': True,
            'achievements': 'level_master',
            'region': 'north'
        },
        {
            'player': 'charlie',
            'duration_minutes': 14,
            'score': 2205,
            'mode': 'casual',
            'completed': False,
            'achievements': 'explorer',
            'region': 'east'
        },
        {
            'player': 'eve',
            'duration_minutes': 21,
            'score': 2438,
            'mode': 'ranked',
            'completed': False,
            'achievements': 'treasure_seeker',
            'region': 'south'
        },
        {
            'player': 'diana',
            'duration_minutes': 29,
            'score': 486,
            'mode': 'casual',
            'completed': False,
            'achievements': 'pixel_perfect',
            'region': 'south'
        },
        {
            'player': 'diana',
            'duration_minutes': 64,
            'score': 321,
            'mode': 'ranked',
            'completed': True,
            'achievements': 'first_blood',
            'region': 'south'
        }
    ],
    'game_modes': ['casual', 'competitive', 'ranked'],
    'achievements': [
        'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
        'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
    ]
}
print("=== List Comprehension Examples ===")
high_scores = [
    score['player'] for score in data['sessions']
    if score['score'] > 2000]
print(f"High scorers (>2000): {high_scores}")
minutes_max = [
    score['duration_minutes'] for score in data['sessions']
    if score['duration_minutes'] > 100]
print(f"High minutes (>100): {minutes_max}")
active_player = [
    player['player'] for player in data['sessions']
    if player['mode'] == 'ranked']
print(f"Active players: {active_player}\n")

print("=== Dict Comprehension Examples ===")
player_scores = {
    k: i['total_score'] for k, i
    in data['players'].items()}
print(f"Player scores: {player_scores}")
ranked_categories = {
    k: i['favorite_mode'] for k, i
    in data['players'].items() if i['favorite_mode'] == 'ranked'
}
print(f"Categories ranked: {ranked_categories}")
achievement_counts = {
    k: i['achievements_count'] for k, i
    in data['players'].items()}
print(f"Achievement counts: {achievement_counts}\n")

print("=== Set Comprehension Examples ===")
unique_players = {
    player['player'] for player in data['sessions']}
print(f"Unique players: {unique_players}")
unique_achievements = {
    achievement['achievements'] for achievement in
    data['sessions']
    }
print(f"Unique achievements: {unique_achievements}")
active_regions = {
    region['region'] for region in data['sessions']
    if region['completed'] is True}
print(f"Active regions: {active_regions}\n")

print("=== Combined Analysis ===")
total_player = {
    player['player'] for player in data['sessions']}
print(f"Total players: {len(total_player)}")
average_score = [
    score['total_score'] for score in data['players'].values()
    ]
print(f"Average score: {(sum(average_score) / len(total_player)):.1f}")
max_score = max(average_score)
print(max_score)
top_perfomer = {
    player: i for player, i in data['players'].items()
    if i['total_score'] == max_score}
top_perfomer_name = max([name for name in top_perfomer.keys()])
top_perfomer_stats = max([
    stats['achievements_count'] for stats
    in top_perfomer.values()])
print(
    f"Top performer: {top_perfomer_name} ({max_score} points, "
    f"{top_perfomer_stats} achievements)")
