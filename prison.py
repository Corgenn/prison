prisoners = [
    {"name" : "Boris", "Age" : 19, "level_d" : 2, "freed" : False},
    {"name" : "Kiril", "Age" : 29, "level_d" : 3, "freed" : False},
    {"name" : "Oleg", "Age" : 54, "level_d" : 4, "freed" : True},
    {"name" : "Nasta", "Age" : 72, "level_d" : 1, "freed" : False},
    {"name" : "Sera", "Age" : 34, "level_d" : 3, "freed" : True},
];



def sort_by_age(prisoners):
    prisoners.sort(key=lambda prisoner: prisoner["Age"]);
    for p in prisoners:
        print(p["name"],"Age",p["Age"]);

def sort_by_freed (prisoners):
    prisoners.sort(key=lambda prisoner: prisoner["freed"]);
    for p in prisoners:
        if p["freed"] == False:
            print (p["name"], "Not escaped");
        else:
            print (p["name"], "Escaped");

def sort_by_danger (prisoners):
    prisoners.sort(key=lambda prisoner: prisoner["level_d"]);
    for p in prisoners:
        print (p["name"],"level_d",p["level_d"]);
    
def n_function (sort_by_age, sort_by_freed, sort_by_danger, prisoners):
    try:
        num_function = int(input("1 to sorted by age,\n2 to sorted by freed,\n3 to sorted by level_danger, \n0 to exsit.\n"));
        if num_function not in [0, 1, 2, 3]:
            raise ValueError()
    except ValueError:
        print("You didn't enter a valid option")
        return n_function(sort_by_age, sort_by_freed, sort_by_danger, prisoners)    

    match num_function:
        case 1:
            sort_by_age (prisoners);
            print ()
        case 2:
            sort_by_freed (prisoners);
            print ()
        case 3:
            sort_by_danger (prisoners);
            print ()
    if num_function  in [1, 2 ,3 ]:
        return n_function(sort_by_age, sort_by_freed, sort_by_danger, prisoners)

n_function(sort_by_age, sort_by_freed, sort_by_danger, prisoners);


 
        