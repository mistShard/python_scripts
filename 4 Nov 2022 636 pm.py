# def main():
#     word = "mosiah"
#     print("Welcome to the guessing game.\n")
#     printHint(word)
#     wordTry = 0
#     attempt = ""
#     wordIndex = 0
#     guess = input("Please make a guess: ")
#     while attempt != word or guess != 0:
#          for y in guess:
#             if y in word and guess.index(y) == word[wordIndex]:
#                 attempt += y.capitalize()
#                 wordIndex += 1
#             elif y in word and guess.index(y) != word[wordIndex]:
#                 attempt += y
#                 wordIndex += 1
#             else:
#                 attempt += "_"
#                 wordIndex += 1
#          wordTry += 1
#          print(f"Your hint is {attempt}")
#          guess = input("Please, hazard a guess: ")

# #while count != hint:
# def printHint(word):
#     blank = ["_  " for i in word]
#     p = "".join(blank)
#     print(f"Your hint is: {p}")    

# if __name__ =="__main__":
#            main()
           
        
alist = [233, 44, 32939, 3431]
from functools import reduce
add = lambda a, b: a + b
aa = reduce(add, alist)
print(aa)