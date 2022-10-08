"""You have a bowl with an even number of pieces of fruit in it. Half of them are bananas, and the other half are apples. 
You need 3 apples to make a pie. 
the task is to evaluate the total number of pies that you can make with the apples that are in your bowl given to total amount of fruit in the bowl.
Input Format is an integer that represents the total amount of fruit in the bowl.
Output Format is an integer representing the total number of whole apple pies that you can make."""
fruit = int(input())
app=0
if (fruit<=4):
   pie=0
else:
    app=int(fruit/2)
    pie=int(app/3)
print(int(pie))
