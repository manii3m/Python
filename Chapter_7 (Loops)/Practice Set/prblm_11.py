marks = []
for i in range(5):
    m = int(input("Enter your marks: "))
    marks.append(m)

f_marks = [m for m in marks if m >= 30]

if len(f_marks) == 0:
    print("Nothing to calculate")
else:
    total = sum(f_marks)
    avg = total / len(f_marks)
    print("Total:", total)
    print("Average:", avg)
    print("\nPercentage of each subject:")
    for i, m in enumerate(f_marks, start=1):
        perc = (m / 100) * 100
        print(f"Subject {i}: {perc}%")
    print(f_marks)