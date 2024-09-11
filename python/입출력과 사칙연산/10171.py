# 아래 예제와 같이 고양이를 출력하시오.

# 입력
# 없음

# 출력
# 고양이를 출력한다.

def solution():
    result = [[" " for i in range (8)] for h in range(4)]
    result[0][0] = "\\"
    result[0][5] = "/"
    result[0][6] = "\\"
    result[1][1] = ")"
    result[1][4] = "("
    result[1][6] = "'"
    result[1][7] = ")"
    result[2][0] = "("
    result[2][3] = "/"
    result[2][6] = ")"
    result[3][1] = "\\"
    result[3][2] = "("
    result[3][3] = "_"
    result[3][4] = "_"
    result[3][5] = ")"
    result[3][6] = "|"
    return result

for p in solution():
    print("".join(map(str, p)))

