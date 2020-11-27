# Converting to binary

Congratulations on writing your program to convert a four-digit integer into an array!  

At the start of the first of these exercises, I explained that this was possible as any four-digit integer is actually a set of instructions for constructing a number from simpler parts.  For example, when we read the number 3260 we are being told to construct a number as follows:

1. First, multiply three by one thousand.
2. Next, multiply two by one hundred.
3. Next, multiply six by ten.
4. Next, multiply one by zero.
5. The number we are interested in is the sum of the four numbers that you obtained from these four multiplications.

We can express these instructions more compactly using the following summation:

![](https://render.githubusercontent.com/render/math?math=37=\sum_{n=0}^3a_n10^n)

where ![](https://render.githubusercontent.com/render/math?math=a_0=0), ![](https://render.githubusercontent.com/render/math?math=a_1=6), ![](https://render.githubusercontent.com/render/math?math=a_2=2) and ![](https://render.githubusercontent.com/render/math?math=a_3=3).

The ![](https://render.githubusercontent.com/render/math?math=a_n) coefficients in this expression are multiplied by powers of ten because we have ten basic symbols for representing numbers 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9.  We do not have a single symbol for representing the numbers eleven or ten so we have to use a pair of symbols to represent these numbers when they are represented in base ten.

The memory of a computer can be thought of as a series of switches that can be on or off.  Numbers stored in the memory of a computer thus cannot be stored in base ten as the basic components of the numbers - the switches in memory - cannot be in ten different states.  These switches can instead only be in two distinct states.  We thus only have two symbols 0 and 1 available to us.  There is no way that the numbers 2 or 3 can be stored using a single switch. 

In computer memory numbers are stored in base 2 rather than base 10.  If we find the number 100101 in the memory this is a set of instruction that tells us to:

1. First, multiply the number 1 by  32
2. Next, multiply the number 0 by 16
3. Next, multiply the number 0 by 8 
4. Next, multiply the number 1 by 4
5. Next, multiply the number 0 by 2
6. Next, multiply the number 1 by 1
7. The number 100101 is the sum of the six numbers that you obtained from these six multiplications.  In base 10 this is 37

We can express these instructions more compactly using the following summation:
 
![](https://render.githubusercontent.com/render/math?math=37=\sum_{n=0}^5a_n2^n)

where ![](https://render.githubusercontent.com/render/math?math=a_0=1), ![](https://render.githubusercontent.com/render/math?math=a_1=0), ![](https://render.githubusercontent.com/render/math?math=a_2=1), ![](https://render.githubusercontent.com/render/math?math=a_3=0), ![](https://render.githubusercontent.com/render/math?math=a_4=0) and ![](https://render.githubusercontent.com/render/math?math=a_5=1).

__In this exercise, you to use what you have learned by reading the above to complete the function `getBinary`.__  This function should take an integer with a value less than or equal to 63, which we shall call `N` as input.  The function will then return a NumPy array with 6 elements all of which should equal 0 or 1  The zeroth element in this numpy array should be the equivalent of ![](https://render.githubusercontent.com/render/math?math=a_0) in the sum above, the second will be ![](https://render.githubusercontent.com/render/math?math=a_1), the third ![](https://render.githubusercontent.com/render/math?math=a_2) and so on. 
