def GetName():
    name = raw_input ("Enter a student's name ")
    grade1 = raw_input ("Enter a grade: ")
grade2 = raw_input ("Enter a grade: ") 
grade3 = raw_input ("Enter a grade: ")
    grade4 = raw_input ("Enter a grade: ")
    return name, grade1, grade2, grade3, grade4

def GetGrades(grade1, grade2, grade3, grade4):
   
    if [grade1, grade2, grade3, grade4]  ==  'A' or [grade1, grade2, grade3, grade4] == 'a':
        [g1, g2, g3, g4] = 4

    elif [grade1, grade2, grade3, grade4]  ==  'B' or [grade1, grade2, grade3, grade4] == 'b':
        [g1, g2, g3, g4] = 3

    elif [grade1, grade2, grade3, grade4]  ==  'C' or [grade1, grade2, grade3, grade4] == 'c':
        [g1, g2, g3, g4] = 2

    elif [grade1, grade2, grade3, grade4]  ==  'D' or [grade1, grade2, grade3, grade4] == 'd':
        [g1, g2, g3, g4] = 1

    elif [grade1, grade2, grade3, grade4]  ==  'F' or [grade1, grade2, grade3, grade4] == 'f':
        [g1, g2, g3, g4] = 0
    
    else:
            return 'invalid grade'
    return g1, g2, g3, g4


