def solution(letter):
    morse = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
             '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
             '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
             '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
             '-.--': 'y', '--..': 'z'}

    letters = letter.split(' ')  # 모스 부호를 공백을 기준으로 분리했습니다.
    answer = ''
    for l in letters:
        if l == '':  # 공백을 발견하면, 공백 하나를 answer에 추가했습니다
            answer += ' '
        elif l in morse:  # 모스 부호 딕셔너리에 해당 모스 부호가 존재하면
            answer += morse[l]      # 해당 모스 부호에 대응되는 알파벳을 answer에 추가

    return answer

# 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.
given_morse = ".-- .- ... - . / -. --- / ..-. .-. . . ... .... / - . .- .-. ... / --- ...- . .-. / --- .-. / --- .-.. -.. / --. .-. .. . ..- ..-. ... "  
            # Waste no fresh tears over old griefs의 모스 부호(지나간일에 새로운 눈물을 낭비하지 말자)
result = solution(given_morse)
print(result)  # 출력 결과: wastenofreshtearsoveroldgriefs
