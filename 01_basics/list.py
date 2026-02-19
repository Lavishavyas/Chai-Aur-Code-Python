tea_varities = ["Black", "Green", "Oolong", "White"]
# print(tea_varities)
# print(tea_varities[0])
# print(tea_varities[1])
# print(tea_varities[-1])
# print(tea_varities[1:3])
# print(tea_varities[:2])
# print(tea_varities[2:])
# tea_varities[3] = "Herbal"
# print(tea_varities) 

# tea_varities[1:2] = ["Lemon"]

# for tea in tea_varities:
    # print(tea, end = "-")
    
# if "Oolong" in tea_varities:
#     print("I have Oolong tea")    
    
# tea_varities.append("Oolong")
# print(tea_varities)    

# tea_varities.pop()
tea_varities.remove("Green")
print(tea_varities)
tea_varities.insert(1, "Green")
print(tea_varities)

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)
tea_varities_copy.append("Lemon")
print(tea_varities_copy)
print(tea_varities)

suared_number = [x**2 for x in range(10)]
print(suared_number) 
cube_num = [x**3 for x in range(5)]
print(cube_num)