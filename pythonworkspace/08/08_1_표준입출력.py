# print("Python", "Java", sep=" vs ", end="? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력
# print("Python", "Java", file=sys.stderr) # 표준에러

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 입력 받은 값은 언제나 str 타입

# 하지만 이렇게 변수를 지정하면 int 타입
answer = 10
print(type(answer))
