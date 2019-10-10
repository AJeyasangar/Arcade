

list = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i ', 'j ','k ', 'l ', 'm ', 'n', 'o' , 'p', 'q', 'r', 's', 't', 'u' , 'v', 'w' ,'x' , 'y', 'z']
enter_letter = input("letter")
for i in range(len(list) -1 ):
    if enter_letter == list[i]:
        print(i+10)
