import random
def calc_game():
    operators = ["+","-","*","/"]
    
    for _ in range(5):
        operator = random.choice(operators)
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        num2
        print(num1, num2, operator)
        
        if  operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2       
        elif operator == "/":
            answer = num1 / num2     
        user_input = imput(f"{num}{operator}{num2}は？")
        
        if user_imput == answer:
            print("正解")
        else:
            print("不正解")
                
    
    calc_game()