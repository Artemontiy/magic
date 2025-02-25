#Арифметические операции с числами 
 

#Сложение 
value1 = 20 
value2 = 30
result = value1 + value2
print(result)


#Простой калькулятор на сложение

requestValue1 = int(input("Введите первое значение"))
requestValue2 = int(input("Введите второе  значение"))
resultValue = requestValue1 + requestValue2
print(f"Результат сложения {resultValue}")

#Калькулятор степени

# requestValue3 = int(input("Введите первое значение"))
# requestValue4 = int(input("Введите второе значение"))
# resultValue = requestValue3 ** requestValue4
# print(f"Результат cтепени {resultValue}")

#Для того чтобы разделить нужно поставить "/",для того чтобы разделить с остатком нужно поставить "%"

#условная конструкция "if"
#Простая авторизация 
# login = input("Введите логин")
# password = input("Введите пароль")
# fallbackOption = input("Введите запасной пароль")
# if login == "artemiy111" and password == "artemiy":
#     print("Вход разрешен.Данные корректны! Welcome!")
# elif fallbackOption == "123":
#     print("Вы успешно зашли при помощи запасного пароля")
# else:
#  print("Ошибка! Вы ввели неккоректный основной и запасной пароль и логин ")
# # == - знак сравнения 

#Проверка возраста
# requestAge = int(input("Введите возраст"))
# if requestAge > 0 and requestAge <= 18:
#     print("Увы зайдите когда будет 19")
# elif requestAge >= 19 and requestAge <= 45:
#     print("Вам можно пить энергетики ,но не думайте что вы бессмертны")
# elif requestAge >= 46 and requestAge <= 70:
#     print("You will die tomorrow if you drink energydrinks!")
# else:
#     print("Сдохнешь")

#Проверка времени 

requestTime = float(input("ВВедите время\t3/"))
if requestTime >= 04.01 and requestTime <= 12.00:
    print("Now it is morning\n")
elif requestTime >=12.01 and requestTime <= 15.00:
    print("Now it is noon\n")
elif requestTime >= 15.01 and requestTime <= 18.00:
    print("Now it is afternoon\n")
elif requestTime >= 18.01 and requestTime <= 21.00:
    print("Now it is evening\n")     
elif requestTime >= 21.01 and requestTime <= 4.00:
    print("Now it is night\n")
else:
    print("ERROR\n")         

# условная конструкция (if\else\elif) состоят из условий и блоков. Если условия выполняются ,то срабатывает определенный блок.










