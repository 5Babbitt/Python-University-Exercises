q = str(input("Is applicant qualified?(y/n): "))
e = int(input("Enter years of experience: "))
a = int(input("Enter applicants age: "))

if not(q == "y" or e > 5):
    print("Rejected")
elif ((e > 5 and a > 30) or (e > 5 and q == "y")):
    print("Call for interview")
else:
    print("Keep record on file")

