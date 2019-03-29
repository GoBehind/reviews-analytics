data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)

print('總共有', len(data), '筆資料, 檔案分析中請稍後 :)')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

# for word in wc:
# 	if wc[word] > 100:
# 		print(word, '出現 ', wc[word], '次')

while True:
	print('輸入[outofprogram]離開')
	word = input('請輸入想查詢的字: ')
	if word in wc:
		print(word, '出現次數為: ', wc[word], '次')
	
	elif word == 'outofprogram':
		break

	else:
		print('留言中沒有出現', word)
		





# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('每筆留言平均長度是: ', sum_len / len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')