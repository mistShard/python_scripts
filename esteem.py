"""
The Rosenberg self-esteem scale is a self-esteem measure
developed by thesociologist Morris Rosenberg in 1965.
It is still used in social-science research today.
"""
fin_score = []
def esteem():
  print("""This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
""")
  q1 = q("I feel that I am a person of worth, at least on an\
 equal plane with others.")
  q2 = q("I feel that I have a number of good qualities.")
  q3 = q("All in all, I am inclined to feel that I am a\
 failure.")
  q4 = q("I am able to do things as well as most other people.")
  q5 = q("I feel I do not have much to be proud of.")
  q6 = q("I take a positive attitude towards myself.")
  q7 = q("On the whole, I am satisfied with myself.")
  q8 = q("I wish I could have more self respect for myself.")
  q9 = q("I certainly feel useless at times.")
  q10 = q("At times I think I am no good at all.")

  compute_positive_response(q1) 
  compute_positive_response(q2) 
  compute_positive_response(q4) 
  compute_positive_response(q6) 
  compute_positive_response(q7) 
  compute_negative_response(q3) 
  compute_negative_response(q5) 
  compute_negative_response(q8) 
  compute_negative_response(q9) 
  compute_negative_response(q10)

  print(sum(fin_score))


def q(x):
  print(x)
  y = input("Enter D, d, a, or A: ")
  return y
  
def compute_positive_response(question):
  score = 0
  if question == "D":
    score += 0
  elif question == "d":
    score += 1
  elif question == "a":
    score += 2
  elif question == "A":
    score += 3
  fin_score.append(score)

def compute_negative_response(question):
  score = 0
  if question == "D":
    score += 3
  elif question == "d":
    score += 2
  elif question == "a":
    score += 1
  elif question == "A":
    score += 0
  fin_score.append(score)

if __name__ == "__main__":
  esteem()