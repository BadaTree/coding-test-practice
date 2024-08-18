# [ ] TODO : 자료구조 1 (연습)

# [1] 단어 뒤집기 2 (백준 17413, 실버 3 )
# https://www.acmicpc.net/problem/17413
# msg = input()
msg = '<open> gat <close>'
msg_list = msg.split()
for s in msg:
    if '<' in s:
        print("&&&&&",s)
print([s if '<' in s else s[::-1] for s in msg_list ])


# [2] 쇠막대기 (백준 10799, 실버 2)
# https://www.acmicpc.net/problem/10799