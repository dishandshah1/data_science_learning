class scores:
    def __init__(self,subject,marks):
         self.subject = subject
         self.marks = marks 
    
    def total(self,*marks):
        try:
            score = 0
            for i in marks:
                if isinstance(i, (int, float)):           
                    print(i)
                    score = score + i
                else:
                    print("this is broken, invalid")
                    break

            return score    
        except Exception as e:
            print(e)

a = scores("Math",100)
print(a.total(55,433,54,[1,255]))