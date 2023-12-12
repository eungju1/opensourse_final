def solution(my_string, target): #my_strung -> my_string으로 변경(오타로 생각해서 string이라 변경했습니다.)
    answer = 0

    # target 문자열의 길이
    target_length = len(target) #len() 함수를 사용하면 문자열의 길이를 쉽게 알 수 있고 
                                #target_length = len(target) 코드는 target에 들어있는 문자열의 길이를 세어서 그 개수를 target_length라는 이름의 변수에 저장할 수 있게 했습니다.

    for i in range(len(my_string) - target_length + 1): # my_string의 길이에서 target의 길이를 빼고 1을 더한 값까지 반복하여     
        if my_string[i:i + target_length] == target:        #target의 길이를 부분 문자열을 my_string에서 비교하기 위해 순회 범위 설정
            answer = 1 #부분 문자열이 target과 일치한다면 answer에 1을 할당하게 했습니다.
            break  # 부분 문자열을 찾았으므로 반복문 종료

    return answer

# Q.1
my_str = "abcdef"#(abcdef)문자열을 my_str에 할당했습니다.
sub_str = "cde"#(cde)를 sub_str 할당했습니다.
result = solution(my_str, sub_str)#solution() 함수를 호출하여 my_str에서 sub_str이 부분 문자열로 존재하는지 확인하게 했습니다
print(result)  # my_str(abcdef)안에 sub_str(abc)가 1번 반복하므로 출력을 하면 1 이 나옵니다.

