def read_file(file):
    x = open(file,'r', encoding = 'utf-8') #Opens the text file into variable x but the variable cannot be explored yet
    y = x.read() #By now it becomes a huge chunk of string that we need to separate line by line
    content = y.splitlines() #The splitline method converts the chunk of string into a list of strings
    return content

def pizza_comparison(pizzas):
    score=0
    for i in range(1,len(pizzas)):
        if ( (len(pizzas[i])+len(pizzas[0])-1) >= score):
            complement_pizza=set.union(set([string for string in list(pizzas[0]) if isinstance(string,str)]),set([string for string in list(pizzas[i]) if isinstance(string,str)]))
            if ( len(complement_pizza)>score or (len(complement_pizza)==score and len(pizzas[i])<len(next_pizza)) ):
                score=len(complement_pizza)
                next_pizza=pizzas[i]
                better_pizza_set=complement_pizza
                index_pizza=[integer for integer in list(pizzas[i]) if isinstance(integer,int)][0]
    return score,next_pizza,index_pizza,better_pizza_set


file = read_file('pizzas1.txt')
specifications=file[0];del(file[0])
specifications=specifications.split(' ')
numberOfPizzas=specifications[0]
Teams2=int(specifications[1])
Teams3=int(specifications[2])
Teams4=int(specifications[3])
pizzas=[]
ingredients=set()
betterPizzas=[]
score2=0;score3=0;score4=0
counter2=0;counter3=0;counter4=0
totalScore=0
index=0

for line in file:
    pizza=line.split(' ')
    del(pizza[0])
    ingredients=set(pizza)
    ingredients.add(index)
    pizzas.append(ingredients)
    index+=1
pizzasTemp0=pizzas.copy()
pizzas.sort(key=len,reverse=True)
pizzasTemp1=pizzas.copy()

for someIndex in range(0,len(pizzasTemp1)):
    if (len(pizzasTemp1)==1):break
    if ((counter4+counter3+counter2)>=(Teams2+Teams3+Teams4)):break
    
    firstIndex=[integer for integer in list(pizzasTemp1[0]) if isinstance(integer,int)][0]

    score2,secondPizza,secondIndex,betterTwoTeamPizza=pizza_comparison(pizzasTemp1)
    if(counter2>=Teams2):
        score2=0
    pizzasTemp2=pizzasTemp1.copy();pizzasTemp2[0]=betterTwoTeamPizza;pizzasTemp2.remove(secondPizza)
    if len(pizzasTemp2)==1:
        order=[firstIndex,secondIndex]
        betterPizzas.append(order)
        for element in order:
            toDelete=pizzasTemp0[element]
            pizzasTemp1.remove(toDelete)
        counter2+=1
        totalScore+=(score2)**2  
        break
    
    score3,thirdPizza,thirdIndex,betterThreeTeamPizza=pizza_comparison(pizzasTemp2)
    if(counter3>=Teams3):
        score3=0
    pizzasTemp3=pizzasTemp2.copy();pizzasTemp3[0]=betterThreeTeamPizza;pizzasTemp3.remove(thirdPizza)
    if len(pizzasTemp3)==1:
        order=[firstIndex,secondIndex,thirdIndex]
        betterPizzas.append(order)
        for element in order:
            toDelete=pizzasTemp0[element]
            pizzasTemp1.remove(toDelete)
        counter3+=1
        totalScore+=(score3)**2
        break
    
    score4,fourthPizza,fourthIndex,betterFourTeamPizza=pizza_comparison(pizzasTemp3)
    if(counter4>=Teams4):
        score4=0
    scores=[score2,score3,score4]
    print(scores)
    
    if ( (score4>score3 and score4>score2) and counter4<Teams4):
        order=[firstIndex,secondIndex,thirdIndex,fourthIndex]
        betterPizzas.append(order)
        for element in order:
            toDelete=pizzasTemp0[element]
            pizzasTemp1.remove(toDelete)
        counter4+=1
        totalScore+=(score4)**2   
    elif( ((score2>=score3 and score2!=0) or (score2>=score4 and score4!=0)) and (score2!=0 and counter2<Teams2)):
        order=[firstIndex,secondIndex]
        betterPizzas.append(order)
        for element in order:
            toDelete=pizzasTemp0[element]
            pizzasTemp1.remove(toDelete)
        counter2+=1
        totalScore+=(score2)**2
    elif (score3>=score4 and score3!=0 and score3>score2 and counter3<Teams3):  
        order=[firstIndex,secondIndex,thirdIndex]
        betterPizzas.append(order)
        for element in order:
            toDelete=pizzasTemp0[element]
            pizzasTemp1.remove(toDelete)
        counter3+=1
        totalScore+=(score3)**2
 
answer=open('submissionPizzaProblem1.txt','w+')
Deliveries=len(betterPizzas)
answer.write(str(Deliveries))

for eachOrder in betterPizzas:
    team=len(eachOrder)
    answer.write('\n'+str(team)+' ')
    for ingredients in eachOrder:
        answer.write(str(ingredients)+' ')