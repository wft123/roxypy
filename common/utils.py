def comb(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


def perm(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret


def dfs_comb(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1] + 1, len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret


def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)
    return ret

def search_map(data, s, e):
    n = len(data)
    m = 99999
    i, j, k=0
    v, dist, via = []
    min

    print("시작 : {}, 도착 : {}".format(s, e))

    for j in range(0, n):
        via[0] = -1
        v[j] = 0
        dist[j] = m

    dist[s-1] = 0

    for i in range(0, n):
        min = m
        for j in range(0, n):
            if v[j] == 0 and dist[j] < min:
                k = j
                min = dist[j]
        v[k] = 1
        for a in v:
            print(a, end=" ")
        print()
        if min == m:
            break
        for j in range(0, n):
            if dist[j] > dist[k] + data[k][j]:
                dist[j] = dist[k] + data[k][j]
                via[j] = k
        path = []
        path_cnt = 0
        k = e-1

        while True:
            path[path_cnt] = k
            if k == s-1:
                break
            k = via[k]

        for i in range(path_cnt-1, 1, -1):
            print("{} -> ".format(path[i]), end=" ")
        print("{} -> ".format(path[i]))



def search_map(data):
    n = 6
    length = 0
    label = list(range(0, n))

    data.sort(key=lambda d: d[2])

    nodes, idx, cost, tmp = 0, 0, 0, 0

    while nodes < n-1:
        if label[data[idx][0]-1] != label[data[idx][1]-1]:
            tmp = label[data[idx][1]-1]
            for i in range(0, n):
                if tmp == label[i]:
                    label[i] = label[data[idx][0]-1]
            cost += data[idx][2]
            nodes += 1
        idx += 1

    return cost