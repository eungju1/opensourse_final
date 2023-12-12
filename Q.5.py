def solution(numbers):
    
    numbers = list(map(str, numbers)) # 숫자를 문자열로 변환하여 비교

    # 비교 함수 정의
    def compare(a, b):
        if a + b > b + a: # a + b가 b + a보다 큰 경우에 a를 더 앞에 두는 식입니다
            return -1 # 위와 같이 a + b 가 더 크면 -1이 반환됩니다
        elif a + b < b + a: # a + b가 b + a보다 작은 경우에 b를 더 앞에 두는 식입니다
            return 1 # 위와 같이 b + ark 더 크면 1이 반환됩니다
        else:
            return 0

    if numbers[0] == '0': # 만약에 리스트 값이 모든 숫자가 0인 경우
        return '0' # 0 이 됩니다.

    return ''.join(numbers) # ''.join(numbers)는 리스트 내의 문자열 요소들을 하나의 문자열로 합칩니다. (EX: numbers = [2, 3, 4] -> 234)

# Q.5
numbers = [8, 30, 17, 2, 23]
print(solution(numbers))  # 결과 출력: 83017223
