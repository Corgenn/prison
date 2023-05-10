prisoners = [
    {"name" : "Boris", "Age" : 19, "level_d" : 2, "freed" : False},
    {"name" : "Kiril", "Age" : 29, "level_d" : 3, "freed" : False},
    {"name" : "Oleg", "Age" : 54, "level_d" : 4, "freed" : True},
    {"name" : "Nasta", "Age" : 72, "level_d" : 1, "freed" : False},
    {"name" : "Sera", "Age" : 34, "level_d" : 3, "freed" : True},
];
try:
    num_function = int(input("print a 1 to sorted by age, 2 to sorted by name, 3 to sorted by level_danger"));
    if 3 > num_function < 0:
        raise ValueError()
except ValueError: 
    print ("You dont print a 1, 2 or 3!");

def sort_by_age (prisoners):
    def get_Age (prisoner):
        return (prisoner["Age"])
    prisoners.sort (key=get_Age)  
    print (prisoners)

match num_function:
    case 1:
            sort_by_age (prisoners)
    case 2:
            print ()
    case 3:
            print ()