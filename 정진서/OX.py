def solution(quiz):
    answer = []
    result_list = [equation.split() for equation in quiz]
    for i in range(len(quiz)):
        if result_list[i][1] == '+':
            if int(result_list[i][0]) + int(result_list[i][2]) == int(result_list[i][4]):
                answer.append('O')
            else :
                answer.append('X')
        if result_list[i][1] == '-':
            if int(result_list[i][0]) - int(result_list[i][2]) == int(result_list[i][4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer

quiz = ["3 - 4 = -3", "5 + 6 = 11"]

solution(quiz)