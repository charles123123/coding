import random
def main():
   #put code here
   answer = random.randint(1,1000)
   print("welcome to the random number guessing game")
   tries = 4
   while (tries>0):
      guess = int(input("guess a number between 1 and 1000: "))
      if (answer == guess):
         print("You Win")
         break
      elif (guess>answer):
         print("guess is too big")
         tries = tries - 1
      else:
         print("guess is too small")
         tries = tries - 1
   if (tries==0):
      print("You Lose")
    
if __name__ == "__main__":
    main()
    
    	