for i in range(1,101):  #iterate through numbers 1 through 100
    output = ""         #string to hold output
    if i % 3 == 0:      #if the number is cleanly divisible by 3, add "Fizz" to the output
        output += "Fizz"
    if i % 5 == 0:      #if the number is cleanly divisible by 5, add "Buzz" to the output
        output += "Buzz"
    if output == "":    #if output remains empty (meaning it isn't a multiple of 3 or 5), then set it to i
        output = i
    print(output)