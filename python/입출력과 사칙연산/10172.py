# 아래 예제와 같이 개를 출력하시오.

# 입력
# 없음

# 출력
# 개를 출력한다.

def solution():
    result = [[" " for i in range(10)] for j in range(5)]
    result[0][0] = "|"
    result[0][1] = "\\"
    result[0][2] = "_"
    result[0][3] = "/"
    result[0][4] = "|"
    result[1][0] = "|"
    result[1][1] = "q"
    result[1][3] = "p"
    result[1][4] = "|"
    result[1][8] = "/"
    result[1][9] = "}"
    result[2][0] = "("
    result[2][2] = "0"
    result[2][4] = ")"
    result[2][5] = "\""
    result[2][6] = "\""
    result[2][7] = "\""
    result[2][8] = "\\"
    result[3][0] = "|"
    result[3][1] = "\""
    result[3][2] = "^"
    result[3][3] = "\""
    result[3][4] = "`"
    result[3][9] = "|"
    result[4][0] = "|"
    result[4][1] = "|"
    result[4][2] = "_"
    result[4][3] = "/"
    result[4][4] = "="
    result[4][5] = "\\"
    result[4][6] = "\\"
    result[4][7] = "_"
    result[4][8] = "_"
    result[4][9] = "|"
    return result

for p in solution():
    print("".join(map(str, p)))