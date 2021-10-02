import re


def combine_char(pos, neg, code):
    sum = 0

    for c in code:
        if c == pos:
            sum += 1
        elif c == neg:
            sum -= 1
        else:
            raise ValueError("Invalid match: " + c)

    if sum >= 0:
        return pos * sum
    else:
        return neg * -sum


def _compress(code):
    # remove any non [],.<>+-
    compressed = re.sub(r'[^\[\]\.,\+\-<>]', "", code)

    # remove leading [ comment ]
    compressed = re.sub(r'^\[[^\[\]]*\]', "", compressed)

    # remove [-][...]
    compressed = re.sub(r'(\[[\-\+]])\[[^\[\]]*\]', "[-]", compressed)

    # remove useless +- and <> combinations
    compressed = re.sub(
        r'[\+\-]*(?:\+-|-\+)[\+\-]*',
        lambda m: combine_char("+", "-", m.group()),
        compressed
    )
    compressed = re.sub(
        r'[<>]*(?:<>|><)[<>]*',
        lambda m: combine_char("<", ">", m.group()),
        compressed
    )

    return compressed


def compress(code: str, line=0):
    compressed = _compress(code)
    while compressed != _compress(compressed):
        compressed = _compress(compressed)
    return '\n'.join(
        compressed[i:i + line]
        for i in range(0, len(compressed), line)
    ) if line else compressed


if __name__ == '__main__':
    code = ""
    while True:
        try:
            code += input()
        except EOFError:
            break
    print(compress(code, 80), end='')
