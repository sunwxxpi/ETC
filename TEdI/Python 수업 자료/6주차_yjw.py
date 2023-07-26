# ==========================연습문제 1================================
# def even_odd(a):
#   if a % 2 ==1:
#     print(f'{a}는 홀수입니다')
#   elif a % 2 ==0:
#     print(f'{a}는 짝수입니다')
# num=int(input())
# even_odd(num)
# ==========================연습문제 2================================
# def sq_sum(n):
#   if n <= 1:
#     return 1
#   elif n >=2:
#     return n**2+sq_sum(n-1)
# num=int(input())
# print(sq_sum(num))
# ==========================연습문제 3================================
# def money(mon_per_hour , hour):
#   sum=(mon_per_hour)*hour*(1-3.3/100)
#   return sum
# mon_per_hour = int(input('시급을 입력하시오: '))
# hour = int(input('근무 시간을 입력하시오: '))
# sum = money(mon_per_hour , hour)
# print(f'월급은 : {round(sum, 2)}')

# ==========================연습문제 4================================
# def prime(n):
#   if n > num:
#     return
#   elif n <= num:
#     cnt = 0
#     for i in range(2, n):
#       if n % i ==0:
#         cnt += 1
#     if cnt ==0:
#       print(f'{n}', end=' ')
#     return prime(n+1)
# num=int(input())
# prime(2)
# ==========================연습문제 5================================
# def sum(n):
#   if n <= 1:
#     return 1
#   elif n >= 2:
#     return n + sum(n-1)
# num=int(input())
# print(sum(num))

# def sum(n):
#   cnt = 0
#   for i in range(1, n+1):
#     cnt += i
#   return cnt
# num=int(input())
# print(sum(num))
# ==========================연습문제 6================================
# def isValid(p):
#   if len(p) < 10:
#     return False
#   is_num = False
#   is_upper = False
#   english = 0
#   capital = 0
#   for i in range(0, len(p)):
#     if (ord(p[i]) >= 97 and ord(p[i]) <= 122) or (ord(p[i]) >= 65 and ord(p[i]) <= 90):
#       english += 1
#     if ord(p[i]) >= 65 and ord(p[i]) <= 90:
#       capital += 1
#   if english >= 1:
#     is_num = True
#   if capital >= 1:
#     is_upper = True
#   return is_upper and is_num
# print('비밀번호는 10자리 이상, 영문 대문자를 포함하여야 합니다.')
# pw = input('비밀번호 입력; ')
# if isValid(pw):
#   print('유효한 비밀번호입니다')
# else:
#   print('비밀번호가 잘못되었습니다! 다시 입력해 주세요')

# ===========================코드업 41================================
# a,b=map(int,input().split())
# print(a%b)
# ===========================코드업 42================================
# a=float(input())
# print(round(a,2))
# ===========================코드업 43================================
# a,b=map(float, input().split())
# print('{:.3f}'.format(a/b))
# ===========================코드업 44================================
# a,b=map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(round(a/b,2))
# ===========================코드업 45================================
# a,b,c=map(int, input().split())
# print(a+b+c, '{:.2f}'.format((a+b+c)/3))
# ===========================코드업 46================================
# a=int(input())
# print(a<<1)
# ===========================코드업 47================================
# a,b=map(int, input().split())
# print(a<<b)
# ===========================코드업 48================================
# a,b=map(int, input().split())
# print('True' if a < b else 'False')
# ===========================코드업 49================================
# a,b=map(int, input().split())
# print('True' if a == b else 'False')
# ===========================코드업 50================================
# a,b=map(int, input().split())
# print('True' if a <= b else 'False')
# ===========================코드업 51================================
# a,b=map(int, input().split())
# print('True' if a != b else 'False')
# ===========================코드업 52================================
# a=int(input())
# print('False' if a == 0 else 'True')
# ===========================코드업 53================================
# a=bool(int(input()))
# print(not a)
# ===========================코드업 54================================
# a,b=map(int, input().split())
# print(bool(a) and bool(b))
# ===========================코드업 55================================
# a,b=input().split()
# print(bool(int(a)) or bool(int(b)))