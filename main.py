from math import sqrt, pi, ceil
from re import sub

CHARECTER_WIDTH_TO_HEIGHT_RAIO = 2
HOLE_TO_FULL_RATIO = 2.64
PI = pi

# given a (area) find and width of doughnut and doughnut hole
def calculate_sizes(area):
    # https://www.desmos.com/calculator/8zn0ov3d73
    x_1 = sqrt(area/(PI*CHARECTER_WIDTH_TO_HEIGHT_RAIO*(HOLE_TO_FULL_RATIO**2-1)))
    y_1 = x_1*CHARECTER_WIDTH_TO_HEIGHT_RAIO

    x_2 = x_1*HOLE_TO_FULL_RATIO
    y_2 = y_1*HOLE_TO_FULL_RATIO
    
    # find innaccuarcy:
    #new_area = PI*x_2*y_2 - PI*x_1*y_1
    #innacuracy = new_area-area
    #print("Found circle with innacuracy of:", innacuracy)

    # i got the x and y mixed up
    return(y_1, x_1, y_2, x_2)


def generate_doughnut(text, extra_size=0):
    # remove whitespaces (-space)
    text = sub("[^\\S ]+", "", text)
    
    x_1, y_1, x_2, y_2 = calculate_sizes(len(text))
    
    index = 0
    result = ""
    
    for y in range(ceil(2*y_2)+1):
        y = y-(y_2)
        for x in range(ceil(2*x_2)+1):
            x = x-(x_2)

            # in doughnut, not in hole
            if ((x**2)/((x_2+extra_size)**2) + (y**2)/((y_2+extra_size)**2) <= 1) and not \
               ((x**2)/((x_1+extra_size)**2) + (y**2)/((y_1+extra_size)**2) <= 1) and \
               index<len(text):
                result += text[index]
                index += 1
            else:
                result += " "

        
        result += "\n"

    # change the size of the doughnut untill it is right
    if (len(text)-index > 0):
        return generate_doughnut(text, extra_size+.01)

    return result


with open("text.txt", "r") as f:
    contents = f.read()

for text in contents.split("\n"):
    if not text: continue

    print(generate_doughnut(text))