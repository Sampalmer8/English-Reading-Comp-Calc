import math

def checkNum(num):
    deci = False
    for char in num:
        if char.isnumeric():
            continue
        elif char == "." and deci == False:
            deci = True
            continue
        else:
            return False
    return True

grades = []
num1 = input("Enter the grade of the first reading comprehension:")
if checkNum(num1) and float(num1) <= 100:
    num2 = input("Enter the grade of the second reading comprehension:")
    if checkNum(num2) and float(num2) <= 100:
        num3 = input("Enter the grade of the third reading comprehension:")
        if checkNum(num3) and float(num3) <= 100:
            num4 = input("Enter the grade of the fourth reading comprehension:")
            if checkNum(num4) and float(num4) <= 100:
                num5 = input("Enter the grade of the fifth reading comprehension:")
                if checkNum(num5) and float(num5) <= 100:
                    grades.append(num1)
                    grades.append(num2)
                    grades.append(num3)
                    grades.append(num4)
                    grades.append(num5)
                    grades.sort(reverse = True)
                    result = grades[:3]
                    nums = list(map(float, result))
                    final_grade = (nums[0] + nums[1] + nums[2]) / 3
                    print(final_grade)
                else:
                    print("Invalid number entered")
            else:
                print("Invalid number entered")
        else:
            print("Invalid number entered")
    else:
        print("Invalid number entered")
else:
    print("Invalid number entered")

