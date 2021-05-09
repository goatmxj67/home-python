def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        # return pow(height/100, 2) * 22
        return pow(height, 2) * 22
    else:
        # return pow(height/100, 2) * 21
        return pow(height, 2) * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
