def solution(age):
    planet_names = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z" # 0���� 25������ ���ڿ� ���� ���ĺ��� ������Ű�� ����Ʈ�̰� ���ڿ� �ش��ϴ� ���ĺ��� ã���� �ֽ��ϴ�.
    ]

    age_str = str(age)  # �־��� ���̸� ���ڿ��� ��ȯ�մϴ�
    
    name = ""
    for num in age_str:
        index = int(num)
        name += planet_names[index] #index = int(num)�� ���ڷ� ǥ���� ����(num)�� ���������� ��ȯ�Ͽ� index�� �Ҵ��ϰ� �߽��ϴ�

    return "PROGRAMMER-" + name

# Q.3
age = 857
result = solution(age)
print(result)  # ��� ���: PROGRAMME-ifh
