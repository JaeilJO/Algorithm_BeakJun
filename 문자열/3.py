from string import ascii_lowercase
S= input()
alphabet_list = list(ascii_lowercase)
for i in alphabet_list:
    if i in S:
        a = S.index(i)
        print(a,end=' ')
    else:
        print(-1, end=' ')


# 괜찮은 코드
# find는 리스트에서 찾고 해당 인덱스를 반환해주며, 없다면 -1을 반환해준다
s = input()
for i in range(97,123):
    print(s.find(chr(i)),end=' ')