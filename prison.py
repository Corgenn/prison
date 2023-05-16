prisoners = [
    {"name" : "Boris", "Age" : 19, "level_d" : 2, "freed" : False},
    {"name" : "Kiril", "Age" : 29, "level_d" : 3, "freed" : False},
    {"name" : "Oleg", "Age" : 54, "level_d" : 4, "freed" : True},
    {"name" : "Nasta", "Age" : 72, "level_d" : 1, "freed" : False},
    {"name" : "Sera", "Age" : 34, "level_d" : 3, "freed" : True},
];
try:
    num_function = int(input("print a 1 to sorted by age, 2 to sorted by freed, 3 to sorted by level_danger"));
    if 3 > num_function < 0:
        raise ValueError()
except ValueError: 
    print ("You dont print a 1, 2 or 3!");

def sort_by_age (prisoners):
    def get_Age (prisoner):
        return (prisoner["Age"])
    prisoners.sort (key=get_Age)
    for p in prisoners:
        print (p);

def sort_by_freed (prisoners):
    for p in prisoners:
        if p["freed"] == False:
            print (p["name"], "Not escaped");
        else:
            print (p["name"], "Escaped");

def sort_by_danger (prisoners):
    def get_danger (prisoner):
        return (prisoner["level_d"])
    prisoners.sort (key=get_danger)
    for p in prisoners:
        print (p);

match num_function:
    case 1:
            sort_by_age (prisoners);
    case 2:
            sort_by_freed (prisoners);
    case 3:
            sort_by_danger (prisoners);
