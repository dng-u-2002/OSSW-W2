def get_integer(prompt):
    """Prompt the user to input a valid integer within a specific range."""
    while True:
        try:
            value = int(input(prompt))
            if -1000 <= value <= 1000:  # Restrict input range to -1000 to 1000
                return value
            print('입력값이 허용 범위를 벗어났습니다. -1000에서 1000 사이의 값을 입력해주세요.')
        except ValueError:
            print('잘못된 입력입니다. 정수를 입력해주세요.')
        except OSError:
            print('입력 오류가 발생했습니다. 다시 시도해주세요.')

def perform_operation(a, b, operator):
    """Perform the operation based on the operator."""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None
    }
    return operations[operator](a, b)

def get_operator():
    """Prompt the user to input a valid operator."""
    while True:
        operator = input('\n원하는 사칙연산 기호 중 하나를 선택하세요.(+, -, *, /)\n기호: ').strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        print('잘못된 입력입니다. 올바른 연산 기호를 입력해주세요.')

def calculate(num1, num2, operator):
    """Perform the calculation and handle division by zero."""
    while True:
        result = perform_operation(num1, num2, operator)
        if result is not None:
            return result
        print('0으로 나눌 수 없습니다. 다시 입력해주세요.')
        num2 = get_integer('\n두번째 숫자를 다시 입력하세요.\n입력: ')

def main():
    """Main function to execute the calculator program."""
    num1 = get_integer('\n첫번째 숫자를 입력하세요.\n입력: ')
    operator = get_operator()
    num2 = get_integer('\n두번째 숫자를 입력하세요.\n입력: ')
    result = calculate(num1, num2, operator)
    print(f'사칙연산 결과는 {result}입니다.')

if __name__ == '__main__':
    main()