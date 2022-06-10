# Arrows N Dots
### AND is a simple esoteric programming language (currently piggy-backing off of Python) which is functionally similar to BrainFuck, except that there are no loop functions. 
### AND is designed to be as simple to program an interpreter for as possible. This is why loops are omitted. Additionally, this creates more of a challenge for the AND developer in how extremely long the end code ends up being.

## AND works as follows:
- The interpreter creates a "tape" of 32 numbers. Each of these numbers default to 0.
- The "pointer" is created; this is essentially the cursor that the developer will use to select the number in the tape that they will perform functions on.
- The number the pointer has selected can be incremented or decremented by 1 with the increment and decrement commands.
- The number at the pointer can either be outputted as the character with the corresponding ASCII value or the raw number.

## AND has six functions:
`>` : Moves the pointer to the right.
`<` : Moves the pointer to the left.
`^` : Increment the value of the number at the pointer.
`v` : Decrement the value of the number at the pointer.
`.` : Print the value of the number at the pointer as an ASCII character.
`:` : Print the value of the number at the pointer as an integer.