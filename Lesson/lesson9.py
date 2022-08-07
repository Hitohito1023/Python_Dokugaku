import os
import csv


path = os.path.join()
path2 = os.path.join()
path3 = os.path.join()


# st = open(path, "w", encoding="utf-8")
# st.write("ファイル書き込みテストです")
# st.close()

# with open(path, "w", encoding="utf-8") as f:
# 	f.write("Hi from Python!")

# read_list = []
# with open(path, "r", encoding="utf-8") as f:
# 	read_list.append(f.read())

# print(read_list)

# with open(path2, "w", newline='') as f:
# 	w = csv.writer(f, delimiter=",")
# 	w.writerow(["one", "two", "three"])
# 	w.writerow(["four", "five", "six"])

# with open(path2, "r") as f:
# 	r = csv.reader(f, delimiter=",")
# 	for row in r:
# 		print(",".join(row))

# read_list = []
# with open(path3, "r", encoding="utf-8") as f:

# 	read_list = f.read().splitlines()
# 	# print(f.read())

# print(read_list)

# ans = input("あなたのお名前は？")
# with open(path, "w", encoding="utf-8") as f:
# 	f.write(ans)

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
list2 = [["トップガン", "リスキービジネス", "マイノリティレポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニングデイ", "マンオブファイアー", "フライト"]]


with open(path2, "w", newline='') as f:
	w = csv.writer(f, delimiter=",")
	for movies in list2:
		w.writerow(movies)