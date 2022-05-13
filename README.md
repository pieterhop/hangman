# Testing Strategy:

This section consists of an overview of our testing approach for our implementation of the Hangman game.


## 1. Code Inspections
Code reviews were carried out by our team members in the attempt of detecting errors and bugs in the code. This low-tech testing technique was done manually (without the aid of testing software) and without executing the code. We have decided to start with code inspections because they offer a very time efficient and effective way to detect bugs in the code, although it's not a very robust testing technique it can be worthwhile for simple and short code like ours.

## 2. Control Flow Testing

Moving onto more robust testing techniques we proceed with code coverage tests.

We have conducted tests on 1 letter words, random length words (between 1 and 10) and 10+ letter words as form of boundary analysis testing.
That said, while describing our testing strategy we will be using a set word: "apple" instead of generating a random word for each iteration of the game for clarity and simplicity.

We use the following control flow graph to illustrate a simplified version of the execution of our program:

![simple_control_flow](hangman/simple_control_flow.jpg?raw=true "Title")

To achieve 100% Decision/condition coverage we will essentially need to test 5 different true-false branches of the decision tree:
A. **While Attempts > 0**
B. **If win** (which corresponds to no "_" remaining in the word that is being guessed)
C. **If attempts == 0** (no remaining attempts left)
D. **If len(guessed) != 1 || is not alphabetical** (If length of the user input is not equal to 1 or if its not a valid data type)
E. **If guessed in letters_tried** (If guessed letter has already been guessed before)

Statement number A does not depend on the user input but on the to-be guessed word that is selected by the code so the following test cases will be focused on statements B-E.

Additional notes:
 - Individual user inputs are divided by "-" and each individual input corresponds to the parameter that is passed to the guess() function (guessed = input() in the simplified control flow graph).
 - Attempts left should not be deducted on invalid input
 - Game should not stop on invalid input but simply give a warning
 - Game should only end after the user wins by guessing the word or loses by running out of attempts
 
|Test case number  | User Input | Expected Output
|--|--|--|
| 1 | a-p-l-e  | You won!|
| 2 | a-p-l-b-c-d-f | No more attempts left, you lose!|
| 3 | a-p-l-2  | Invalid Input, Enter another letter prompt |
| 4 | a-p-l-?   | Invalid Input, Enter another letter prompt |
| 5 | a-p-l-2-e | Invalid Input followed by You Won! |
| 6 | a-p-l-   | Invalid Input, Enter another letter prompt |
| 7 |  | Invalid Input, Enter another letter prompt |
| 8 | a-p-l-ee  | Invalid Input, Enter another letter prompt |
| 9 | -a-p-l-e | Invalid Input followed by You Won! |
| 10 | a-p-l-????  | Invalid Input, Enter another letter prompt |
| 11 | -a-p-l-e | Invalid Input followed by You Won! |
| 12 | a-a-p-l-p-a-e | Already guessed output, Enter another letter prompt, You Won! output at the end |
| 13 | a-a-p-l-p-a-a-p | Already guessed output, Enter another letter prompt |

Tests 1-2 are targeted at the conditional statements B and C.

Tests 3-5 are targeted at the conditional statement D.

Tests 6-11 are targeted at the conditional statement E. Equivalence partitions on the length of the input was used here:
|Invalid  | Valid | Invalid
|--|--|--|
|Input length < 1  | Input length == 1 | Input length > 1

Tests 11-13 are targeted at testing the flow of the game (outlined in "Additional Notes" above)
