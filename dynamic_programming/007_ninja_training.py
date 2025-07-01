def ninja_training(day,last,input):
    if day==0:
        base_max=0
        for i in range(3):
            if i!=last:
                base_max=max(base_max, input[day][i])
        return base_max
    level_max=0
    for i in range(3):
        if i != last:
            current_points = input[day][i]+ninja_training(day-1, i, input)
            level_max=max(level_max, current_points)
    return level_max

def ninja_training_memo(day,last, input,dp=None):
    if dp is None:
        n = len(input)
        dp = [[-1 for _ in range(4)] for _ in range(n)]
    if day==0:
        base_max=0
        for i in range(3):
            if i!=last:
                base_max=max(base_max,input[day][i])
        return base_max
    if dp[day][last] != -1:
        return dp[day][last]
    level_max=0
    for i in range(3):
        if i != last:
            current_points = input[day][i]+ninja_training_memo(day-1,i, input,dp)
            level_max=max(level_max,current_points)
    dp[day][last]=level_max
    return dp[day][last]


def ninja_training_tabulation(day,last, points,dp=None):
    n = len(points)
    if dp is None:
        dp = [[-1 for _ in range(4)] for _ in range(n)]
    for last in range(4):
        base_max = 0
        for i in range(3):
            if i != last:
                base_max = max(base_max, points[0][i])
        dp[0][last]=base_max
    for d in range(1,n):
        for last in range(4):
            level_max = 0
            for i in range(3):
                if i != last:
                    current_points = points[day][i] + dp[day - 1][i]
                    level_max = max(level_max, current_points)
            dp[d][last] = level_max
    return dp[day][last]

