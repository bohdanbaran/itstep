def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)