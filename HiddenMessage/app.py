#First section begin
class In:
    def __init__(self, number, word):
        self.number = number
        self.word = word

numberoflines = 0
def read_file(filename):
    structs=[]
    global numberoflines
    with open(filename, 'r')as file:
        for line in file:
            data = line.strip().split()
            number = int(data[0])
            word = data[1]
            In2 = In(number, word)
            numberoflines += 1
            structs.append(In2)
        return structs



#First section end
#Second section start

def create_pyramid(nums):
    pyramid = []
    i = 0
    row_length = 1
    while i < len(nums):
        row = nums[i:i + row_length]
        pyramid.append(row)
        i += row_length
        row_length += 1
    return pyramid

#Second section end
#Third section start
def decode(message_file):
    structs = read_file(message_file)
    numbers = []
    for i in structs:
        numbers.append(int(i.number))
    numbers.sort()
    py = create_pyramid(numbers)
    message = ""
    for i in py:
        for j in structs:
            if (i[-1] == j.number):
                message += " " + j.word
    print(message)
#Third section end
filename ='coding_qual_input.txt'
decode(filename)