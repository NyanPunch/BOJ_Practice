# 가까운 수
def solution(array, n):
    # ans = 0 으로 초기화시 17번 18번 실패
    # [2, 3, 4], 1 을 예로 들 수 있음
    ans = array[0] 

    for i in array:
        if abs(n - ans) > abs(n - i):
            ans = i 
        elif abs(n - ans) == abs(n - i):
            ans = min(i, ans)
    return ans
