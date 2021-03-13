# 暴力解法

def tournamentWinner(competitions, results):
	points = {}
	for i in range(len(results)):
		if results[i] == 0:
			#数字太多可读性低
			winner = competitions[i][1]
		else:
			winner = competitions[i][0]
		
		# TODO 有没有 check if esxist, otherwise crate one 函数 记好了
		if winner in points:
			points[winner] += 3
		else:
			points[winner] = 3
	# TODO lambda
	point_order  = lambda points: points[1]
	# 这里可以用sorted,但是增加复杂度到 logn
	points = sorted(points.items(), key = point_order, reverse = True)
    return points[0][0]



def tournamentWinner(competitions, results):
	# 增加代码可读性 空间换取时间
	HOME_TEAM_WON = 1 
	# 用于后续的 避免排序
	current_best_team = ""
	# boundary case
	points = {"": 0}
	
	# TODO: enumerate
	for idx, two_teams in enumerate(competitions):
		# 想不起来用
		home, away = two_teams 
		winner = home if results[idx] == HOME_TEAM_WON else away
		# 不独立可以
		update_winner_socore(winner, points)
		# linear sort
		if points[winner] > points[current_best_team]:
			current_best_team = winner
    return current_best_team

def update_winner_socore(winner, points):
	if winner in points.keys():
		points[winner] += 3
	else:
		points[winner] = 3