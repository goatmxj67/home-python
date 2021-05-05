python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # index + 1 부터 찾아준다.
print(index)

print(python.find("Java")) # 못 찾으면 -1 반환 / 찾으면 0
#print(python.index("Java")) # 못 찾으면 오류 -> 다음 줄 부터 실행 안함
print("hi")

print(python.count("n")) 