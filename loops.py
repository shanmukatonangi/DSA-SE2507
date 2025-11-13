# temperature = 85
# if temperature < 90:
#     print("Let's go to the park!")
# else:
#     print("Let's stay indoors and read a book.")


# name="shanmukh"
# print




# if(temperature>60){
#     print("It's a nice day!")
# }else{
#     print("It's a bit chilly today.")
# }

# age=45

# if age>=18 and age<=35:
#     print("You are eligible to work.")
# elif age>35 and age<=50:
#     print("You have a lot of experience to offer.")
# else:
#     print("You are not eligible to work.")

# age = int(input("Enter your age: "))
# height = int(input("Enter your height in cm: "))
# if age >= 10:
#     print("You are old enough to ride the rollercoaster")
#     if height >= 120:
#         print("And you meet the height requirement.")
#     else:
#         print("But you do not meet the height requirement.")
# else:
#     print("You are not eligible to ride the rollercoaster because you are too young.")


# //age=9 height=125


# age = 25
# if age < 13:
#     print("Child.")
# elif 13 <= age <= 19:
#     print("Teenager.")
# else:
#     print("Adult.")


# elif: age>=13 and age<=19

# score = int(input("What is your numeric score? "))
# if score < 60:
#     letter_grade = "F"
# elif score < 70:
#     letter_grade = "D"
# elif score < 80:
#     letter_grade = "C"
# elif score < 90:
#     letter_grade = "B"
# else:
#     letter_grade = "A"
# print("Your letter grade is", letter_grade)

# 75


# i=0

# while i<5:
#     print(i)
#     i=i+1

# Example of a while loop
# while True:
#     response = input("Do you want to continue? (yes/no): ")
#     if response.lower() == 'no':
#         break  # Exit the loop if the user says 'no'
#     else:
#         print("Continuing the loop...")

# print("Loop has been terminated.")



# respone='yes'

# while(true)if(true){ break; console.log()}
    
# while True:
#     if True:
#         break
#     print("hello")


# for(i=0;i<5;i++){
#     console.log(i)
# }

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)

# numbers = [1, 2, 3, 4, 5]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# for(num of numbers){
#     if(num%2==0){
#         evennumbers.push(num)
#     }
# }

# def Hello():
#     print("Hello, World!")
#     return 24

# Hello()
# print(Hello())

def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            letter = letter.lower()
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

result = count_letters("abac")
print(result)

# def count_letters(word):



# def add2(x, y):
#     return x + y


# add = lambda x, y: x + y
# result = add(3, 4)
# print(result)  # Output: 7

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]