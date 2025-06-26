import random
def title(a):
    print(45*'#'+a+45*'#'+'\n')
def ex_print(ex_num):
    print(f'\n{107*'-'}\n'
          f'{50*" "}-EX {ex_num}-{50*" "}\n')
title(' Bars_Final_Work ')
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 1-
#Write a for loop that prints the numbers from 12 to 24.
def ex_1_main():
    ex_print(1)
    for num in list(range(12, 25, )):
        print(num, end=",")
    print('\n')
#ex_1_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 2-
#Write a for loop that prints the ODD numbers from 7 to 31.
def ex_2_main():
    ex_print(2)
    for num in list(range(7, 32, )):
        if not num % 2 == 0:
            print(num, end=",")
    print('\n')
#ex_2_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 3-
#Write a for loop that prints the EVEN numbers from 10 to -20.
def ex_3_main():
    ex_print(3)
    for num in list(range(10, -21, -1)):
        if num % 2 == 0:
            print(num, end=",")
    print('\n')
#ex_3_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 4-
#Write a for loop that iterates through all numbers from 1 to 45. Print the following:
#For each number that multiples of 3 print “Fizz”
#For each number that multiples of 5 print “Buzz”
#For each number that multiples of 3 and 5 print “FizzBuzz”
def ex_4_main():
    ex_print(4)
    num_list=[]
    for num in list(range(1, 46), ):
        if num % 3 == 0:
            if num % 5 == 0:
                num_list.append("fizzbuzz")
            else:
                num_list.append("fizz")
        elif num % 5 == 0:
            num_list.append("buzz")
        else:
            num_list.append(num)
    index=0
    while index != len(num_list):
        if index%11==0 and not index==0:
            print(num_list[index], end="\n")
        else:
            print(num_list[index], end=",")
        index += 1
    print('\n')
#ex_4_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 5-
#Write a function that receives an array as a parameter and calculates the sum
#of all the numbers in the given array (don’t use sum() function).
#For example if the given array is: [1,13,22,123,49,34,5,24,57,45]
#The result should be 373
def ex_5_main():
    ex_print(5)
    given_array=[1,13,22,123,49,34,5,24,57,45]
    print(f'my given array :\n{given_array}')
    def array_sumer(array):
        array_sum=0
        for num in array:
            array_sum+=num
        return array_sum
    given_array_sum=array_sumer(given_array)
    print(f'my given array "sumed":\n{given_array_sum}')
#ex_5_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 6-
#Write a function that receives an array of objects.
#Each object should represent a student with the properties:
# #id,first name,last name,age,country,city#

#In addition, the function should receive a property to change.

#1 - The function should check for each property in each object in the array if
#    the given property exists and if it does, the function should delete it from the object.
#2 - Write a function that prints each property of each object in the given array.
#3 - Write a function that sorts the array by the students age from the oldest to
#    the youngest and return the sorted array.
def ex_6_main():
    ex_print(6)
    students = [
        {
            'id': 101,
            'first_name': 'Emma',
            'last_name': 'Wilson',
            'age': 22,
            'country': 'USA',
            'city': None,
            'is_payment_received': None
        },
        {
            'id': 102,
            'first_name': 'Liam',
            'last_name': 'Smith',
            'age': 24,
            'country': 'Canada',
            'city': 'Toronto',
            'is_payment_received': None
        },
        {
            'id': 103,
            'first_name': 'Sophia',
            'last_name': 'Brown',
            'age': 21,
            'country': 'UK',
            'city': 'London',
            'is_payment_received': None
        },
        {
            'id': 104,
            'first_name': 'Noah',
            'last_name': 'Miller',
            'age': 23,
            'country': 'Germany',
            'city': 'Berlin',
            'is_payment_received': None
        }
    ]
    def change_check_delete(arr):
        print("\nchange check delete func: \n")
        properties=[]
        def change():
            for student in arr:
                import random
                student['is_payment_received'] = random.choice([True, False])
                for property in student:
                    while len(properties) != len(student.keys()):
                        properties.append(property)
                        break
            return arr
        def check_print(arr):
            for property in properties:
                print("\n", property, ":")
                for student in students:
                    if property in student:
                        if student[property] != None:
                            print(f"{student['first_name']} {student['last_name']} : {student[property]} : check")
                        else:
                            print(f"{student['first_name']} {student['last_name']} : missing!")
        def delete_property(arr):
            for property in properties:
                for student in students:
                    if property in student:
                        if student[property] != None:
                            student[property]=""
        arr = change()
        check_print(arr)
        delete_property(arr)
    def print_prop(arr):
        print("\nprint prop func:\n")
        for student in arr:
            for property in student:
                print(f'{property} : {student[property]}')
            print("\n")
    def sort_age(arr):
        print(f'sorting by age\n')
        ages = []
        sorted_students = []
        for student in arr:
            try:
                ages.append(student['age'])
            except KeyError:
                print('value not fount')
        ages.sort()
        ages.reverse()
        for item in ages:
            for student in arr:
                if student['age'] == item:
                    sorted_students.append(student)
                elif student['age'] == None:
                    print('property not found')
        arr.clear()
        arr.extend(sorted_students)
        return arr
    print_prop(students)
    sort_age(students)
    print_prop(students)
    change_check_delete(students)
    print_prop(students)
#ex_6_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 7-
#1 - Write a function that receives the array shown above and prints only animalType: cat.
#2 - Write a function that receives the array shown above and the animal type.
#    The function should print all names of that animal type if this type exists in the object.
#3 - Write a function that that receives the array shown above and animal name The function should add
#     the specified animal name to each ‘names’ array in each animal_type if that name
#     does not exist in the ‘names’ array.
#check if input is in each type
#if name not in certain type add it
def ex_7_main():
    ex_print(7)
    our_pets = [
        {"animal_type": "cat",
         "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
        {"animal_type": "dog",
         "names": ["Spot", "Bowser", "Frankie"]}
    ]
    def print_cat_type(our_pets):
        print("print cat type func ")
        cat_dict = our_pets[0]
        print(cat_dict, '\n')
    def print_animal_type(our_pets):
        print("print animal type func")
        while True:
            animal_type = input("enter an animal type:\n")
            type_bool = ""
            i = 0
            if animal_type.isalpha():
                for pet in our_pets:
                    if animal_type.lower() == pet['animal_type']:
                        type_bool = 1
                        print(f'the possible names for {animal_type} are :'
                              f'{pet["names"]}')
                        break
                    else:
                        print(f"animal type {animal_type} is not in our_pets {i}")
                        i += 1
            else:
                print("invalid input")
            if type_bool == 1:
                break

        # input type
        # check type
        # print names of type
    def add_name(our_pets):
        print("add name func ")
        while True:
            name_input = input("enter a pet name:\n")
            if name_input.isalpha():
                pet_name = name_input
                break
            else:
                print("invalid input")
        for num in [0, 1]:
            type = our_pets[num]
            names_lower = []
            for name in type['names']:
                names_lower.append(name.lower())
            if pet_name not in names_lower:
                type['names'].append(pet_name.capitalize())
            else:
                print(f'the name "{pet_name}" already exists in {our_pets[num]['animal_type']} type names')
            print(f'{our_pets[num]['animal_type']} names:{type['names']}')
    print_cat_type(our_pets)#1
    add_name(our_pets)#3
    print_animal_type(our_pets)#2
#ex_7_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 8-
#1 - Write a function that prints all the student data
#    (each student property should be printed in a new line).
#2 - Write a function that receives the student object and a hobby,
#    the function should add the hobby to the student's hobbies array if it’s not exist already.
#3 - Use the function that you wrote in ex 1 to print the data of the student and
#    check that the new hobby has been added.
#4 - Write a function that receives an object of a student and hobby, the function should
#    delete the hobby from the student's hobbies.
#5 - Use the function that you wrote in ex 1 to print the data student and check that the hobby has
#    been deleted from the object student.
#6 - Add to the object student new property: family_name and add a value.
def ex_8_main():
    ex_print(8)
    student = {
        'name': 'John',
        'age': 20,
        'hobbies': ['reading', 'games', 'coding'],
    }
    def print_all_student_data(       student):
        student_keys=[]
        print("\nprint all student data func:")
        for key in student:
            student_keys.append(key)
        for key in student_keys:
            print(f'{key}:{student[key]}')



        #for property in student loop
        #print
    def add_hobby(student_hobbies):
        print("\nadd hobby func:")
        while True:
            new_hobby=input("input new hobby name:\n")
            if new_hobby.isalpha():
                if not new_hobby.lower() in student_hobbies:
                    student_hobbies.append(new_hobby.lower())
                    print(f'{new_hobby.lower()} been added to student hobby list')
                    break
                else:
                    print("hobby is already in student hobby list")
            else:
                print("invalid input")
        print_all_student_data(student)
    def delete_hobby(student_hobbies):
        print("\ndelete hobby func:")
        while True:
            hobby_delete=input(f'chose a hobby delete :\n{student_hobbies}\n')
            if hobby_delete.isalpha():
                if hobby_delete.lower() in student_hobbies:
                    student_hobbies.remove(hobby_delete)
                    break
                else:
                    print("hobby dont exist")
            else:
                print("invalid input")
        print_all_student_data(student)
    def add_family_name(student):
        student["family_name"]="Wilson"
        print_all_student_data(student)
    print_all_student_data(student)
    add_hobby(student["hobbies"])
    delete_hobby(student["hobbies"])
    add_family_name(student)
#ex_8_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                  -EX 9-
#Write a function that prints all the elements of a 2D array using nested for loops.
#print_matrix(matrix) → Should print: 1 2 3 4 5 6
def ex_9_main():
    ex_print(9)
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]]
    for row in matrix:
        for num in row:
            print(num,end=" ")
#ex_9_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 10-
#Write a function to count how many numbers of zeros appear in a 2D
#matrix using nested for loops and increment operation.
#print(zero_count(matrix)) → Should print: 5
def ex_10_main():
    ex_print(10)
    matrix = [
        [0, 1, 1],
        [0, 1, 0],
        [1, 0, 0]]
    def zero_counter(matrix):
        print("\nzero counter func")
        zero_count=0
        for row in matrix:
            for num in row:
                if num == 0:
                    zero_count+=1
        print(zero_count)
    zero_counter(matrix)
#ex_10_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 11-
#Write a function to return an array of all the elements that are repeated more than once in a given array.
#print(find_dup(arr)) Should print: [4, 1]
def ex_11_main():
    ex_print(1)
    arr = [4, 2, 34, 4, 1, 12, 1, 4]
    def find_dup(arr):
        print("\nfind dup func")
        arr_counter=[]
        dup_list=[]
        for num in arr:
            if num in arr_counter:
                if not num in dup_list:
                    dup_list.append(num)
            arr_counter.append(num)
        return dup_list
    print(find_dup(arr))
#ex_11_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 12-
#Write a function using a for loop that gets an array and returns a new array with the
# elements from the given array appearing in reverse order. (Don’t use array reverse() method)
#For example:
#arr = [43, "what", 9, true, "cannot", false, "be", 3, true];
#Function output should be:
#[true, 3, “be”, false, “cannot”, true, 9, “what”, 43]
def ex_12_main():
    ex_print(12)
    arr = [43, "what", 9, True, "cannot", False, "be", 3, True]

    def reverse_order(arr):
        print("\nreverse order func")
        reverse_arr=[]
        for i in range(len(arr)):
            reverse_arr.insert(0,arr[i])
        print(reverse_arr)
        return reverse_arr
    reverse_order(arr)
#ex_12_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 13-
#Given two arrays of integers. Add up each element in the same position and
# create a new array containing the sum of each pair.
# Assume both arrays are of the same length.
# For example:
# first_array = [4, 6, 7];
# second_array = [8, 1, 9];
# Function output should be:
# [12, 7, 16]
def ex_13_main():
    ex_print(13)
    first_array = [4, 6, 7]
    second_array = [8, 1, 9]
    print("\nex13 solution :")
    sum_array=[]
    for i in range(len(first_array)):
        sum_array.append(first_array[i]+second_array[i])
    print(sum_array)
#ex_13_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 14-
#Write a program that will check if two strings are palindromes. A palindrome
# is a word that spells the same forward and backward. Palindrome: a word,
# phrase, or sequence that reads the same backward as forward, examples
# for valid palindromes: madam, nurses run.
#For example:
#first_str = "racecar"
#second_str = "Java"
#Function output should be:
#True (for first_str)
#False (for second_str)
def ex_14_main():
    ex_print(14)
    first_str = "racecar"
    second_str = "Java"
    possible_palindromes = []
    possible_palindromes.append(first_str), possible_palindromes.append(second_str)
    def is_palindrome(str_list):
        print("\nis palindrome func:")
        for str in possible_palindromes:
            reverse_str = ""
            for char in str:
                reverse_str = char + reverse_str
            if reverse_str == str:
                print(f'{str} is a palindrome')
            else:
                print(f''
                      f'{str} is not a palindrome')
    is_palindrome(possible_palindromes)
#ex_14_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 15-
#Write a while loop that iterates as long as the counter is less than 100,
# on every iteration the counter is multiplied by 2 starting from 1.
def ex_15_main():
    ex_print(15)
    counter=1
    i=0
    print(f'\niteration:{i},counter:{counter}')
    i+=1
    while counter*2<100:
        counter *= 2
        print(f'iteration:{i},counter:{counter}')
        i += 1
#ex_15_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 16-
#Write a while loop that iterates as long as the counter is greater than 50 ,
#on every iteration the counter is divided by 2.
#The counter should start with the value 900000 before the first iteration.
def ex_16_main():
    ex_print(16)
    i=0
    counter=900000
    print(f'\niteration:{i},counter:{counter}')
    while counter/2>50:
        counter //= 2
        i += 1
        print(f'iteration:{i},counter:{counter}')
#ex_16_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 17-
#Write a function that gets an array of strings as parameter and returns a new
#array containing all the values that appear more than once.
#In your solution use only while loops.
def ex_17_main():
    ex_print(17)
    names = [
        "Emma", "Liam", "Olivia", "Noah", "Emma", "Ava", "Liam", "Mia",
        "Ethan", "Ava", "Sophia", "Jackson", "Isabella", "Lucas", "Mason", "Aria",
        "Oliver", "Charlotte", "James", "Amelia", "Benjamin", "Harper", "Elijah", "Evelyn",
        "William", "Abigail", "Emma", "Logan", "Aiden", "Ella", "Liam", "Scarlett",
        "Henry", "Grace", "Lucas", "Chloe", "Jack", "Zoe", "Michael", "Layla",
        "Alexander", "Riley", "Sebastian", "Lily", "Mateo", "Hannah", "Daniel", "Nora",
        "Matthew", "Lillian", "Joseph", "Addison", "Samuel", "Avery", "David", "Aubrey",
        "Carter", "Ella", "Jayden", "Natalie", "Owen", "Sofia", "Wyatt", "Brooklyn"
    ]
    def find_dup(arr):
        print("\nfind dup func:")
        index = 0
        dup_list = []
        while index != len(arr):
            momentary_dup_list = []
            search_index = 0
            name = arr[index]
            while search_index != len(arr):
                possible_dup = arr[search_index]
                while name == possible_dup:
                    momentary_dup_list.append(possible_dup)
                    break
                search_index += 1
            while len(momentary_dup_list) > 1:
                while not momentary_dup_list[0] in dup_list:
                    dup_list.append(momentary_dup_list[0])
                    break
                break
            index += 1
        return dup_list
    dup_list=find_dup(names)
    print(dup_list)
#ex_17_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 18-
#Write a function that gets an array of strings as parameter and returns a new
#array containing all the values from the provided array in the same order but
#without any duplicated values. In your solution use only while loops.

#For example:
#names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]
#Function output should be:
#['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor']
def ex_18_main():
    ex_print(18)
    fruits = ['Apple', 'Banana', 'Mango', 'Peach', 'Grape',
        'Banana', 'Pineapple', 'Mango', 'Kiwi', 'Apple',
        'Strawberry', 'Peach', 'Watermelon', 'Kiwi', 'Papaya']
    def dup_remover(str_list):
        print("\ndup remover func:")
        fruits_sorted=[]
        index=0
        while index!=len(str_list):
            index_str=str_list[index]
            while not index_str in fruits_sorted:
                fruits_sorted.append(index_str)
                break
            index+=1
        print(fruits_sorted)
    dup_remover(fruits)
#ex_18_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 19-
#Write a function that gets an array of strings as parameter and returns a new
#array containing all the values from the provided array in the same order but
# without any duplicated values.
#If the string ‘pete’ is a value inside the array your function should skip it
#and not copy it to the new array. In your solution use only while loops.

#For example:
#names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', ‘Chris’, ‘Kevin’]

#Function output should be:
#*['Chris', 'Kevin', 'Naveed', 'Victor']
def ex_19_main():
    ex_print(19)
    names = ['Chris', 'Kevin', 'Naveed', 'Pete','Victor', 'Chris','Kevin']
    def sort_str_no_petes(names):
        print("\n\nsort list no petes func:")
        sorted_list=[]
        index=0
        while index!=len(names):
            name=names[index]
            while name == 'Pete':
                index +=1
                break
            else:
                while not name in sorted_list:
                    sorted_list.append(name)
                    break
                index+=1
        return sorted_list
    new_names=sort_str_no_petes(names)
    print(new_names)
#ex_19_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 20-
#Use a while loop to iterate on a boolean array.
#As long as the next index is different from the previous index the iteration
#continues, otherwise, return the index of the element with the same
#value. If there are not two successive values, the function will return -1.

#For example:
#array= [true, false, false, true, true, false] → return 2
#array= [true, false, true, false, true, true]; → returns 5
#array= [true, false, true, false, true, false]; → returns -1
def ex_20_main():
    ex_print(20)
    array1=[True,False,False,True,True,False]
    array2=[True,False,True,False,True,True]
    array3=[True,False,True,False,True,False]
    def bool_iteration(bool_list):
        print("\nbool iteration func:")
        index=0
        while index != len(bool_list):
            search_index = index
            pair_check = []
            while search_index < index + 2 and search_index != len(bool_list):
                pair_check.append(bool_list[search_index])
                search_index += 1
            if 1 < len(pair_check):
                check1 = pair_check[0]
                check2 = pair_check[1]
            if check1==check2:
                return_index = index + 1
                return return_index
            index += 1
        return_index=-1
        return return_index
    print(f'array1 :{bool_iteration(array1)}\n')
    print(f'array2 :{bool_iteration(array2)}\n')
    print(f'array3 :{bool_iteration(array3)}\n')
#ex_20_main()
#-----------------------------------------------------------------------------------------------------------------------
#                                                 -EX 21-
#Write a python program that gets user input (use input() function for this).
#The first input will be the user full name
#Second input will be the user age
#Third input will be the user email
#Write validation for each input provided by the user and allow the user to try
#again in case the user provided invalid input.

#Validation for full name input → string type with 2 words for first name and last name.
#Validation for age input → int type between 1 - 130.
#Validation for email input → string type with ‘@’ inside.
def ex_21_main():
    ex_print(21)
    def user_data_input():
        print("\nUser data input func:")
        def user_full_name_input():
            while True:
                input_full_name=input("Enter your full name ('first' 'last'):\n")
                list_name=input_full_name.rsplit(" ")
                if len(list_name)==2 and list_name[0].isalpha() and list_name[1].isalpha():
                    full_name=list_name[0].capitalize()+" "+list_name[1].capitalize()
                    return full_name
                else:
                    print("invalid input")
        def user_age_input():
            while True:
                input_age = input("Enter your age:\n")
                if input_age.isdigit():
                    age=int(input_age)
                    if 1<age<130:
                        return age
                    else:
                        print("Age must be between 1-130")
                else:
                    print("Invalid Input")
        def user_email_input():
            while True:
                stl_list= [".com", ".org", ".net", ".info", ".biz",
                                ".us", ".ca", ".de", ".fr", ".uk", ".au",
                                ".app", ".shop", ".guru", ".online", ".tech",
                                ".xyz", ".blog",".il"]
                user_email_input=input("Enter your Email (###@###.###):\n")
                if user_email_input.count("@")==1 :
                    for stl in stl_list:
                        if user_email_input.endswith(stl):
                            return user_email_input
                    print(f"Must end with a legit stl like:\n{stl_list}")
                else:
                    print(f"Must contain '@'")
        user_full_name=user_full_name_input()
        user_age = user_age_input()
        user_email=user_email_input()
        def print_user_data(name,age,email):
            print(f'\n\nuser_full_name: {user_full_name}\n'
                  f'user_age: {user_age}\n'
                  f'user_email: {user_email}')
        print_user_data(user_full_name,user_age,user_email)
    user_data_input()
#ex_21_main()
