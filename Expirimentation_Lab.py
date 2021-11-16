# x = "*"
#
# for i in range(5):
#     print(x)
#     x = x + " *"

iterations = 6
rows = iterations
iterations = iterations + 1
for rows2 in range(1, iterations):
    for col in range(rows):
        print("*", end= " ")
    rows = rows-1
    print("")

