def solution(age):
    planet_names = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z" # 0부터 25까지의 숫자에 각각 알파벳을 대응시키는 리스트이고 숫자에 해당하는 알파벳을 찾을수 있습니다.
    ]

    age_str = str(age)  # 주어진 나이를 문자열로 변환합니다
    
    name = ""
    for num in age_str:
        index = int(num)
        name += planet_names[index] #index = int(num)은 문자로 표현된 숫자(num)를 정수형으로 변환하여 index에 할당하게 했습니다

    return "PROGRAMMER-" + name

# Q.3
age = 857
result = solution(age)
print(result)  # 출력 결과: PROGRAMME-ifh
