# name = "Ted"
# for character in name:
#   print(character)

# shows = ["GOT", "Narcos", "Vice"]
# for show in shows:
#   print(show)

# coms = ("A. Development", "Friends", "Always Sunny")
# for show in coms:
#   print(show)

# people = {"G. Bluth II": "A. Development",
#           "Barney": "HIMYM",
#           "Dennis": "Always Sunny"
#         }
# for character in people:
#   print(people[character])

# tv = ["GOT", "Narcos", "Vice"]
# i = 0
# for show in tv:
#   new = tv[i]
#   new = new.upper()
#   tv[i] = new
#   i += 1
# print(tv)

# for i in range(1, 11):
#   print(i)

# x = 10
# while x > 0:
#   print('{}'.format(x))
#   x -= 1
# print("Happy New Year!")

# for i in range(1,6):
#     if i == 3:
#     	continue
#     print(i)

# for i in range(1, 3):
# 	print(i)
# 	for letter in ["a", "b", "c"]:
# 		print(letter)

# titles = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
# for title in titles:
# 	print(title)

# for i in range(25, 51):
# 	print(i)

# titles = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
# for i, title in enumerate(titles):
# 	print(str(i) + ":" + title)

# list = [3, 6, 8, 9]
# while True:
# 	print("qで終了します")
# 	ans = input("数字を当てよう！！")
# 	if ans == "q":
# 		break
# 	elif int(ans) in list:
# 		print("正解です！！")
# 	else:
# 		print("残念！")

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
ans_list = []

for i in list1:
	for j in list2:
		ans = i * j
		ans_list.append(ans)

print(ans_list)