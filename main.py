import random

def guessing_game(min_num=1, max_num=100, max_attempts=10):
    secret_number = random.randint(min_num, max_num)
    print(secret_number)
    attempts = 0
    print(f"გამარჯობა! უნდა გამოიცნოთ რიცხვი {min_num}-{max_num} დიაპაზონში.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nცდა {attempts+1}/{max_attempts}. შეიყვანეთ თქვენი ვარაუდი: "))
            
            if guess < min_num or guess > max_num:
                print(f"გთხოვთ, შეიყვანოთ რიცხვი {min_num}-{max_num} დიაპაზონში.")
                continue

            attempts += 1

            if guess < secret_number:
                print("უფრო მაღალი!")
            elif guess > secret_number:
                print("უფრო დაბალი!")
            else:
                print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი {secret_number} მე - {attempts} მცდელობით.")
                return
        
        except ValueError:
            print("გთხოვთ, შეიყვანოთ სწორი რიცხვი.")

    print(f"\nსამწუხაროდ, ცდების რაოდენობა ამოიწურა. სწორი პასუხი იყო {secret_number}.")

# თამაშის გაშვება
guessing_game()
