# find the maximum of three numbers
def find_max(a,b,c):
    return max(a,b,c)

# multiply all numbers in a list
def multiply_list(*nums,i=0):
    #product = value of first number in list and also covers the case of the list having 1 number
    product=nums[0]

    if (len(nums)==0):
       return 0

    if (len(nums) > 1):
        #nums[1:] = start at indeces 1 and go through list elements to the end of the list
        for num in nums[1:]:
            product = product * num
    
    return product

#reverse a string
def reverse(string):
    return string[::-1]

#check whether a number falls in a given range
def check_in_range(a,b,c):
    if a in range(b,c):
        return True
    else:
        return False

#pascal - solution source:https://replit.com/@SD-Team/1024-solution#main.py
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)



#outputs
print(find_max(48,100,226))
print(multiply_list(1,2,3,4))
print(f"This is the reverse of your string {reverse('This is reversed.')}")
print(check_in_range(3,4,10))
print(check_in_range(5,4,10)
pascal(6)