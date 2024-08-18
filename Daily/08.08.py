# [ ] 세솔 테크 코테 문제 복기 

# [ ] problem 1
# input :
# 주문한 메뉴 가격 [피자,치킨,보쌈, 김밥] , 할인율이 다른 쿠폰 리스트 [[50,0,0,30],[20,30,40,50]]
# output :
# [할인률이 가장 높은 쿠폰 번호, 할인된 총 가격]
# [500,0,200,0] -> 피자,보쌈만 주문 
# [500,0,0,200], [[0,20,30,0], [0,50,50,0]] 
# -> 주문한 음식에 적용되는 할인이 없어서 쿠폰 미적용과 가격이 같음 -> [-1,-1] 반환



def solution(price,coupon):
    n = 100000000000
    result = 10000000000
    
    for i in range(len(coupon)):
        cur_price = sum([price[j]*(1-(coupon[i][j]*0.01)) for j in range(len(price))])
        if result > cur_price :
            n = i
            result = int(cur_price)
    return [n+1,result] if sum(price) != result else [-1,-1]

# [ ] Problem 2
from collections import deque


def split_stepwise(message):
    result = []
    next_msg = []
    
    split_msg = deque(message)

    while split_msg:
        # 각 문자를 분리하여 다음 레벨 메시지를 생성
        msg = split_msg.popleft()
        # 다음 레벨 msg 생성
        next_msg.extend([m for m in msg.split(msg[0]) if m != ''])
     
        if not split_msg:
            break
        
    # 현재 단계에서 완전히 사라진 alpha 찾기
    result = set(''.join(message)) - set(''.join(next_msg))
    print(''.join(message),''.join(next_msg))
    print(next_msg,result)   
    return next_msg,sorted(result)


def solution(message):
    result = [ ] # 분해해서 사라진 알파벳 리스트
    next_msg = [message]
 
    while next_msg:
        next_msg, removed_aplpha = split_stepwise(next_msg)
        result.extend(removed_aplpha)
        if not next_msg:  # msg가 비어 있으면 반복 종료
            break
        
    return ''.join(result)
        
print(solution('banbanbact'))