
print("welcome in Kaun Banega Crorepati")
q_list=[["how many continents are there?"],
        ["What is the capital of India?"],
        ["NG mein kaun sa course karaya jata hai?"]]
opt_list=[["four","nine","seven","eight"],
         ["chandigarh","bhopal","chennai","delhi"],
         ["software engineering","counseling","tourism","agriculture"]]
sol_list=["seven", "delhi","software engineering"]
i=0
count=0
lifeline=1
while i<len(q_list):
    print("this is your question:-")
    print(q_list[i])
    print("those are your option:-")
    j=0
    while j<len(opt_list[i]):
        print(opt_list[i][j])
        j=j+1
    if lifeline==1:
        print("choose yes for 50-50 lifeline")
        choose_lifeline=input("enter your option for lifeline=")
        if choose_lifeline=="yes":
            if opt_list[i]==sol_list[i]:
                print(sol_list[i],opt_list[i+1])
                lifeline+=1
            else:
                print(sol_list[i],opt_list[i])
                lifeline+=1
    else:
        print("your lifeline is over")
    sol=input("enter your solution")
    if sol==sol_list[i]:
        print("congrats,your next question is :-")
        count=count+1
    elif sol!=sol_list:
        print("you lose")
        break
    i=i+1
    if count==3:
        print("congrats!,you win")