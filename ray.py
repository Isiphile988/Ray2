mark = float(input())
experience = int(input())
honours = input()

if mark >= 65:
    if experience >= 2 or honours =="yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
