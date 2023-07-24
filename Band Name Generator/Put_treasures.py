# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#print(position[0])
#print(position[1])
row=int(position[0])-1 # it will sekect the row to be filled, -1 is done to avoid index out of range error
column=int(position[1])-1 # it will select the column of the row
#print('row',row)
#print('column',column)
map[row][column]='**'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

