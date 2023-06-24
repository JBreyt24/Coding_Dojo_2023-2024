# 1. integers 0 to 150
# for count in range(0,151):
#     print(count)

# 2. multiples of 5 from 5 to 1000
# for count in range(5,1001,5):
#     print(count)

# 3. integers 1 to 100: divisible by 5 "coding" if by 10 then "coding dojo"
# for count in range(1,101):
#     if count % 5 == 0:
#         print("Coding")
#     if count % 10 == 0:
#         print("Coding Dojo")
#     else:
#         print(count)

# 4. odd integers 0 to 500_000 and print final sum

# sum = 1
# for count in range(1,500_001,2):
#     count += sum
#     print(count)

#  5. start @ 2018 and count down by 4s

# for count in range(2018,0,-4):
    # print(count)

# 6. Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for count in range(lowNum, highNum + mult):
    if count % mult == 0:
        print(count) 

# output should show multiples of 10 starting at 10, and counting up to and stopping at 30