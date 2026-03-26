# define a function draw_box that takes 3 parameters
# use a nested loop
# print char


def draw_box(width, height, char):
    for x in range(1, height + 1):
        for y in range(1, width + 1):
            print(char, end="")
        print()


draw_box(6, 2, "#")
draw_box(4, 2, "*")
