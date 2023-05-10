prisoner = [
    {"name" : "Boris", "Age" : 19, "level_d" : 2, "freed" : False},
    {"name" : "Kiril", "Age" : 29, "level_d" : 3, "freed" : False},
    {"name" : "Oleg", "Age" : 54, "level_d" : 4, "freed" : True},
    {"name" : "Nasta", "Age" : 72, "level_d" : 1, "freed" : False},
    {"name" : "Sera", "Age" : 34, "level_d" : 3, "freed" : True},
];

try:
    num_function = int(input("print a 1 to sorted for age, 2 to sorted for name, 3 to sorted for level_danger"))
    if 3 > num_function < 0:
        raise ValueError()
except ValueError:
    print ("You dont print a 1, 2 or 3!");

match num_function:
    case "1":
            print (prisoner)
    case "2":
            print ("asd")
    case "3":
            print ()