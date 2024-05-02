# Simple KBC , there is 3 level in this game at Rs.3000 , Rs.10000 , Rs.160000.


question=[['what is the capital of india','new delhi','delhi ncr','noida','delhi',1],
          ['what is the capital of M.P.','Bhopal','Indore','Jaipur','lucknow',1],
          ['what is the capital of U.P.','Bhopal','Indore','Jaipur','lucknow',4],
          ['what is the capital of rajasthan','Bhopal','Indore','Jaipur','lucknow',3],
          ['what is the capital of haryana','Bhopal','Chandigarh','Jaipur','lucknow',2],
          ['what is the capital of Punjab','chnadigarh','Indore','Jaipur','lucknow',1],
          ['what is the capital of Tripura','Aizwal','Dispur','Gangtok','Shilong',1],
          ['what is the capital of Assam','Aizwal','Dispur','Gangtok','Shilong',2],
          ['what is the capital of Sikkim','Aizwal','Dispur','Gangtok','Shilong',3],
          ['what is the capital of Meghalaya','Aizwal','Dispur','Gangtok','Shilong',4],          
] 
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money =00
for i in range(0,len(question)):
    ques = question[i]
    print( f'\n\nQuestion for Rs{levels[i]} is:\n')
    print(f'{ques[0]}')
    print(f'1.{ques[1]}')                   
    print(f'2.{ques[2]}')
    print(f'3.{ques[3]}')
    print(f'4.{ques[4]}')
    reply = int(input('enter the correct ans:'))
    if (reply==ques[-1]):
        print(f'you have won Rs{levels[i]}, now go to next question.')
        if(i==2):
            money = 3000
        elif(i==4):
            money = 10000
        elif(i==8):
            money = 160000
    else:
        print('wrong answer')
        break
print(f'your take home amount is Rs.{money}')
