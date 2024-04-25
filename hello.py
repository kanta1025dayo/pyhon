import random

def calc_game():
    operators = ["+", "-", "*", "/"]

    for _ in range(5):
        operator = random.choice(operators)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print(num1, num2, operator)

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            answer = num1 / num2

        user_input = input(f"{num1}{operator}{num2}は？")
        # 入力値を浮動小数点数または整数に変換する
        try:
            user_input = float(user_input) if '.' in user_input else int(user_input)
        except ValueError:
            print("数値を入力してください。")
            continue

        if user_input == answer:
            print("正解")
        else:
            print("不正解")

# 関数を外部で呼び出す
calc_game()
