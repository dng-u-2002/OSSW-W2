def get_integer(prompt):
    """사용자가 올바른 정수를 입력할 때까지 반복하는 함수"""
    while True:
        try:
            return int(input(prompt))
        except (ValueError, OSError):
            print('잘못된 입력입니다. 정수를 입력해주세요.')

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == '__main__':
    input1 = get_integer('\n첫번째 숫자를 입력하세요.\n입력: ')

    while True:
        act = input('\n원하는 사칙연산 기호 중 하나를 선택하세요.(+, -, *, /)\n기호: ')
        if act in ['+', '-', '*', '/']:
            break
        print('잘못된 입력입니다. 올바른 연산 기호를 입력해주세요.')

    input2 = get_integer('\n두번째 숫자를 입력하세요.\n입력: ')

    if act == '+':
        result = plus(input1, input2)
    elif act == '-':
        result = minus(input1, input2)
    elif act == '*':
        result = mul(input1, input2)
    elif act == '/':
        result = divide(input1, input2)

    print(f'사칙연산 결과는 {result}입니다.')
