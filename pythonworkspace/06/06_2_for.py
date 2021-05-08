# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waitng_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waitng_no))

#randrange() 배울 때 배운 거
# for waitng_no in range(5): # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(waitng_no))

# for waitng_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waitng_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))