# First Assignment
Q1 = []

while True:
    num = input("Enter the number that you want to add: ")
    try:
        if num == "":
            break
        else:
            num = int(num)
            Q1.append(num)
    except:
        print(f"Enter a number")
stack = []
Q2 = []
for i in range(len(Q1)):
    if i <=2:
        stack.append(Q1[i])
    else:
        Q2.append(Q1[i])
print(Q2)
reversed_queue = []

while stack:
    reversed_queue.append(stack.pop())
for i in Q2:
    reversed_queue.append(i)

print(reversed_queue)


# Second Assignment

queue = []

while True:
    number = input("Enter the number and will break if entered character : ")
    try:
        number = int(number)
        queue.append(number)
        if len(queue) > 5:
            queue.pop(0)
    except:
        break

print(queue)


# Third Assignment

def round_robin(tasks):
    queue = tasks[:]
    finished = []

    while queue:
        name, time_needed = queue.pop(0)
        time_needed -= 2

        if time_needed > 0:
            queue.append((name, time_needed))
        else:
            finished.append(name)

    return finished


# Example usage
tasks = [("A", 3), ("B", 6), ("C", 1)]
print(round_robin(tasks))