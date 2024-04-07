#In the sets.py file write code for the functions:

#get_students_who_took_prog1_and_prog2(prog1, prog2)
#get_students_who_took_prog2_only(prog1, prog2)
#get_students_who_took_prog1_not_prog_2(prog1, prog2) 
#get_students_who_took_prog2_not_prog_1(prog1, prog2) 

def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return prog1.intersection(prog2)
def get_students_who_took_prog2_only(prog1, prog2):
    return prog2 - prog1
def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    return prog1 - prog2
def get_students_who_took_prog2_not_prog_1(prog1, prog2):
    return prog2 - prog1