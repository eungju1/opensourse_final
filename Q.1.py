def solution(my_string, target): #my_strung -> my_string���� ����(��Ÿ�� �����ؼ� string�̶� �����߽��ϴ�.)
    answer = 0

    # target ���ڿ��� ����
    target_length = len(target) #len() �Լ��� ����ϸ� ���ڿ��� ���̸� ���� �� �� �ְ� 
                                #target_length = len(target) �ڵ�� target�� ����ִ� ���ڿ��� ���̸� ��� �� ������ target_length��� �̸��� ������ ������ �� �ְ� �߽��ϴ�.

    for i in range(len(my_string) - target_length + 1): # my_string�� ���̿��� target�� ���̸� ���� 1�� ���� ������ �ݺ��Ͽ�     
        if my_string[i:i + target_length] == target:        #target�� ���̸� �κ� ���ڿ��� my_string���� ���ϱ� ���� ��ȸ ���� ����
            answer = 1 #�κ� ���ڿ��� target�� ��ġ�Ѵٸ� answer�� 1�� �Ҵ��ϰ� �߽��ϴ�.
            break  # �κ� ���ڿ��� ã�����Ƿ� �ݺ��� ����

    return answer

# Q.1
my_str = "abcdef"#(abcdef)���ڿ��� my_str�� �Ҵ��߽��ϴ�.
sub_str = "cde"#(cde)�� sub_str �Ҵ��߽��ϴ�.
result = solution(my_str, sub_str)#solution() �Լ��� ȣ���Ͽ� my_str���� sub_str�� �κ� ���ڿ��� �����ϴ��� Ȯ���ϰ� �߽��ϴ�
print(result)  # my_str(abcdef)�ȿ� sub_str(abc)�� 1�� �ݺ��ϹǷ� ����� �ϸ� 1 �� ���ɴϴ�.

