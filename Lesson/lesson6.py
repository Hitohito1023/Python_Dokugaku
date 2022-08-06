# # # # author = "Kafka"

# # # # print(author[0])
# # # # print(author[4])

# # # print("cat" + "dog" + "bird")

# # # print("aiueo" * 3)

# # print("hello".upper())

# # print("HELLO".lower())

# # name = "Jon"
# # print("こんにちは,{}".format(name))

# # what = input("何が：")
# # when = input("いつ：")
# # where = input("どこで：")
# # do = input("どうした：")
# # r = "{}は{}に{}で{}。".format(what,when,where,do)
# # print(r)

# # print("簡単->ムズカシ".split("->"))

# # code = "グーチョキパー"
# # print("->".join(code))

# # code2 = ["グー", "チョキ", "パー"]
# # print("->".join(code2))

# ###  1
# word = "カミュ"
# print(word[0])
# print(word[1])
# print(word[2])

# ### 2
# what = input("書いたもの：")
# who = input("宛先：")
# msg = "私は昨日{}を書いて、{}に送った！".format(what,who)
# print(msg)

# 3
# msg = "aldous Huxley was born in 1894"
# print(msg.capitalize())


## 4
# msg = "どこで？ 誰が？ いつ？".split(" ")
# print(msg)
# lst = "Where now? Who now? When now?".split("?")
# print(lst)

## 5
# str = ["The", "fox", "jumped", "over", "the", "fence", "."]
# msg = " ".join(str[:6]) + str[6]
# print(msg)

##6
# str = "A screaming comes across the sky."
# msg = str.replace("s", "$")
# print (msg)

## 7
# word = "Hemingway"
# print(word.index("m"))

## 8
# chal8 = "\"Wow!\" she said. \"This is a stupid challenge\" Kurt interrupted."
# print(chal8)

## 9
# str = "three " + "three " + "three"
# print(str)
# word = "three " * 3
# # print(word.strip())
# print(word[:-1])

## 10
str = "4月の晴れた寒い日で、時計がどれも十三時を打っていた。"
msg = str[:str.index("、")]
print(msg)