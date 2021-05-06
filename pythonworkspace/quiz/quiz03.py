url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(f"{url}의 비밀번호는 {password}입니다.")
print("%s의 비밀번호는 %s입니다." % (url, password))
print("{}의 비밀번호는 {}입니다.".format(url, password))