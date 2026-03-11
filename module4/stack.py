# First assignment 

stack = []

while True:
    number = input("Enter the number to store and will break if entered character : ")
    try:
        number = int(number)
        stack.append(number)
    except:
        break

smallest_num = min(stack)
print(smallest_num)

# Second assignment

def undo_actions(actions, n):
    stack = actions[:]
    undone = []

    for _ in range(n):
        if not stack:
            break
        undone.append(stack.pop())

    return undone, stack


# Example usage
actions = ["open", "edit", "save", "close"]
n = 2

undone, remaining = undo_actions(actions, n)

print("Undone:", undone)
print("Left in stack:", remaining)


# Third assignment

def simplify_path(path: str) -> str:
    stack = []
    parts = path.split("/")

    for part in parts:
        if part == "" or part == ".":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)
    
print(simplify_path("/home//user/.././docs"))