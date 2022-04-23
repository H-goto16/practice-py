problems = {
    "りんご":"apple",
    "犬":"dog"
}

value = input("Q: 「りんご」")

if value == problems["りんご"]:
    print("正解")
elif value == problems["犬"]:
    print("正解")
else:
    print("不正解")