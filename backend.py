#imports the string module, which contains constants I need for this application
import string

#creates a list of all uppercase letters in ascii alphabet
upper_letters = list(string.ascii_uppercase)

#creates a list of all lowercase letters in ascii alphabet
lower_letters = list(string.ascii_lowercase)

#creates a list of numbers 0-9
numbers = list(string.digits)

#creates a list of special characters
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '=', '+', '?']

#creates a list that combines all the previous lists
master_list = list(upper_letters+lower_letters+numbers+special_characters)

#imports the random module, which defines a series of functions for generating or manipulating random integers
import random

#creates an empty list for us to start adding to
end_product = []

#for loop that says for every number in range 0-15, add a random choice from the master_list to our empty list called end_product
for x in range(15):
    end_product.append(random.choice(master_list))

#converts the 16 random characters in the end_product list to a string and prints it
password = ''.join(end_product)





#Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", p = password)

if __name__ == '__main__':
    app.run()










#Git
