#Grading system
score = int(input("Enter the score:"))
if score >= 70:
  print("Grade A")
elif score >= 60 and score < 70:
  print("Grade B")
elif score >= 50 and score < 60:
  print("Grade C")
elif score >= 40 and score < 50:
  print("Grade D")
elif score <39 :
  print("Grade E")
else:
  print("Fail and the student takes supplementary test")