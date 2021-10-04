new_black = 10
# print(new_black)
# print(type(new_black))

# float_me = 0.5
# print(float_me)
# print(type(float_me))


stringify = "We had a downpour in Lagos 2 days ago!"
# print(stringify)
# print(type(stringify))

my_verdict = True
# print(my_verdict)
# print(type(my_verdict))

random_stuff = ['music', "sports", True, 99.9]
# print(random_stuff)
# print(type(random_stuff))

new_guy = ("45", False, 101)
# print(new_guy)
# print(type(new_guy))

sports = {"football", "cricket", "basketball", "cricket"}
# print(sports)
# print(type(sports))


my_info = {
    "name" : "Adamu",
    "gender" : "Male",
    "age" : 12
}

# print(my_info)
# print(type(my_info))




###ARITHMETIC OPERATIONS
my_mod = 33 % 4
# print(my_mod)


my_quote = 33 // 4
# print(my_quote)

r_power = 5 ** 4
# print(r_power)


####COMAPRISON OPERATORS
first_num = 67
second_num = 40

# quick_check = first_num != second_num
# print(quick_check)

# feedback = ((first_num % 2 != 0) or (second_num > first_num)) and not((second_num == 40) or (second_num // 2 != 0))
# print(feedback)

career = "She is a model who lives in California"
# output = "She I" in career

# scores = [62, 55, 72, 89]
# check = 62 in scores

# print(check)


###CONTATENATION
# first_phrase = "Hello"
# second_phrase = "there, welcome!"

# full_sent = first_phrase + " " + second_phrase
# print(full_sent)


career = "She is a model who lives in California!"
desired_char = career[-1]
desired_portion = career[ : 10]
# print(desired_portion)


# age_limit = 10
# report_template = "You can't gain access unitl your are {} years old.".format(age_limit)

# report_template = f"You can't gain access unitl your are {age_limit} years old."

# print(report_template)


##ESCAPE CHARACTER
source_of_income = 'The nation\'s crude oil'
# print(source_of_income)

refined_career = career.title()

quick_search = career.startswith("She is")

# another_search = career.index("nigeria")
# print(another_search)

# print(refined_career)

career = "!She is a model who lives in California!"
trans_list = career.split("!")
# print(trans_list)

new_career = career.replace("California", "Texas")
# print(new_career)

trimmed = career.lstrip("!")
# print(trimmed)


####LIST
random_stuff = ["pawn", "phone", "pen", "ball", False, 99.69, "pawn", 2021, 4+2j, "water"]
# print(random_stuff)

desired_item = random_stuff[-1]
# print(desired_item)

desired_items = random_stuff[ : : 3]
# print(desired_items)

random_stuff[1] = "water"

random_stuff[3 : 6 : 2] = ["chair", True]


# print(random_stuff)

no_of_occurence = random_stuff.count("water")
# print(no_of_occurence)

# print(random_stuff.index("pawn"))

random_stuff.remove("water")

random_stuff.append("Checkmate")

# print(random_stuff)

backup_list = random_stuff.copy()
# print(backup_list)

random_stuff.insert(0, "awesome")
# print(random_stuff)

scores = [31, 19, 20, 56, 45]
# print(scores)
# print("\n")
scores.sort(reverse = True)
# print(scores)


# print(random_stuff)
# print("\n")
# random_stuff.reverse()
# print(random_stuff)

quick_one = ("Brilliant", "Shy", "Great")
# print(quick_one[1:])

# quick_one[1] = "Bold"
# print(quick_one)





####SETS
grocery_cart1 = {"Bread", "Oranges", "Jam", "Fruit Juice", "Eggs", "Butter", "Cookies"}
grocery_cart2 = {"Eggs", "Yam", "Grapes", "Cookies", "Apple", "Carrot", "Bread", "Ice Cream"}

# print(grocery_cart1)
# print(grocery_cart2)

grocery_cart2.discard("Yam")
grocery_cart2.add("Youghurt")
# print(grocery_cart2)

merged_carts = grocery_cart1.union(grocery_cart2)
# print(merged_carts)

# grocery_cart1.update(grocery_cart2)
# print(grocery_cart1)

backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()

cart1_only = grocery_cart1.difference(grocery_cart2)
# print(cart1_only)

# grocery_cart2.difference_update(grocery_cart1)
# print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
# print(common_groceries)

backup_cart1.intersection_update(backup_cart2)
# print(backup_cart1)

taking_out_duplicates = grocery_cart1.symmetric_difference(grocery_cart2)
# print(taking_out_duplicates)
 

#####DICTIONARIES!!!
customer_info = {
    "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
    "gender" : ["Male", "Male", "Male", "Female"],
    "age" : [22, 29, 34, 18],
    "nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
}

# print(customer_info)

all_names = customer_info["name"]
# print(all_names)

all_nationalities = customer_info.get("nationality")
# print(all_nationalities)

all_keys = customer_info.keys()
# print(all_keys)

all_values = customer_info.values()
# print(all_values)

all_items = customer_info.items()
# print(all_items)

customer_info.update({"occupation" : ["Actor", "Banker", "Footballer", "Experience Engineer"]})

customer_info.pop("age")

customer_info.clear()
# print(customer_info)



####BUILTIN FUNCTIONS
# # get_data = input("Enter integers here: ")
# #to have access to the integers
# con_list = get_data.split(" ")
# #to convert/change the entries to proper integers
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])
# con_list[2] = int(con_list[2])
# con_list[3] = int(con_list[3])
# con_list[4] = int(con_list[4])


# # smallest_integer = min(con_list)
# # print(smallest_integer)
# new_list = list(set(con_list))
# new_list.sort()

# output = new_list[-2]

# print(output)

first_list = ["high", "low", "middle", "high-lows", "dark space"]
second_list = [1, 2, 3]

zipped_object = zip(first_list, second_list)
# print(list(zipped_object))


modifier = lambda a : a.startswith("oic")
output = modifier("voice")
# print(output)


scores = [68, 72, 83, 91]
upgraded_scores = map(lambda a : a + 2, scores)
output = list(upgraded_scores)
# print(output)

num = [20, 31, 45, 60,  10, 77]
my_sieve = filter(lambda a : a % 2, num)
output = list(my_sieve) 
# print(output)

rand_words = ["Emmanuel", "Pizza", "Coerce", "Smooth", "Laptop", "Screen"]
retain_e = filter(lambda a : "e" in a, rand_words)
output = list(retain_e)
# print(output)


my_sequence = range(10, 25)
# print(list(my_sequence))



#####BUILTIN MODULES
# import time
# print("This is line 302")
# time.sleep(12)
# print("This is line 304")


import random as rd
rd.seed(99)
rand_words = ["Emmanuel", "Pizza", "Coerce", "Smooth", "Laptop", "Screen"]
# rd.shuffle(rand_words)

random_pick = rd.choice(rand_words)
# print(random_pick)

selected_items = rd.sample(rand_words, 6)
# print(selected_items)

feedback = rd.randrange(14, 44, 2)
# print(feedback)


####DATETIME
from datetime import datetime as dt
current_date_and_time = dt.now()
# print(current_date_and_time)


current_year = dt.now().year
# print(current_year)

output = current_date_and_time.strftime("%B%m")
# print(output)

ch_day = "25/12/2021"
converted_date = dt.strptime(ch_day, "%d/%m/%Y")
# print(converted_date.date())

notable_days = ["15/1/2021", "14/2/2021", "1/4/2021", "29/5/2021", "12/6/2021", "1/10/2021", "25/12/2021"]


#####CONDITIONALS
# if 5 > 8 or dt.now().minute % 2 == 0:
#     print("Hell yeah")
# else:
#     pass


# if "z" in "Emmanuel":
#     print("Spelt correctly")
# elif 59 > 58.9:
#     print("Mathematically correct")
# else:
    # pass

# get_data = input("Enter data here: ")
# # print(get_data)


# if len(set(get_data)) != len(get_data):
#     print("Duplicates are present")
# else:
#     print("There are no duplicates")


# cracker = 1
# while (cracker < 5):
#     if cracker == 3:
#         print("Here is my ride outta the loop!")
#         break
#     else:
#         print("I'm in the loop")
#         cracker += 1


####GUESS GAME!!!!
# import random as rd
# get_data = input("Enter two integers here: ")
# con_list = get_data.split(" ")
# #converting to integers
# con_list[0] =  int(con_list[0])
# con_list[1] = int(con_list[1])

# #randomly selecting an integer within the given range
# random_integer = rd.randrange(con_list[0], con_list[1])

# #time to guess
# while True:
#     user_guess = input("Enter your guess here: ")
#     if random_integer == int(user_guess):
#         print("You guessed right!")
#         break
#     elif int(user_guess) < random_integer:
#         print("Guess too low... try again")
#     elif int(user_guess) > random_integer:
#         print("Guess too high... try again")
#     else:
#         pass

####FOR LOOP
# new_word = "Universe"
# for letter in new_word:
#     print("Home for all!")

# new_list = ["pop", "rock", "country"]
# for item in new_list:
#     print(item)


# scores = [68, 90, 78, 71, 83]
# for num in scores:
#     if num % 2 == 0:
#         print(f"{num} is an even number")
#     elif num % 2 != 0:
#         print("{} is an odd number".format(num))
#     else:
#         pass



# customer_info = {
#     "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
#     "gender" : ["Male", "Male", "Male", "Female"],
#     "age" : [22, 29, 34, 18],
#     "nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
# }

# for entry in customer_info.items():
#     print(entry[1][0])
#     print("\n")


continents = ["Africa", "Asia", "North America", "South America", "Europe", "Antartica", "Australia"]
countries = ["Morocco", "China", "USA", "Argentina", "Croatia", "Eskimo", "New Zealand"]

zipped_object = zip(countries, continents)

# for entry in zipped_object:
#     print(entry)

# print("\n")

# for country_name, continent_name in zipped_object:
#     print(country_name)


####10 percent increment
# get_data = input("Enter integers here: ")
# con_list = get_data.split(" ")
# #converting to integers
# for num in range(len(con_list)):
#     con_list[num] = int(con_list[num])

# for x in range(len(con_list)):
#     con_list[x] *= 1.1
    # con_list[x] = round(con_list[x], 2)

# print(con_list)


# get_data = input("Enter integers here: ")
# con_list = get_data.split(" ")
# #converting to integers
# new_list = map(lambda a : int(a), con_list)
# #to increment
# output = list(map(lambda a : round(a * 1.1, 2), new_list))
# print(output)



####2-LEVEL NESTED LOOP
# starters = ["It's", "They are", "They all are"]
# nouns = ["car", "country", "Lady"]
# adjectives = ["fast", "beautiful", "awesome"]

# for  beginner in starters:
#     for qualifier in adjectives:
#         for word in nouns:
#             print(beginner, qualifier, word)

#         print("\n")

scores = [60, 62, 77, 64, 66, 57, 91]
upgraded_scores = [num + 3 for num in scores]

# print(upgraded_scores)

# weird_structure = [print(num + 3) for num in scores]

new_upgrade = [num + 3 for num in scores if num % 2 == 0]
# print(new_upgrade)

new_list = [("Awesome", 12), ("Zebra", 2), ("Dawn", 9), ("New", 4)]
sorted_list = sorted(new_list, key = lambda a : a[1], reverse = True)
print(sorted_list)
