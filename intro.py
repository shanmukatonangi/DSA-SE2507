# # num=10
# # print(num)
# # fruits = ["apple", "banana", "mango",12,True]
# # print(fruits[2])

# # colors = {"red", "blue"}
# # print(colors)



# # user = {
# #     "name": "John",
# #       "age": 30
# #       }

# # my_first_string = 'Hello World !!!'
# # print(my_first_string) 

# # #python
# # # Single word
# # my_first_string = 'Hello World !!!'
# # print(my_first_string)  # Output: Hello World !!!

# # # Entire phrase
# # phrase = 'Statistics sits at the heart of machine learning'
# # print(phrase)

# # # Double quotes
# # my_string = "String built with double quotes"
# # print(my_string)

# # # Using escape characters
# # print('I\'m fine. How are you?')

# # # Multiline string
# # print('''
# # Student : I\'m fine. How are you?
# # Instructor : I am doing fine
# # ''')

# # # Replacing a word
# # message = "Hey muddy, how are you doing?"
# # message = message.replace('muddy', 'buddy')
# # print(message)

# # List of integers
# # my_list = [1, 2, 3, 4]
# # print(my_list)

# # # Mixed data types
# # my_list = ['A string', 23, 100.232, 'o', True]
# # print(my_list)

# # # Modifying a list element
# # my_list = [1, 2, 3, 4, 5]
# # my_list[0] = 10
# # print(my_list)

# # # Calculating mean marks
# # marks = [87, 76, 95, 68, 80, 83, 92, 74, 79, 89]
# # mean_marks = sum(marks) / len(marks)
# # print(mean_marks)

# # Create dictionary
# marvel_dict = {
#     'Name': 'Thor',
#     'Place': 'Asgard',
#     'Weapon': 'Hammer',
#     1: 2,
#     3: 'power',
#     'alibies': ['Ironman', 'Captain America'],
#     'abc': {1: 2, 4: 5}
# }

# print(marvel_dict['Place'])  # Output: Asgard
# print(marvel_dict['alibies'])  # Output: ['Ironman', 'Captain America']

# # Dictionary methods
# print(list(marvel_dict.keys()))
# print(list(marvel_dict.values()))
# print(marvel_dict.items())

# # Nested dictionary access
# print(marvel_dict['abc'][1])  # Output: 2

# # Dictionary mutation
# customer = {
#     "id": 1234,
#     "name": "John Smith",
#     "email": "john@example.com"
# }
# customer["email"] = "john.smith@example.com"
# customer["phone"] = "555-555-1212"
# del customer["id"]
# print(customer)

# name = input("Enter your name: ")
# print("Hello, " + name + "!")


# nums=[3,6,9,10,12,13,4,5,7,99,1]
# large=nums[0]

# for n in nums:
#     if(n>large):
#         large=n

# print("largest number is:",large)

# nums=[1,2,3,4,5,9,12,13,15]
# target=14
# for i in range(len(nums)):
#     if(nums[i]+nums[i+1]==target):
#         print("target found at index:",i,i+1)
        break