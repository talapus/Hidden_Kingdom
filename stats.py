def character_stats(max_points):
    skill_points = 10
    stats = {'STR' : 0, 'STA' : 0, 'CHA' : 0 }
    while True:
        for stats in stats.values():
            if skill_points < max_points:
               stats = randint(0, max_points)
    return stats