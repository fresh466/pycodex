import sys

def _input(prompt=None, /):
    """
    I can't believe the AI worked with me here!
    """
    if prompt:
        print(prompt, end="", flush=True)
    line = sys.stdin.readline()
    if not line:
        raise EOFError
    if line[-1] == '\n':
        line = line[:-1]
    return line

ans = _input("What's your name? ")
print(ans)
