def solution(numbers):
    
    numbers = list(map(str, numbers)) # ���ڸ� ���ڿ��� ��ȯ�Ͽ� ��

    # �� �Լ� ����
    def compare(a, b):
        if a + b > b + a: # a + b�� b + a���� ū ��쿡 a�� �� �տ� �δ� ���Դϴ�
            return -1 # ���� ���� a + b �� �� ũ�� -1�� ��ȯ�˴ϴ�
        elif a + b < b + a: # a + b�� b + a���� ���� ��쿡 b�� �� �տ� �δ� ���Դϴ�
            return 1 # ���� ���� b + ark �� ũ�� 1�� ��ȯ�˴ϴ�
        else:
            return 0

    if numbers[0] == '0': # ���࿡ ����Ʈ ���� ��� ���ڰ� 0�� ���
        return '0' # 0 �� �˴ϴ�.

    return ''.join(numbers) # ''.join(numbers)�� ����Ʈ ���� ���ڿ� ��ҵ��� �ϳ��� ���ڿ��� ��Ĩ�ϴ�. (EX: numbers = [2, 3, 4] -> 234)

# Q.5
numbers = [8, 30, 17, 2, 23]
print(solution(numbers))  # ��� ���: 83017223
