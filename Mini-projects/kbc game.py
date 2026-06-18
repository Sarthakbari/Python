4# # this program is not correct error is there 
# # Questions =[ 
# # [
# # " who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None",4
# # ],

# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],

# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],

# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],


# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],


# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],


# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],



# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],



# # [" who invent python language ?" ,
# # "john", "will", "Noha", "Guido van Rossum", "None", 4],

# # ]

# # levels=[1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, ]
# # money=0
# # for i in range(0, len(Questions)):
# #     Question= Questions[i]
# #     print(f"\n\n\nQuestion for Rs. {levels[i]}")
# #     print(f"a.{Question[1]}      b.{Question[2]}")
# #     print(f"c.{Question[3]}      d.{Question[4]}")

# #     reply=int(input("Enter your ans (1-4)"))
# #     if (reply==Question[-1]):
# #         print(f"Correct Ans , you won Rs.{levels[i]}")
# #         if(i==4):
# #             money=10000
# #         elif(i==9):
# #             money= 320000
# #         elif(i==14):
# #             money=10000000
# #         else:
# #             print("Wrong Answer")
# #             break
# # print(f"Your taking money home is {money}")
           



# # without quit mode 

# # Questions = [
# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

# #     ["Who invented the Python language?",
# #      "John", "Will", "Noha", "Guido van Rossum", "None", 4]
# # ]

# # levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000]

# # money = 0

# # for i in range(len(Questions)):
# #     Question = Questions[i]
# #     print(f"\n\n\nQuestion for Rs. {levels[i]}")
# #     print(f"a.{Question[1]}      b.{Question[2]}")
# #     print(f"c.{Question[3]}      d.{Question[4]}")

# #     reply = int(input("Enter your answer (1-4): "))
# #     if reply == Question[-1]:
# #         print(f"Correct Answer! You won Rs.{levels[i]}")
# #         if i == 4:
# #             money = 10000
# #         elif i == 8:
# #             money = 320000
# #         elif i == len(Questions) - 1:
# #             money = 10000000
# #     else:
# #         print("Wrong Answer")
# #         break

# # print(f"Your prize money is {money}")



# # quit mode is there 
# Questions = [
#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4],

#     ["Who invented the Python language?",
#      "John", "Will", "Noha", "Guido van Rossum", "None", 4]
# ]

# levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000]

# money = 0

# for i in range(len(Questions)):
#     Question = Questions[i]
#     print(f"\n\n\nQuestion for Rs. {levels[i]}")
#     print(f"a.{Question[1]}      b.{Question[2]}")
#     print(f"c.{Question[3]}      d.{Question[4]}")

#     reply = input("Enter your answer (1-4), or 'q' to quit: ")
    
#     if reply.lower() == 'q':
#         print("Quitting the quiz...")
#         break
    
#     reply = int(reply)
    
#     if reply == Question[-1]:
#         print(f"Correct Answer! You won Rs.{levels[i]}")
#         if i == 4:
#             money = 10000
#         elif i == 8:
#             money = 320000
#         elif i == len(Questions) - 1:
#             money = 10000000
#     else:
#         print("Wrong Answer")
#         break

# print(f"Your prize money is {money}")



# code with harrys code 
questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")
