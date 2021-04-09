def numberOfWaysToTraverseGraph(width, height):
	ways = [[1 for x in range(width)] for y in range(height) ]  
	for h in range(1,height):
		for w in range(1,width):
			ways[h][w] = ways[h-1][w] + ways[h][w-1]
    return ways[-1][-1]
