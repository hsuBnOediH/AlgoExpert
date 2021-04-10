# 这个方法行不通  需要分析一下 0 不指向 所有都指向0 的情况
# cycle 应该首先想到的 链接的祖先 需要有个地方记录祖先， 最好的方法应该是dfs 不是 bfs
def cycleInGraph(edges):
    visited = [False for i in range(len(edges))]
    need_check = []
    next_i = get_next_uncheck(edges, visited)
    while next_i is not None:
        visited[next_i] = True
        need_check.extend(edges[next_i])
        has_cycle = bfs(need_check, edges, visited)
        if has_cycle: return True
        next_i = get_next_uncheck(edges, visited)
    return False


def bfs(need_check, edges, visited):
    while len(need_check) > 0:
        v = need_check.pop(0)
        v_con = edges[v]
        for target in v_con:
            if visited[target]:
                return True
            elif target not in need_check:
                need_check.append(target)
        visited[v] = True
    return False


def get_next_uncheck(edges, visited):
    for node in range(len(edges)):
        if visited[node]:
            continue
        else:
            return node
    return None



### dfs solution
# dfs
def cycleInGraph(edges):
    numberOfNode = len(edges)
    visited = [False for _ in range(numberOfNode)]
    # 专门用来记录祖先的stack
    currentlyInStack = [False for _ in range(numberOfNode)]

    # for loop 处理 上来就是空的情况 0 谁都不连接
    for node in range(numberOfNode):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True

    return False


def isNodeInCycle(node, edges, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    c_arr = edges[node]
    for c in c_arr:
        if not visited[c]:
            res = isNodeInCycle(c, edges, visited, currentlyInStack)
            if res:
                return True
        elif currentlyInStack[c]:
            return True
    # 相当于拿出来stack
    currentlyInStack[node] = False
    return False

# 明天写一个自己理解的dfs 出来
