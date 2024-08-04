text1 = "dfghjkl;lkjhgf"
# incorrect

res = text1.replace("j", "h").replace("h", "0")

#not effective

res2 = ""

for char in text1:
    if char == "j":
        res2 += "h"
    elif char == "h":
        res2 += "0"

print(res2)


translate_map = str.maketrans("jhs", "h0M")

res3 = text1.translate(translate_map)
print(res3)


