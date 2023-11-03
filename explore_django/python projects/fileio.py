s = "Harry is a good boy"

# with open("text.txt", "w") as f:
#     f.write(s)

fp = open("text.txt", "w")
fp.write(s)
fp.close()