class GFG:
	def __init__(self, Marks):
		self.Marks = Marks
	def __lt__(self,other):
	    return self.Marks<other.Marks
student1_marks = GFG(90)
student2_marks = GFG(88)

# print(student1_marks.Marks < student2_marks.Marks) =>if lt method not present 
print(student1_marks < student2_marks)
