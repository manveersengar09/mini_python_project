
#MINI PROJECT:- KON BANEGA CROREPATI {K.B.C.}

questions = [
    [" QUES 1 } What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    [" QUES 2 } Which language is used for web apps?", "Python", "JavaScript", "HTML", "All of the above", 4],
    [" QUES 3 } Who is the founder of Microsoft?", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Jeff Bezos", 2],
    [" QUES 4 } Which is the largest planet?", "Venus", "Saturn", "Jupiter", "Mars", 3],
    [" QUES 5 } Which year did India get independence?", "1947", "1956", "1963", "1950", 1],
    [" QUES 6 } The Taj Mahal is located in which city?", "Delhi", "Agra", "Jaipur", "Mumbai", 2],
    [" QUES 7 } Which river is known as the ‘Ganga of the South’?", "Krishna", "Godavari", "Kaveri", "Yamuna", 3],
    [" QUES 8 } Who wrote the national anthem of India?", "Bankim Chandra Chatterjee", "Rabindranath Tagore", "Mahatma Gandhi", "Subhash Chandra Bose", 2],
    [" QUES 9 } What is the chemical symbol for water?", "O2", "H2O", "CO2", "NaCl", 2],
    [" QUES 10} How many states are there in India?", "28", "27", "29", "26", 1],
    [" QUES 11} Which sport is P.V. Sindhu associated with?", "Cricket", "Hockey", "Tennis", "Badminton", 4],
    [" QUES 12} Which is the hottest planet in the solar system?", "Mercury", "Mars", "Venus", "Saturn", 3],
    [" QUES 13} Who was the first President of India?", "Dr. Rajendra Prasad", "Zakir Husain", "R. Venkataraman", "Sarvepalli Radhakrishnan", 1],
    [" QUES 14} Which animal is known as the Ship of the Desert?", "Camel", "Horse", "Donkey", "Elephant", 1],
    [" QUES 15} Which Indian city is called the Pink City?", "Lucknow", "Hyderabad", "Jaipur", "Jodhpur", 3],
    [" QUES 16} Who is known as the Father of the Nation?", "Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", "Sardar Patel", 2],
    [" QUES 17} What is the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    [" QUES 18} Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium", 3],
    [" QUES 19} Who discovered gravity?", "Isaac Newton", "Albert Einstein", "Galileo", "Nikola Tesla", 1],
    [" QUES 20} MS Dhoni is related to which sport?", "Football", "Cricket", "Basketball", "Baseball", 2]
]
name = input("ENTER YOUR NAME:-")
prizes = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 
    640000, 1250000, 2500000, 5000000, 10000000, 20000000, 40000000, 75000000, 90000000, 100000000
]
money = 0

for i in range(len(questions)):
    q = questions[i]
    print(f"\nQuestion {i+1} for ₹{prizes[i]}:")
    print(f"{q[0]}")
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")
    
    user_input = input("Enter your answer (1-4) or '0' to quit: ")
    if user_input == "0":
        print(f" {name} You have quit the game. Your winnings: ₹{money}")
        break
    elif int(user_input) == q[5]:
        money = prizes[i]
        print(f"Correct! {name} You have won ₹{money}")
    else:
        print("Wrong answer!")
        if i >= 4:
            print(f"{name} You have crossed the first milestone. You win ₹10000.")
        else:
            print(f" {name} You win nothing.")
        break

else:
    print(f"\nCongratulations! {name} You have won the top prize: ₹{money}")

print("Thank you for playing KBC Python Edition!")
