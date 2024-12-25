# برنامه‌ای بنویسید که ضرایب یک معادله درجه دوم را دریافت کند و ریشه های معادله راچاپ کند.
# zarib = input("Enter a,b,c: ")
# zarib = zarib.split()
# print(zarib)
# a , b , c = float(zarib[0]) , float(zarib[1]) , float(zarib[2])

# def risha(a,b,c):
#     delta = (b**2)-4*a*c
#     if delta>0:
#         javab_1 = (-b-(delta**0.5))/(2*a)
#         javab_2 = (-b+(delta**0.5))/(2*a)
#     elif delta==0:
#         javab_1 = javab_2 = (-b)//(2*a)
#     else:
#         print("This equation don't have any javab")
#     return [f"Risha 1: {javab_1}" , f"Risha 2: {javab_2}"]

# print(risha(a,b,c))


# برنامه‌ای بنویسید که یک عدد صحیح از ورودی دریافت و مشخص کند
# برای خورد کردن چنین مقدار پولی با سکه‌های یک تومانی، ۲ تومانی و ۱۰ تومانی به حداقل چه تعداد سکه نیازمندیم.
# (مثلا اگر کاربر ۲۳ را وارد کرد باید در خروجی بنویسد (دو سکه ۱۰ تومانی، یک سکه ۲ تومانی و یک سکه ۱ تومانی

# x = int(input("Enter the adad: "))

# def tarigha(adad):
#     seka_10 = (adad//10)
#     adad %= 10
#     seka_2 = (adad//2)
#     adad %= 2
#     seka_1 = (adad)
#     return f"seka 10 tomani: {seka_10} , seka 2 tomani: {seka_2} , seka 1 tomani: {seka_1}"

# print(f"برای تقسیم کردن میتوان طریقه های زیر را در نظر کرفت: ")
# print(tarigha(x))


# برنامه یی بنویسید که از ورودی عدد
# (n) را بکیرد و مجموع 1 تا (n) را محاسبه کند
# n = int(input("Enter your adad: "))
# sum = 0
# while n!=0:
#     sum += n
#     n -= 1

# print(sum)


# برنامه یی بنویسید که ورودی (n) را از کاربر دریافت و فاکتوریل آن را محاسبه کند
# n = int(input("Enter your adad: "))
# def factorial(n):
#     javab = 1
#     for i in range(1,n+1):
#         javab *= i
#     return javab
# print(factorial(n))
print("salam")
