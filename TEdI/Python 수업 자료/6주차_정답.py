# 연습문제
# 1

def even_odd(n) :
    if n % 2 == 0 :
        print("%d는 홀수 입니다" % n)
    else :
        print("%d는 짝수 입니다" % n)


# 2
def Number(num) :
    list_new = []
    for x in range(1, num + 1) :
        list_new.append(x**2)
    return list_new
n = int(input("n 값을 입력하세요:"))
num_list = Number(n)
print(num_list)

# 3

def payment(pay, hour) :
    return pay * hour * 0.97

pay = int(input('시급을 입력하시요 :'))
hour = int(input('근무 시간을 입력하시오 :'))
p = payment(pay, hour)
print("월급은 :", p)


#4

def prime(n) :
    if n < 2 :
        print("1 이상의 수 입력해주세요")
        return 0
    for x in range(2, n) :
        if n % x == 0 :
            return False
    return True

def p(n) :
    for x in range(2, n+1) :
        if prime(x):
            print("%d 소수 입니다"% x)

# 5
def s(n) :
    if n < 1:
        return n 
    return s(n-1) + n

# 6
def isValid(p):
    if len(p)<10:
        return False
    is_num=False
    is_upper=False
    for x in p:
        if x.isupper() :
            is_upper = True
        if x.isdigit():
            is_num = True 
    
    return is_upper and is_num

print("▶ 비밀번호는 10자리 이상, 영문 대문자를 포함하여야 합니다.")
pw = input("비밀번호 입력 :")
if isValid(pw):
    print("유효한 비밀번호입니다")
else: 
    print("비밀번호가 잘못되었습니다! 다시 입력해 주세요")
                
        
