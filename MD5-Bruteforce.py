import time
import itertools, string
import hashlib
import sys
import signal
import threading


def attack(characters, hashValue):
    start_time = time.time()
    numTrys=0                   #Keep track of number of attempts
    for n in range(1, 32):      #Allow up 32 characters (No way to run this many characters realistically)
      for char in itertools.product(characters, repeat=n): #Permute all possiblity characters
          string = ''.join(char)                           #Add the char one char at a time
          savedString = string                             #Save the string in case it is the solution
          m = hashlib.md5()                                #This creates a md5 hash from the hash library
          m.update(string)                                 #Update this hash with a hash of string
          numTrys +=1                                      #Increase the number of trys that we have attempted
          if m.hexdigest() == hashValue:                   #Check if it matches the hash
              returnThis = savedString
              print (returnThis + "    %s seconds" % (time.time() - start_time))    #Print time to hash
              return returnThis                                                 #Return the found string so it is printed by main

def main():
    with open("hashes.txt") as file:                      #Open a hashfile
      for line in file:                                   #Go through all the lines
        line = line.strip()                               #Get rid of blank spaces
        characters = string.printable                     #Set characters to all possible print able characters
        password = attack(characters,line);                     #Call attach with characters and the input hash


if __name__ == "__main__":
    main()
