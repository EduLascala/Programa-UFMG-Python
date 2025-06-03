# UFMG - Introduction to Programming with Python Exercises

This repository contains Python solutions for various programming exercises from the UFMG "Introduction to Programming" course. The exercises are organized into "Prova" (Tests) and "Semana" (Weeks), reflecting the course structure.

## Prova 1

These problems cover fundamental programming concepts, including basic arithmetic operations, input/output, and simple control flow.

### `problema1.py`
Calculates the future value of an investment given the initial investment, annual interest rate, and investment period in years.
**Concepts:** Input/Output, Floating-point arithmetic, Exponentiation.


### `problema2.py`
Distributes a prize among three people (Pedro, João, and Marcela) proportionally to their individual bets.
**Concepts:** Input/Output, Arithmetic operations, Proportions.


### `problema3.py`
Takes an integer `x` as input and calculates `(x*3)+1 + (x*2)-1`.
**Concepts:** Input/Output, Integer arithmetic.


### `problema4.py`
Calculates the sum of the digits of a four-digit integer.
**Concepts:** Input/Output, `while` loop, Modulo operator, Integer division.


### `teste.py`
Similar to `problema4.py`, this script also calculates the sum of the digits of an input integer.
**Concepts:** Input/Output, `while` loop, Modulo operator, Integer division.


## Prova 2

These problems involve conditional statements (`if/elif/else`) for decision-making and more complex logical evaluations.

### `problema1.py`
Determines the median of three input integers.
**Concepts:** Conditional statements (`if`), Logical operators.


### `problema2.py`
Classifies a triangle as Equilateral, Isosceles, or Scalene based on the lengths of its three sides. Includes input validation.
**Concepts:** Conditional statements (`if/elif/else`), Input validation, Geometric classification.


### `problema3.py`
Calculates an employee's gross salary, income tax (IR), INSS, FGTS, total deductions, and net salary based on their hourly wage and hours worked. Tax rates are tiered.
**Concepts:** Input/Output, Conditional statements (`if/elif/else`), Arithmetic operations, Percentage calculations.


### `problema4.py`
Solves a quadratic equation ($ax^2 + bx + c = 0$) and determines the real roots, if any, based on the discriminant.
**Concepts:** Input/Output, Quadratic formula, Conditional statements (`if/elif/else`), Square root.


## Prova 3

This section introduces functions and their application in solving problems like the FizzBuzz game, fuel consumption, and parking fee calculation.

### `problema1.py`
Implements the FizzBuzz game using a function. Returns "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, or the number itself otherwise.
**Concepts:** Functions, Modulo operator, Conditional statements (`if/elif/else`).


### `problema2.py`
Calculates fuel consumption and provides a rating ("Venda o carro!", "Econômico!", "Super econômico!") based on distance traveled and fuel consumed.
**Concepts:** Functions, Division, Conditional statements (`if/elif/else`).


### `problema3.py`
Calculates parking fees based on arrival and departure times. Fees are tiered and rounded up to the nearest hour for durations over 4 hours.
**Concepts:** Functions, Time calculations (minutes conversion), Conditional statements (`if/elif/else`), `math.ceil`.


### `teste.py`
Another version of the parking fee calculation, similar to `problema3.py`.
**Concepts:** Functions, Time calculations (minutes conversion), Conditional statements (`if/elif/else`), `math.ceil`.


## Prova 4

These problems demonstrate the use of loops (`for` and `while`) for iterative calculations and finding specific values within ranges.

### `problema1.py`
Calculates the sum of all proper divisors of a given integer `n`.
**Concepts:** Functions, `for` loop, Modulo operator, Summation.


### `problema2.py`
Calculates the sum of the series $1 + 1/2 + 1/3 + \dots + 1/n$.
**Concepts:** `for` loop, Floating-point summation.


### `problema3.py`
Determines how many months it takes for João's investment (renting a fixed income fund) to surpass Carlos's investment (savings account), given their initial amounts and monthly returns.
**Concepts:** `while` loop, Financial calculations, Percentage increase.


### `problema4.py`
Prints all perfect squares within a given range `[x, y]`.
**Concepts:** Nested `for` loops, Perfect squares.


### `problema5.py`
Reads a series of non-negative numbers and finds the largest and smallest among them. Input ends when a negative number is entered.
**Concepts:** `while` loop, Finding maximum and minimum values.


## Prova 5

This section focuses on string manipulation, including character processing, concatenation, and basic encryption (Caesar cipher).

### `problema1.py`
Reads two integers, sums them, and then removes all occurrences of the digit '0' from the sum.
**Concepts:** String conversion, String searching (`find`), String slicing, `while` loop.


### `problema2.py`
Combines two input words by alternating their characters.
**Concepts:** String iteration, String concatenation, `while` loop, String length (`len`).


### `problema3.py`
Decodes an "embaralhada" (scrambled) phrase by reversing each half of the string and then concatenating them.
**Concepts:** String slicing, String reversal, Conditional statements, String length.


### `problema4.py`
Implements a simple Caesar cipher to encrypt a word. Each letter is shifted by a given key value.
**Concepts:** Character ASCII values (`ord`, `chr`), String iteration, Character shifting, Modulo arithmetic (for wrapping around the alphabet).


## Semana 1

Basic Python programs covering arithmetic calculations, variable assignments, and type conversions.

### `problema1.py`
Calculates the perimeter of a circle, the area of a circle, and the volume of a sphere given the radius.
**Concepts:** Constants, Arithmetic operations, Input/Output.


### `problema2.py`
Calculates the final velocity and distance traveled of an object given initial velocity, acceleration, and time.
**Concepts:** Kinematic equations, Arithmetic operations, Input/Output.


### `problema3.py`
Converts a given time in seconds into hours, minutes, and seconds.
**Concepts:** Integer division, Modulo operator, Time conversion.


### `problema4.py`
Reverses a four-digit integer.
**Concepts:** String conversion, String slicing, Integer conversion.


## Semana 2

Programs focusing on conditional logic and comparisons to determine characteristics or apply rules.

### `problema1.py`
Finds the largest and smallest among five input integers and counts how many of them are divisible by 3.
**Concepts:** Conditional statements (`if`), Comparison operators, Modulo operator, Counting.


### `problema2.py`
Determines the type of traffic infraction (if any) based on registered speed and maximum allowed speed.
**Concepts:** Conditional statements (`if/elif/else`), Comparison operators, Percentage calculations.


### `problema3.py`
Checks if an individual is eligible for retirement based on age, years of contribution, and gender.
**Concepts:** Conditional statements (`if/elif/else`), Logical operators (`and`, `or`).


### `problema4.py`
Calculates a salary increase and the new salary based on tiered percentage raises.
**Concepts:** Conditional statements (`if/elif/else`), Percentage calculations.


## Semana 3

This set of problems emphasizes the use of functions to encapsulate logic and promote code reusability.

### `problema1.py`
A function `pagamento` that calculates a new salary based on tiered percentage increases, similar to `Semana 2/problema4.py`.
**Concepts:** Functions, Conditional statements (`if/elif/else`), Percentage calculations.


### `problema2.py`
A function `pagamento` that calculates an employee's net salary after applying tiered income tax deductions.
**Concepts:** Functions, Conditional statements (`if/elif/else`), Percentage calculations, Salary calculation.


### `problema3.py`
Contains two functions: `verifica_triangulo` to check if three given side lengths can form a triangle, and `tipo_triangulo` to classify a valid triangle as Equilateral, Isosceles, or Scalene.
**Concepts:** Functions, Triangle inequality theorem, Conditional statements (`if/elif/else`).


### `problema4.py`
A function `calcula_valor` that determines the total cost of fuel (gasoline 'a' or ethanol 'g') based on quantity and applies discounts according to the amount purchased.
**Concepts:** Functions, Conditional statements (`if/elif/else`), Percentage discounts.


## Semana 6

These problems involve file handling, reading data from text files, and processing strings within those files.

### `problema1.py`
Reads a text file named `texto.txt` and prints the longest line along with its length.
**Concepts:** File I/O (`open`, `close`), Iterating through lines, String length (`len`), Finding maximum.


### `problema2.py`
Reads `texto.txt` and identifies the longest word in the file, printing the word and its length.
**Concepts:** File I/O, String splitting (`split`), Iterating through words, Finding maximum.


### `problema3.py`
Reads `texto.txt` and prints all words that have a length greater than or equal to a user-specified integer `n`.
**Concepts:** File I/O, String splitting, Conditional statements, String length.


### `problema4.py`
Reads dates from a file named `datas.txt` (format `DD/MM/YYYY`) and determines the most recent date.
**Concepts:** File I/O, String slicing, Integer conversion, Date comparison logic.


### `problema5.py`
Reads student names and their four grades from `notas.txt`. Calculates the average for each student and prints the name and average for those with an average greater than 60.
**Concepts:** File I/O, String slicing, String splitting, Summation, Average calculation.


## Semana 7

This section focuses on recursion, solving mathematical and sequence-related problems using recursive functions.

### `problema1.py`
Calculates the sum of integers from `m` to `n` using recursion.
**Concepts:** Recursion, Base case, Recursive step, Summation.


### `problema2.py`
Calculates $k^n$ (k to the power of n) using recursion.
**Concepts:** Recursion, Base case, Recursive step, Exponentiation.


### `problema3.py`
Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm implemented recursively.
**Concepts:** Recursion, Euclidean algorithm, Modulo operator.


### `problema4.py`
Calculates the sum of the first `n` natural numbers using recursion.
**Concepts:** Recursion, Summation of natural numbers.


### `problema5.py`
Prints natural numbers from 0 up to `n` in ascending order using recursion.
**Concepts:** Recursion, Printing sequence.


### `problema6.py`
Prints even natural numbers from 0 up to `n` in ascending order using recursion.
**Concepts:** Recursion, Printing even sequence.


### `problema7.py`
Prints odd natural numbers from 1 up to `n` in ascending order using recursion.
**Concepts:** Recursion, Printing odd sequence.


## Semana 8

These problems introduce data structures like dictionaries and lists, and demonstrate their use in counting frequencies and sorting data.

### `problema1.py`
Finds the most frequent character in an input word.
**Concepts:** Dictionaries (hash maps), Character iteration, Frequency counting, List of tuples, Sorting.


### `problema2.py`
Finds the most frequent vowel in an input word.
**Concepts:** Dictionaries, Character iteration, Conditional statements, Frequency counting, List of tuples, Sorting.


### `problema3.py`
Reads student names and two grades, calculates the average, and then prints students sorted by average in descending order. Input ends when an empty name is entered.
**Concepts:** Lists of tuples, Input loop, Average calculation, Sorting.


### `problema4.py`
Reads a series of integers until -1 is entered, then finds and prints the most frequent number among the entered values.
**Concepts:** Dictionaries, `while` loop, Frequency counting, List of tuples, Sorting.
