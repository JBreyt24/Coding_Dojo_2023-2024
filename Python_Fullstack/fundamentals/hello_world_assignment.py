# # 1. TASK: print "Hello World"
print("Hello World")
# # 2. print "Hello Noelle!" with the name in a variable
name = "Josh"
print("Hello","Josh")	# with a comma
print("Hello" + "Josh")	# with a +
# # 3. print "Hello 42!" with the number in a variable
name = 72
print("Hello", name )	# with a comma
print("Hello" + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "pasta"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

# Bonus
guitar_brands = ["ibanez, solar, esp, schector"]
guitar_brands.append("mayones")
print(guitar_brands)