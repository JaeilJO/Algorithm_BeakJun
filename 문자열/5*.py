words = input().upper()
unique_words = list(set(words)) 
cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt) 
    
if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])