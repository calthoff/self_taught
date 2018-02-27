# Thank you so much for purchasing my book! Feel free to contact me at cory[at]theselftaughtprogrammer.io.
# If you are enjoying it, please consider leaving a review on Amazon :). https://www.amazon.com/dp/B01M01YDQA#customerReviews. Keep up the hard work!

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()
