'''
This question is being asked in a SDE interview at Amazon.
The youtube url for the video is: https://www.youtube.com/watch?v=mjZpZ_wcYFg

Question: Run Length Encoding.
This technique was used in the past for compression of an image file. Since an image file is represented in pixels;
the compression algorithm would reduce it's size for efficient storage

Eg: Input aaaabbccc  ==> The output should be 4a2b3c
    Input aaaabbccca ==> The output should be 4a2b3c1a

Remember the order matters in Run Length and Encoding algorithm

'''

def func_rle(str_input):
    print("My Input string is: " + str_input)

    # Initialize a blank string for final output
    str_1 = ''

    # Initialize a blank variable for looping through string
    x = 0
    y = str_input[0]

    # Adding a blank space at the end of input string since I need to iterate on the entire string and need to include the last element
    str_input = str_input+' '

    for i in str_input:
        if y == i:
            x = x + 1
            y = i
        else:
            str_1 = str_1 + str(x) + y
            y = i
            x = 1
    print(str_1)


if __name__=="__main__":
    str_input='abcd'
    #str_input = 'aaaabbccc'
    #str_input = 'aaaabbccca'

    func_rle(str_input)