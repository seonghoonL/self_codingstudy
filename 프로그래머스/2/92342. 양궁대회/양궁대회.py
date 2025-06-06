import copy
def solution(n, info):
    best_diff = 0
    best_alloc = [-1]
    curr = [0] * 11
    def calc_diff():
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if info[i] == 0 and curr[i] == 0:
                continue
            if curr[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i
        return ryan_score - apeach_score
    def dfs(index, arrows_left):
        nonlocal best_diff, best_alloc
        if index == 10:
            curr[10] = arrows_left
            diff = calc_diff()
            if diff > 0:
                if diff > best_diff:
                    best_diff = diff
                    best_alloc = copy.deepcopy(curr)
                elif diff == best_diff:
                    for i in range(10, -1, -1):
                        if curr[i] > best_alloc[i]:
                            best_alloc = copy.deepcopy(curr)
                            break
                        elif curr[i] < best_alloc[i]:
                            break
            curr[10] = 0
            return
        needed = info[index] + 1
        if arrows_left >= needed:
            curr[index] = needed
            dfs(index + 1, arrows_left - needed)
            curr[index] = 0
        dfs(index + 1, arrows_left)
    dfs(0, n)
    return best_alloc