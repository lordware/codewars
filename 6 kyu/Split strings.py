def solution(s):
    result = [s[i:i + 2] for i in range(0, len(s), 2)]
    if len(result) == 0:
        return []
    if len(result[-1]) == 1:
        result[-1] += '_'
    return result
