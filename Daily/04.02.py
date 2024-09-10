def solution(code):
    ret = ''
    mode = 0
    idx = 0
    for i in code:
        if mode == 0:
            if code[idx] != '1' and idx %2 == 0 :
                ret += i
            elif code[idx] == '1' :
                mode = 1
        else:
            if code[idx] != '1' and idx % 2 != 0 :
                ret += i
            elif code[idx] == '1' :
                mode = 0
        print(ret, idx)
        idx += 1
        
    if ret == '':
        ret = "EMPTY"
    print(ret)
    return ret

solution(	"abc1abc1abc")