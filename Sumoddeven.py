sumeven=0
sumodd=0
i=1
while(i<=100):
  if(i%2==0):
    sumeven=sumeven+i
  else:
    sumodd=sumodd+i
  i=i+1
print("Sum of even : ",sumeven)
print("Sum of odd : ",sumodd)
