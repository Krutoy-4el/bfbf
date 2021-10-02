# config

CELL_SIZE = 1

# variables


def compare(greater, equal, lesser):
    return (
        "+>>>[<<]>[->-[<<]>]>[[-]<<<-" + lesser
        + ">>>>>]<<<[[-]<<-" + greater
        + ">>]<<[-" + equal + "]"
    )


# first six cells - current coordinates,
# of code and memory
# then buffer and max value
# comparator, current cell, depth var, flag of moving
width = 6 + 1 + 1 + 6 + 1 + 1 + 1
moveRight = (
    ">"*width + "[-" + "<"*(width+1) + "+" + ">"*(width+1) + "]" + "<[->+<]"*3
    + "<"*6 + "<[->+<]" + "<" + "<[->+<]"*6 + ">" + ">[-" + ">>>>>+>>>>+"
    + "<"*9 + "]>>>>>[-<<<<<+>>>>>]>[-<+>>>>>+<<<<]<[->+<]>>"
    + compare("", "<"*7 + "[-]<+" + ">"*8, "<"*7 + "+" + ">"*7) + "<"*8
)

moveLeft = (
    "[-<+>]>"*6 + ">" + "[-<+>]>" + ">"*6 + "[-<+>]>"*3 + "<"*(width+2)
    + "[-" + ">"*(width+1) + "+" + "<"*(width+1) + "]" + ">"
    + ">[-" + ">>>>>+>>>>+" + "<"*9 + "]>>>>>[-<<<<<+>>>>>]>>"
    + compare(
        "<"*7 + "-" + ">"*7,
        "<[-<+<<<<<+>>>>>>]<[->+<]" + "<"*6 + "-" + ">"*8,
        ""
    ) + "<"*8
)

moveToCode = (
    ">"*(width-1) + "+[" + "<"*(width-1) + moveLeft + ">[-" + ">"*5 + "+"
    + ">"*4 + "+" + "<"*9 + "]" + ">"*5 + "[-" + "<"*5 + "+" + ">"*5
    + "]<<<[->>>+" + ">"*5 + "+" + "<"*8 + "]>>>[-<<<+>>>]>>"
    + compare(
        "",
        (
            "<"*6 + "[->>>>+>>>>+" + "<"*8 + "]>>>>[-<<<<+>>>>]" + "<"*6
            + "[-" + ">"*6 + "+" + ">"*5 + "+" + "<"*11 + "]" + ">"*6
            + "[-" + "<"*6 + "+" + ">"*6 + "]>>"
            + compare("", ">"*8 + "-" + "<"*8, "")
        ),
        ""
    ) + ">"*8 + "]" + "<"*(width-1)
)

moveToPointer = (
    ">"*(width-1) + "+[" + "<"*(width-1) + moveRight + ">[-" + ">"*5 + "+"
    + ">"*4 + "+" + "<"*9 + "]" + ">"*5 + "[-" + "<"*5 + "+" + ">"*5 + "]<[->+"
    + ">"*5 + "+" + "<"*6 + "]>[-<+>]>>"
    + compare(
        "",
        (
            "<"*4 + "[->>+>>>>+" + "<"*6 + "]>>[-<<+>>]" + "<"*6 + "[-" + ">"*6
            + "+" + ">"*5 + "+" + "<"*11 + "]" + ">"*6 + "[-" + "<"*6 + "+"
            + ">"*6 + "]>>" + compare("", ">"*8 + "-" + "<"*8, "")
        ),
        ""
    ) + ">"*8 + "]" + "<"*(width-1)
)

incCodePtr = (
    ">>>[->>>+>>>>+" + "<"*7 + "]>>>[-<<<+>>>]>[-<+" + ">"*5
    + "+<<<<]<[->+<]>>"
    + compare("", "<"*5 + "[-]<+" + ">"*6, "<"*5 + "+" + ">"*5) + "<"*8
)

decCodePtr = (
    ">>>[->>>+>>>>+" + "<"*7 + "]>>>[-<<<+>>>]>>"
    + compare("<<<<<->>>>>", "<[-<+<<<+>>>>]<[->+<]<<<<->>>>>>", "")
    + "<"*8
)

incPointer = (
    ">>>>>[->+>>>>+" + "<"*5 + "]>[-<+>]>[-<+" + ">"*5 + "+<<<<]<[->+<]>>"
    + compare("", "<"*3 + "[-]<+" + ">"*4, "<"*3 + "+" + ">"*3) + "<"*8
)

decPointer = (
    ">>>>>[->+>>>>+" + "<"*5 + "]>[-<+>]>>"
    + compare("<<<->>>", "<[-<+<+>>]<[->+<]<<->>>>", "")
    + "<"*8
)

copyCommandToComparator = (
    "[-" + "<"*7 + "+<<<<+" + ">"*11 + "]" + "<"*11 + "[-" + ">"*11
    + "+" + "<"*11 + "]>>"
)

# program starts
print(">")
# hard-coded filling of max value cell
if CELL_SIZE == 1:
    print(">"*4 + "+++++[->+++++[->+++++[->++<]<]<]>>>+++++" + "<"*7)  # 255
else:
    raise ValueError("Not implemented.")

# reading code
print(">"*width)
print(
    "<+[>,[-" + "<"*7 + "+<<<<+" + ">"*11 + "]" + "<"*11 + "[-" + ">"*11
    + "+" + "<"*11 + "]" + ">"*5 + "+"*10 + "<<<"
)
print(compare("", ">"*8 + "->[-]" + "<"*9, "") + "<"*8)
print(moveRight)
print(">"*(width-1) + "]" + "<"*(width-1))

# copying coordinates to ptr
print(
    "[->>>>+>>+" + "<"*6 + "]" + ">"*6 + "[-" + "<"*6 + "+" + ">"*6 + "]"
    + "<"*5
)
print(
    "[->>>>+>+" + "<"*5 + "]" + ">"*5 + "[-" + "<"*5 + "+" + ">"*5 + "]"
    + "<"*6
)

print(moveToCode)

# checking command
print(">"*width + "[")
# comparing with plus
print(copyCommandToComparator)
print("+++++[->++++[->>++<<]<]>>>+++<<<")
print(compare("", ">"*6 + "+" + "<"*6, ""))
print(">"*9)
# comparing with minus
print(copyCommandToComparator)
print("+++[->+++[->>+++++<<]<]")
print(compare("", ">"*6 + "-" + "<"*6, ""))
print(">"*9)
# comparing with >
print(copyCommandToComparator)
print("+++[->++++[->>+++++<<]<]>>>++<<<")
print(
    compare(
        "",
        (
            "<"*8 + moveToPointer + ">"*14 + "[->>>+<<<]" + "<"*14 + moveRight
            + incPointer + ">"*width + "[-<<<+>>>]" + "<"*width + moveToCode
            + ">"*8
        ),
        ""
    )
)
print(">"*9)
# comparing with <
print(copyCommandToComparator)
print("+++[->++++[->>+++++<<]<]")
print(
    compare(
        "",
        (
            "<"*8 + moveToPointer + ">"*14 + "[->>>+<<<]" + "<"*14 + moveLeft
            + decPointer + ">"*width + "[-<<<+>>>]" + "<"*width + moveToCode
            + ">"*8
        ),
        ""
    )
)
print(">"*9)
# comparing with dot
print(copyCommandToComparator)
print("+++++[->++++[->>++<<]<]>>>++++++<<<")
print(compare("", ">"*6 + "." + "<"*6, ""))
print(">"*9)
# comparing with comma
print(copyCommandToComparator)
print("+++++[->++++[->>++<<]<]>>>++++<<<")
print(compare("", ">"*6 + "," + "<"*6, ""))
print(">"*9)
# comparing with [
print(copyCommandToComparator)
print("++[->+++++[->>+++++++++<<]<]>>>+<<<")
print(
    compare(
        "",
        (
            ">"*6 + "[-<<<<+<<<<+" + ">"*8 + "]" + "<"*8 + "[-" + ">"*8 + "+"
            + "<"*8 + "]>>" + compare(
                "",
                (
                    ">"*7 + "+[" + "<"*15 + moveRight + incCodePtr + ">"*width
                    + copyCommandToComparator
                    + "++[->+++++[->>+++++++++<<]<]>>>+<<<"
                    + compare("", ">"*7 + "+" + "<"*7, "") + ">"*9
                    + copyCommandToComparator
                    + "++[->+++++[->>+++++++++<<]<]>>>+++<<<"
                    + compare("", ">"*7 + "-" + "<"*7, "") + ">"*7 + "]"
                    + "<"*7
                ),
                ""
            )
        ),
        ""
    )
)
print(">"*9)
# comparing with ]
print(copyCommandToComparator)
print("++[->+++++[->>+++++++++<<]<]>>>+++<<<")
print(
    compare(
        "",
        (
            ">"*6 + "[-<<<<+<<<<+" + ">"*8 + "]" + "<"*8 + "[-" + ">"*8 + "+"
            + "<"*8 + "]>>" + compare(
                (
                    ">"*7 + "+[" + "<"*15 + moveLeft + decCodePtr + ">"*width
                    + copyCommandToComparator
                    + "++[->+++++[->>+++++++++<<]<]>>>+<<<"
                    + compare("", ">"*7 + "-" + "<"*7, "") + ">"*9
                    + copyCommandToComparator
                    + "++[->+++++[->>+++++++++<<]<]>>>+++<<<"
                    + compare("", ">"*7 + "+" + "<"*7, "") + ">"*7 + "]"
                    + "<"*7
                ),
                "",
                ""
            )
        ),
        ""
    )
)

# moving forward
print("<"*8)
print(moveRight)
print(incCodePtr)
print(">"*width)

print("]")

print("<"*width)
