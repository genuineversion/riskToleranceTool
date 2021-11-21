purpose="This risk tolerance questionnaire is designed with one specific financial goal in mind. Your responses should be directed towards that specific goal."

riskToleranceTypes=[
    "Conservative",
    "Moderately low",
    "Moderate",
    "Moderately high",
    "Aggressive"
]

objectiveTypes={
    "income":"Your primary objective when investing is to earn a regular stream of income from your investments.",
    "growth":"Your primary objective when making an investment decision is to grow the value of the investment through potential capital appreciation. This can be achieved at different magnitudes for risk appetite between moderate risk to aggressive risk."
}

experienceLevel={
    "veryExperienced": "You are well experienced which means you have practical knowledge when it comes to investing. You also have an active portfolio of investments and frequently invests directly in the capital market including security analysis, evaluation, and selection.",
    "Experienced": "As an experienced investor, you may consider a mix of professionally managed investment funds and direct investing in the capital market.",
    "Somewhat Experienced": "You are probably knowledgeable in some areas of investing and not so informed in other areas. You should largely take your investment decision through investment professionals and will need to familiarize yourself more with understanding investments.",
    "Inexperience": "You have little knowledge about investing, so, we will recommend that you start with mutual funds as this is professionally managed by investment experts. You should also familiarize yourself with a glossary of investment terms (link) and our articles directed towards providing investment literacy"
}


Question1={
    "Qst": "What is your main investment goal?",
    "a":"Income: You are primarily concerned about accruing benefits such as interest income on the investment or dividend income from shares",
    "b":"Growth: You are primarily concerned about capital appreciation, that is, increase in the price of your investment compared to when you bought it."
}

Question2={
    "Qst": "I plan to keep this money invested for",
    "a":"1 year or less",
    "b":"2 - 3 years",
    "c":"4 – 5 years",
    "d":"Above 5 years"
}

Question3={
    "Qst": "Which of the following best describes your attitude towards investment risks?",
    "a":"When making investment choices, I am primarily concerned about protecting my investments and ensure no loss of capital",
    "b":"I am willing to accommodate some loss of capital for an investment that also has a potential of providing higher returns even though there is no certainty of higher return."
}  

Question4={
    "Qst":"After making the investment decision and you have your money invested, which of the following will make you change your investment plan to a more stable option?",
    "a":"I am willing to take a loss up to 10% of my investment. Once it crosses 10%, I will switch to a more stable option",
    "b":"I can accommodate a loss up to 20%. I consider anything above too high and I will immediately switch to a less risk investment",
    "c":"I can accommodate losses up to 25% but any loss above 25% is a trigger for me to sell and switch to a less risky investment.",
    "d":"Even if there is a loss on my investment above 25%, I would not change my investment plan."
    } 

Question5={
    "Qst":"What is the primary source of funding your investment?",
    "a":"Savings from current and future self-employment",
    "b":"Savings from current and future salaried employment",
    "c":"Past savings without any future regular inflow",
    "d":"Pensions and gratuity from retirement",
    "e":"Inheritance & Gifts"
    } 

Question6={
    "Qst":"What is your current age bracket?",
    "a":"18 – 24 years",
    "b":"25 – 29 years",
    "c":"30 – 34 years",
    "d":"35 – 39 years",
    "e":"40 – 49 years",
    "f":"50 years and above"
    } 

Question7={
    "Qst":"How would losing money affect you?",
    "a":"It would not impact my current standard of living and I do not need to sell other investments as a result",
    "b":"It will affect me but I have other resources I could fall back on.",
    "c":"It would have an impact on my immediate standard of living."
    } 

Question8={
    "Qst":"When it comes to investing in stock or bond mutual funds (or individual stocks or bonds), I would describe myself as?",
    "a":"Very experienced",
    "b":"Experienced",
    "c":"Somewhat experienced",
    "d":"Inexperienced"
    } 

# Risk Tolerance Form & Response Collection
def rtForm():

    global response1, response2, response3, response4, response5, response6, response7, response8
    print(purpose)
    print("Question 1 \n")
    print(Question1["Qst"])
    print(f'{"a."} {Question1["a"]}')
    print(f'{"b."} {Question1["b"]}')
    response1=input("Enter a or b \n")

    print("\n")

    print("Question 2 \n")
    print(Question2["Qst"])
    print(f'{"a."} {Question2["a"]}')
    print(f'{"b."} {Question2["b"]}')
    print(f'{"c."} {Question2["c"]}')
    print(f'{"d."} {Question2["d"]}')
    response2=input("Enter a, b, c or d \n")

    print("\n")

    print("Question 3 \n")
    print(Question3["Qst"])
    print(f'{"a."} {Question3["a"]}')
    print(f'{"b."} {Question3["b"]}')
    response3=input("Enter a or b \n")
    
    print("\n")

    print("Question 4 \n")
    print(Question4["Qst"])
    print(f'{"a."} {Question4["a"]}')
    print(f'{"b."} {Question4["b"]}')
    print(f'{"c."} {Question4["c"]}')
    print(f'{"d."} {Question4["d"]}')
    response4=input("Enter a, b, c or d \n")

    print("\n")

    
    print("Question 5 \n")
    print(Question5["Qst"])
    print(f'{"a."} {Question5["a"]}')
    print(f'{"b."} {Question5["b"]}')
    print(f'{"c."} {Question5["c"]}')
    print(f'{"d."} {Question5["d"]}')
    print(f'{"e."} {Question5["e"]}')
    response5=input("Enter a, b, c, d or e \n")

    print("\n")

        
    print("Question 6 \n")
    print(Question6["Qst"])
    print(f'{"a."} {Question6["a"]}')
    print(f'{"b."} {Question6["b"]}')
    print(f'{"c."} {Question6["c"]}')
    print(f'{"d."} {Question6["d"]}')
    print(f'{"e."} {Question6["e"]}')
    print(f'{"f."} {Question6["f"]}')
    response6=input("Enter a, b, c, d, e or f \n")

    print("\n") 

        
    print("Question 7 \n")
    print(Question7["Qst"])
    print(f'{"a."} {Question7["a"]}')
    print(f'{"b."} {Question7["b"]}')
    print(f'{"c."} {Question7["c"]}')
    response7=input("Enter a, b or c \n")

    print("\n") 

    print("Question 8 \n")
    print(Question8["Qst"])
    print(f'{"a."} {Question8["a"]}')
    print(f'{"b."} {Question8["b"]}')
    print(f'{"c."} {Question8["c"]}')
    print(f'{"d."} {Question8["d"]}')
    response8=input("Enter a, b, c or d \n")

    print("\n")



# Applies logic to determine the appropriate risk tolerance level
def rtAnalysis():

    global riskTolerance
    if response2 == "a" or response3=="a" or response5=="c" or response6=="d" or response6=="f" or response7=="c":
        riskTolerance=riskToleranceTypes[0]
    elif response2=="b" and response4=="a":
        riskTolerance=riskToleranceTypes[1]
    elif response2=="b" and response4=="b":
        riskTolerance=riskToleranceTypes[2]
    elif response2=="b" and response4=="c":
        riskTolerance=riskToleranceTypes[2]
    elif response2=="b" and response4=="d":
        riskTolerance=riskToleranceTypes[2]
    elif response2=="c" and response4=="a":
        riskTolerance=riskToleranceTypes[1]
    elif response2=="c" and response4=="b":
        riskTolerance=riskToleranceTypes[2]
    elif response2=="c" and response4=="c":
        riskTolerance=riskToleranceTypes[3]
    elif response2=="c" and response4=="d":
        riskTolerance=riskToleranceTypes[3]
    elif response2=="d" and response4=="a":
        riskTolerance=riskToleranceTypes[2]
    elif response2=="d" and response4=="b":
        riskTolerance=riskToleranceTypes[3]
    elif response2=="d" and response4=="c":
        riskTolerance=riskToleranceTypes[3]
    elif response2=="d" and response4=="d":
        riskTolerance=riskToleranceTypes[4]

# This is also used to determine as part of the output to the user, advise based on the objective the user has selected as preference.
def objSelection():
    global userObjective
    if response1=="a":
        userObjective=objectiveTypes["income"]
    elif response1=="b":
        userObjective=objectiveTypes["growth"]

# This is also used to determine as part of the output to the user, advise based on the user's experience when it comes to investment based on what the user has selected.
def experience():
    global userX
    if response8=="a":
        userX=experienceLevel["veryExperienced"]
    elif response8=="b":
        userX=experienceLevel["Experienced"]
    elif response8=="c":
        userX=experienceLevel["Somewhat Experienced"]
    elif response8=="d":
        userX=experienceLevel["Inexperience"]
    
   


def resultOutput():
    print(riskTolerance)
    print(userX)
    print(userObjective)


rtForm()   
rtAnalysis()
objSelection()
experience()

print(f"Your risk tolerance level is {riskTolerance}")
print(userX)
print(userObjective)
