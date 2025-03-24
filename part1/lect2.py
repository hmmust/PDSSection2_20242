def calc_marks(m):
    return min(m),max(m),sum(m),sum(m)/len(m)
    
marks = [10,13,15,20,17]
x,y,z,m = calc_marks(marks)
x,y,_,_ = calc_marks(marks)
print(x,y)
#print(calc_marks(marks))

