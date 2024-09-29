# [ ] 201 자료구조 1
# https://blog.naver.com/zzzxxx3166/223517272663

# [1] 단어 뒤집기 2
msg = input()
inside_tag = False
word = []
result = []

for char in msg:
    if char == '<':
        if word:
            result.extend(word[::-1])
            word = []
        inside_tag = True
        result.append(char)
    elif char == '>':
        inside_tag = False
        result.append(char)
    elif char == ' ':
        if inside_tag:
            result.append(char)
        else:
            if word:
                result.extend(word[::-1])
                word = []
            result.append(char)
    else:
        if inside_tag:
            result.append(char)
        else:
            word.append(char)

if word:
    result.extend(word[::-1])

print(''.join(result))
# [2] 쇠막대기 (실버2)


# [3] 오큰 수 

# [4] 오등큰 수


