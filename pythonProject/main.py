isMarried = False
print(isMarried)  # False

isAlive = True
print(isAlive)  # True

a = 0b11
b = 0b1011
c = 0b100001
print(a)    # 3 в десятичной системе
print(b)    # 11 в десятичной системе
print(c)    # 33 в десятичной системе
print(type(a))
print(type(isMarried))

first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(round(third_number,5)) # 0.40002000000000004

number = 5 # в двоичной форме 101
print(f"number = {number:0b}")  # number = 101

x = 45  # Значение, которое надо зашифровать - в двоичной форме 101101
key = 102  # Пусть это будет ключ - в двоичной форме 1100110

encrypt = x ^ key  # Результатом будет число 1001011 или 75
print(f"Зашифрованное число: {encrypt}")

decrypt = encrypt ^ key  # Результатом будет исходное число 45
print(f"Расшифрованное число: {decrypt}")

message = "hello world!"
hello = "hello"
print(hello in message)  # True - подстрока hello есть в строке "hello world!"

print(3 or 1)

print(bool(" ") + 5)