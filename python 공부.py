def calculate_weight(height, gender):
    if gender == "male":
        male = True
    elif gender == "female":
        male = False
    else:
        print("do it again.")

    if male:
        weight = height * height * 22
        weight = round(weight, 2)
        print("average weight of men whose height is " + str(height) + "m is " + str(weight) + "kg.")
    else:
        weight = height * height * 21
        weight = round(weight, 2)
        print("average weight of women whose height is " +str(height) + "m is " + str(weight) + "kg.")

calculate_weight(1.75, "male")
calculate_weight(1.65, "female")